"""Render a 3D knowledge-archipelago draft with Blender Cycles (bpy, headless, GPU).
Reads layout_<variant>.npz + labels_<variant>.json from gen_layout.py; writes render_<variant>_<res>.png and
anchors_<variant>.json (label anchors projected to image pixels) for the vector label overlay.
Usage: python render.py <archipelago|islands|planet> [res=1024] [samples=64]
"""
import sys, json, math
import numpy as np
import bpy
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view

variant = sys.argv[1]
_res = sys.argv[2] if len(sys.argv) > 2 else "1024"
RX, RY = (int(v) for v in _res.split("x")) if "x" in _res else (int(_res), int(_res))
RES = RX; SPP = int(sys.argv[3]) if len(sys.argv) > 3 else 64
src = "archipelago" if variant == "planet" else variant
TEX = variant == "current"
CUT = "cut" in sys.argv
L = np.load(f"layout_{src}.npz"); H, own = L["H"], L["own"]
meta = json.load(open(f"labels_{src}.json"))
fields = meta["fields"]
STEP = 1
H, own = H[::STEP, ::STEP], own[::STEP, ::STEP]
ny, nx = H.shape
xs = L["xs"][::STEP] if "xs" in L.files else np.linspace(-1, 1, nx)
ys = L["ys"][::STEP] if "ys" in L.files else np.linspace(-1, 1, ny)
n = ny
ZS = 0.55                                     # vertical exaggeration


def hexrgb(h):
    h = h.lstrip("#"); return [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]


def srgb2lin(c):
    return [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]


def sat(c, s=1.25):
    m = sum(c) / 3; return [min(1, max(0, m + (x - m) * s)) for x in c]


COL = [srgb2lin(sat(hexrgb(f["color"]))) for f in fields]
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene

# ---------------- terrain mesh with vertex colours
verts, faces, cols = [], [], []
if variant == "planet":
    for i in range(n):
        for j in range(n):
            lon, lat = xs[j] * 1.25, -xs[i] * 1.05
            r = 1 + H[i, j] * 0.22
            verts.append((r * math.cos(lat) * math.sin(lon), r * math.sin(lat), r * math.cos(lat) * math.cos(lon)))
else:
    for i in range(ny):
        for j in range(nx):
            verts.append((xs[j], -ys[i], max(H[i, j], -0.06) * ZS))
if "cut" in sys.argv:
    from scipy.ndimage import binary_fill_holes, binary_dilation
    keep = binary_dilation(binary_fill_holes(own >= 0), iterations=5)
else:
    keep = np.ones((ny, nx), bool)
for i in range(ny - 1):
    for j in range(nx - 1):
        if keep[i, j] and keep[i + 1, j + 1] and keep[i, j + 1] and keep[i + 1, j]:
            a = i * nx + j; faces.append((a, a + 1, a + nx + 1, a + nx))
me = bpy.data.meshes.new("terrain"); me.from_pydata(verts, [], faces); me.update()
ca = me.color_attributes.new("col", "FLOAT_COLOR", "POINT")
from scipy.ndimage import gaussian_filter
hmax = max(float(H.max()), 1e-3)
base = np.zeros((ny, nx, 3))
for f in range(len(COL)):
    base[own == f] = COL[f]
base[own < 0] = srgb2lin([0.86, 0.84, 0.78])                       # beach / unowned land
base = np.stack([gaussian_filter(base[..., k], 1.4) for k in range(3)], -1)
t = np.clip(H / hmax, 0, 1)[..., None]
snow = np.array(srgb2lin([0.97, 0.97, 0.95]))
rgb = base * (0.72 + 0.28 * t) * (1 - t ** 3) + snow * t ** 3
sand = np.clip(1 - H / 0.012, 0, 1)[..., None] ** 2; rgb = rgb * (1 - sand) + np.array(srgb2lin([0.86, 0.83, 0.74])) * sand    # soft shoreline
if "cut" in sys.argv:
    from scipy.ndimage import binary_fill_holes as _bfh, gaussian_filter as _gf
    ALPHA = np.clip(_gf(_bfh(own >= 0).astype(float), 2.2) * 2.2 - 0.25, 0, 1)
else:
    ALPHA = np.ones((ny, nx))
rgba = np.concatenate([rgb, ALPHA[..., None]], -1).reshape(-1)
ca.data.foreach_set("color", rgba.astype(np.float32))
for p in me.polygons:
    p.use_smooth = True
ob = bpy.data.objects.new("terrain", me); sc.collection.objects.link(ob)
if RX > 2000:                                   # final resolution: one level of smooth subdivision, no faceting
    sub = ob.modifiers.new("smooth", "SUBSURF"); sub.levels = 1; sub.render_levels = 1
mat = bpy.data.materials.new("terrain"); mat.use_nodes = True
nt = mat.node_tree; bsdf = nt.nodes["Principled BSDF"]
attr = nt.nodes.new("ShaderNodeAttribute"); attr.attribute_name = "col"
nt.links.new(attr.outputs["Color"], bsdf.inputs["Base Color"]); bsdf.inputs["Roughness"].default_value = 0.85
if "cut" in sys.argv:
    nt.links.new(attr.outputs["Alpha"], bsdf.inputs["Alpha"])
if TEX:
    import os
    uv = me.uv_layers.new(name="uv")
    for poly in me.polygons:
        for li in poly.loop_indices:
            vi = me.loops[li].vertex_index; i, j = divmod(vi, n)
            uv.data[li].uv = (j / (n - 1), 1 - i / (n - 1))
    tex = nt.nodes.new("ShaderNodeTexImage"); tex.image = bpy.data.images.load(os.path.abspath("tex_current.png"))
    nt.links.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
ob.data.materials.append(mat)

# ---------------- water
water = bpy.data.materials.new("water"); water.use_nodes = True
wb = water.node_tree.nodes["Principled BSDF"]
wb.inputs["Base Color"].default_value = (*srgb2lin([0.86, 0.92, 0.93] if TEX else [0.42, 0.62, 0.72]), 1); wb.inputs["Roughness"].default_value = 0.18
if variant == "planet":
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1.0, segments=192, ring_count=96)
    w = bpy.context.active_object
elif CUT:
    from scipy.ndimage import binary_fill_holes, binary_dilation
    region = binary_dilation(binary_fill_holes(own >= 0), iterations=4)
    wv, wf = [], []
    vid = -np.ones((ny, nx), int)
    for i in range(ny):
        for j in range(nx):
            if region[i, j]:
                vid[i, j] = len(wv); wv.append((xs[j], -ys[i], 0.0))
    for i in range(ny - 1):
        for j in range(nx - 1):
            q = (vid[i, j], vid[i, j + 1], vid[i + 1, j + 1], vid[i + 1, j])
            if min(q) >= 0:
                wf.append(q)
    wm = bpy.data.meshes.new("water"); wm.from_pydata(wv, [], wf); wm.update()
    wa = wm.color_attributes.new("col", "FLOAT_COLOR", "POINT")
    flat = [ALPHA[i, j] for i in range(ny) for j in range(nx) if vid[i, j] >= 0]
    wa.data.foreach_set("color", np.array([[1, 1, 1, a_] for a_ in flat], np.float32).reshape(-1))
    wnt = water.node_tree; wat = wnt.nodes.new("ShaderNodeAttribute"); wat.attribute_name = "col"
    wnt.links.new(wat.outputs["Alpha"], wnt.nodes["Principled BSDF"].inputs["Alpha"])
    w = bpy.data.objects.new("water", wm); sc.collection.objects.link(w)
    bpy.ops.mesh.primitive_plane_add(size=8, location=(0, 0, -0.065))
    catcher = bpy.context.active_object; catcher.is_shadow_catcher = True
else:
    bpy.ops.mesh.primitive_plane_add(size=6, location=(0, 0, 0.0))
    w = bpy.context.active_object
w.data.materials.append(water)
for p in w.data.polygons:
    p.use_smooth = True

# ---------------- bridges (islands variant): arcs between island centres, radius ~ sqrt(shared records)
if variant == "islands":
    cen = meta["meta"]["centres"]
    br = bpy.data.materials.new("bridge"); br.use_nodes = True
    bb = br.node_tree.nodes["Principled BSDF"]; bb.inputs["Base Color"].default_value = (0.95, 0.93, 0.88, 1); bb.inputs["Roughness"].default_value = 0.5
    for e in meta["meta"]["bridges"]:
        a, b = Vector((*cen[e["a"]], 0)), Vector((*cen[e["b"]], 0))
        a.y, b.y = -a.y, -b.y
        mid = (a + b) / 2; d = (b - a).length
        cu = bpy.data.curves.new("br", "CURVE"); cu.dimensions = "3D"
        sp = cu.splines.new("BEZIER"); sp.bezier_points.add(1)
        for k, (p, hd) in enumerate(((a, a + Vector((0, 0, 0.30 * d))), (b, b + Vector((0, 0, 0.30 * d))))):
            sp.bezier_points[k].co = p + Vector((0, 0, 0.05)); sp.bezier_points[k].handle_left = hd; sp.bezier_points[k].handle_right = hd
        cu.bevel_depth = 0.0025 * math.sqrt(e["n"]); cu.bevel_resolution = 4
        o = bpy.data.objects.new("br", cu); o.data.materials.append(br); sc.collection.objects.link(o)

# ---------------- light, world, camera
sun = bpy.data.lights.new("sun", "SUN"); sun.energy = 4.6; sun.angle = math.radians(3.5); sun.color = (1.0, 0.95, 0.88)
so = bpy.data.objects.new("sun", sun); so.rotation_euler = (math.radians(60), 0, math.radians(-42)); sc.collection.objects.link(so)
world = bpy.data.worlds.new("w"); world.use_nodes = True
world.node_tree.nodes["Background"].inputs["Color"].default_value = (0.62, 0.74, 0.88, 1)
world.node_tree.nodes["Background"].inputs["Strength"].default_value = 0.40
sc.world = world
cam = bpy.data.cameras.new("cam"); cam.lens = 50
co = bpy.data.objects.new("cam", cam); sc.collection.objects.link(co); sc.camera = co
if variant == "planet":
    co.location = (0.0, -1.2, 4.6); target = Vector((0, 0, 0))
elif variant == "current":
    co.location = (0.0, -2.45, 2.10); target = Vector((0, 0.05, 0))
    so.rotation_euler = (math.radians(62), 0, math.radians(-40))
elif RX > RY:
    cam.lens = 50; co.location = (0.0, -3.40, 4.85); target = Vector((0.16, -0.12, 0))
else:
    co.location = (0.0, -2.25, 2.12); target = Vector((0, 0.02, 0))
d = target - co.location; co.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()

# ---------------- render settings (GPU OptiX)
sc.render.engine = "CYCLES"
prefs = bpy.context.preferences.addons["cycles"].preferences; prefs.compute_device_type = "OPTIX"; prefs.get_devices()
for dv in prefs.devices:
    dv.use = dv.type == "OPTIX"
sc.cycles.device = "GPU"; sc.cycles.samples = SPP; sc.cycles.use_denoising = True
sc.render.resolution_x = RX; sc.render.resolution_y = RY; sc.render.film_transparent = CUT
sc.render.image_settings.color_mode = "RGBA" if CUT else "RGB"
sc.view_settings.view_transform = "AgX"; sc.view_settings.look = "AgX - Medium High Contrast"
import os; sc.render.filepath = os.path.abspath(f"render_{variant}{'_cut' if CUT else ''}_{RX}x{RY}.png")
bpy.ops.render.render(write_still=True)

# ---------------- project label anchors to pixels
out = []
for lab in meta["labels"]:
    x, y = lab["xy"]; z = lab["z"]
    if variant == "planet":
        X, Y = x * 1.35, y * 1.35; rho = math.hypot(X, Y); c = 2 * math.asin(min(1, rho / 2))
        lat = math.asin(Y * math.sin(c) / rho) if rho else 0; lon = math.atan2(X * math.sin(c), rho * math.cos(c)) if rho else 0
        r = 1 + z * 0.35 + 0.01; p = Vector((r * math.cos(lat) * math.sin(lon), -r * math.sin(lat), r * math.cos(lat) * math.cos(lon)))
    else:
        p = Vector((x, -y, z * ZS + 0.01))
    v = world_to_camera_view(sc, co, p)
    out.append(dict(lab, px=[v.x * RX, (1 - v.y) * RY], depth=v.z))
json.dump(dict(res=RES, rx=RX, ry=RY, labels=out), open(f"anchors_{variant}{'_cut' if CUT else ''}.json", "w"), indent=1)
print("done", sc.render.filepath)
