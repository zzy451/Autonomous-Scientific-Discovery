// Original Microsoft Charticulator algorithms, MIT; see vendored source.
(function(Geometry) {
    function vectorLength(p) {
        return Math.sqrt(p.x * p.x + p.y * p.y);
    }
    Geometry.vectorLength = vectorLength;
    function pointDistance(p1, p2) {
        return Math.sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y));
    }
    Geometry.pointDistance = pointDistance;
    function vectorNormalize(p) {
        const len = Math.sqrt(p.x * p.x + p.y * p.y);
        return {
            x: p.x / len,
            y: p.y / len
        };
    }
    Geometry.vectorNormalize = vectorNormalize;
    function vectorRotate90(p) {
        return {
            y: p.x,
            x: -p.y
        };
    }
    Geometry.vectorRotate90 = vectorRotate90;
    function vectorRotate(p, radians) {
        return {
            x: p.x * Math.cos(radians) + p.y * Math.sin(radians),
            y: -p.x * Math.sin(radians) + p.y * Math.cos(radians)
        };
    }
    Geometry.vectorRotate = vectorRotate;
    function vectorAdd(p1, p2) {
        return {
            x: p1.x + p2.x,
            y: p1.y + p2.y
        };
    }
    Geometry.vectorAdd = vectorAdd;
    function vectorSub(p1, p2) {
        return {
            x: p1.x - p2.x,
            y: p1.y - p2.y
        };
    }
    Geometry.vectorSub = vectorSub;
    function vectorMul(p1, p2) {
        return {
            x: p1.x * p2.x,
            y: p1.y * p2.y
        };
    }
    Geometry.vectorMul = vectorMul;
    function vectorDiv(p1, p2) {
        return {
            x: p1.x / p2.x,
            y: p1.y / p2.y
        };
    }
    Geometry.vectorDiv = vectorDiv;
    function vectorScale(p, s) {
        return {
            x: p.x * s,
            y: p.y * s
        };
    }
    Geometry.vectorScale = vectorScale;
    function vectorDot(p1, p2) {
        return p1.x * p2.x + p1.y * p2.y;
    }
    Geometry.vectorDot = vectorDot;
    function vectorCross(p1, p2) {
        return p1.x * p2.y - p2.x * p1.y;
    }
    Geometry.vectorCross = vectorCross;
    function intervalOverlap(xMin, xMax, yMin, yMax) {
        return !(xMax < yMin || yMax < xMin);
    }
    Geometry.intervalOverlap = intervalOverlap;
    function rectOverlap(a1, a2) {
        return intervalOverlap(Math.min(a1.x1, a1.x2), Math.max(a1.x1, a1.x2), Math.min(a2.x1, a2.x2), Math.max(a2.x1, a2.x2)) && intervalOverlap(Math.min(a1.y1, a1.y2), Math.max(a1.y1, a1.y2), Math.min(a2.y1, a2.y2), Math.max(a2.y1, a2.y2));
    }
    Geometry.rectOverlap = rectOverlap;
    function applyZoom(zoom, pt) {
        return {
            x: pt.x * zoom.scale + zoom.centerX,
            y: pt.y * zoom.scale + zoom.centerY
        };
    }
    Geometry.applyZoom = applyZoom;
    function unapplyZoom(zoom, pt) {
        return {
            x: (pt.x - zoom.centerX) / zoom.scale,
            y: (pt.y - zoom.centerY) / zoom.scale
        };
    }
    Geometry.unapplyZoom = unapplyZoom;
    function degreesToRadians(degrees) {
        return degrees / 180 * Math.PI;
    }
    Geometry.degreesToRadians = degreesToRadians;
})(Geometry || (Geometry = {}));
function prettyNumber(x, digits = 8) {
    return x?.toFixed(digits).replace(/^([+-]?[0-9]*(\.[0-9]*[1-9]+)?)\.?0+$/, "$1");
}
function getRandomNumber() {
    return +("" + Math.random()).slice(2);
}
var Geometry;


//# sourceURL=src/core/common/math.ts
var PathTextAlignment = /*#__PURE__*/ function(PathTextAlignment) {
    PathTextAlignment["Start"] = "start";
    PathTextAlignment["Middle"] = "middle";
    PathTextAlignment["End"] = "end";
    return PathTextAlignment;
}({});
function makeRect(x1, y1, x2, y2, style, rx, ry) {
    return {
        type: "rect",
        x1,
        x2,
        y1,
        y2,
        style,
        rx,
        ry
    };
}
function makeCircle(cx, cy, r, style) {
    return {
        type: "circle",
        cx,
        cy,
        r,
        style
    };
}
function makeEllipse(x1, y1, x2, y2, style) {
    return {
        type: "ellipse",
        x1,
        x2,
        y1,
        y2,
        style
    };
}
function makeGroup(elements) {
    return {
        type: "group",
        elements,
        transform: {
            x: 0,
            y: 0,
            angle: 0
        }
    };
}
function makeLine(x1, y1, x2, y2, style) {
    return {
        type: "line",
        x1,
        x2,
        y1,
        y2,
        style
    };
}
function makePolygon(points, style) {
    return {
        type: "polygon",
        points,
        style
    };
}
function makeText(cx, cy, text, fontFamily, fontSize, style, selectable) {
    return {
        type: "text",
        cx,
        cy,
        text,
        fontFamily,
        fontSize,
        style,
        selectable
    };
}
class PathMaker {
    path = {
        type: "path",
        cmds: [],
        transform: ""
    };
    currentX;
    currentY;
    moveTo(x, y) {
        this.path.cmds.push({
            cmd: "M",
            args: [
                x,
                y
            ]
        });
    }
    lineTo(x, y) {
        this.path.cmds.push({
            cmd: "L",
            args: [
                x,
                y
            ]
        });
    }
    transformRotation(angle, x = 0, y = 0) {
        this.path.transform = `rotate(${angle} ${x} ${y})`;
    }
    setBeginArrowType(arrowType) {
        this.path.beginArrowType = arrowType;
    }
    setEndArrowType(arrowType) {
        this.path.endArrowType = arrowType;
    }
    cubicBezierCurveTo(c1x, c1y, c2x, c2y, x, y) {
        this.path.cmds.push({
            cmd: "C",
            args: [
                c1x,
                c1y,
                c2x,
                c2y,
                x,
                y
            ]
        });
    }
    quadraticBezierCurveTo(cx, cy, x, y) {
        this.path.cmds.push({
            cmd: "Q",
            args: [
                cx,
                cy,
                x,
                y
            ]
        });
    }
    arcTo(rx, ry, xAxisRotation, largeArcFlag, sweepFlag, x, y) {
        this.path.cmds.push({
            cmd: "A",
            args: [
                rx,
                ry,
                xAxisRotation,
                largeArcFlag,
                sweepFlag,
                x,
                y
            ]
        });
    }
    archimedeanSpiral(cx, cy, a, b, thetaMin, thetaMax, moveTo = false) {
        const ticks = Math.ceil(Math.abs(thetaMax - thetaMin) / (Math.PI / 6)) + 1;
        for(let i = 0; i < ticks; i++){
            const theta1 = i / ticks * (thetaMax - thetaMin) + thetaMin;
            const r1 = a + b * theta1;
            const x1 = r1 * Math.cos(theta1);
            const y1 = r1 * Math.sin(theta1);
            const theta2 = (i + 1) / ticks * (thetaMax - thetaMin) + thetaMin;
            const r2 = a + b * theta2;
            const x2 = r2 * Math.cos(theta2);
            const y2 = r2 * Math.sin(theta2);
            const scaler = (theta2 - theta1) / 3;
            if (moveTo && i == 0) {
                this.moveTo(cx + x1, cy + y1);
            }
            const dx1 = (b * Math.cos(theta1) - y1) * scaler;
            const dy1 = (b * Math.sin(theta1) + x1) * scaler;
            const dx2 = (b * Math.cos(theta2) - y2) * scaler;
            const dy2 = (b * Math.sin(theta2) + x2) * scaler;
            this.cubicBezierCurveTo(cx + x1 + dx1, cy + y1 + dy1, cx + x2 - dx2, cy + y2 - dy2, cx + x2, cy + y2);
        }
    }
    polarLineTo(cx, cy, angle1, r1, angle2, r2, moveTo = false) {
        if (moveTo) {
            const p1x = cx + Math.cos(Geometry.degreesToRadians(angle1)) * r1;
            const p1y = cy + Math.sin(Geometry.degreesToRadians(angle1)) * r1;
            this.moveTo(p1x, p1y);
        }
        if (Math.abs(angle2 - angle1) < 1e-6) {
            const p2x = cx + Math.cos(Geometry.degreesToRadians(angle2)) * r2;
            const p2y = cy + Math.sin(Geometry.degreesToRadians(angle2)) * r2;
            this.lineTo(p2x, p2y);
        } else {
            if (Math.abs(r1 - r2) < 1e-6) {
                if (angle2 > angle1) {
                    let a1 = angle1;
                    while(angle2 > a1){
                        let a2 = angle2;
                        if (a2 > a1 + 180) {
                            a2 = a1 + 180;
                        }
                        const p2x = cx + Math.cos(Geometry.degreesToRadians(a2)) * r1;
                        const p2y = cy + Math.sin(Geometry.degreesToRadians(a2)) * r1;
                        this.arcTo(r1, r1, 0, 0, 0, p2x, p2y);
                        a1 = a2;
                    }
                } else if (angle2 < angle1) {
                    let a1 = angle1;
                    while(angle2 < a1){
                        let a2 = angle2;
                        if (a2 < a1 - 180) {
                            a2 = a1 - 180;
                        }
                        const p2x = cx + Math.cos(Geometry.degreesToRadians(a2)) * r1;
                        const p2y = cy + Math.sin(Geometry.degreesToRadians(a2)) * r1;
                        this.arcTo(r1, r1, 0, 0, 1, p2x, p2y);
                        a1 = a2;
                    }
                }
            } else {
                const b = (r2 - r1) / (angle2 - angle1);
                const a = r1 - b * angle1;
                const deg2rad = Math.PI / 180;
                this.archimedeanSpiral(cx, cy, a, b / deg2rad, angle1 * deg2rad, angle2 * deg2rad);
            }
        }
    }
    closePath() {
        this.path.cmds.push({
            cmd: "Z",
            args: []
        });
    }
}
function makePath(style) {
    const maker = new PathMaker();
    maker.path.style = style;
    return maker;
}
function translation(x = 0, y = 0) {
    return {
        x,
        y,
        angle: 0
    };
}
function rotation(angle) {
    return {
        x: 0,
        y: 0,
        angle
    };
}
function concatTransform(a, b) {
    const theta = Geometry.degreesToRadians(a.angle);
    const cos = Math.cos(theta);
    const sin = Math.sin(theta);
    return {
        x: a.x + b.x * cos - b.y * sin,
        y: a.y + b.x * sin + b.y * cos,
        angle: a.angle + b.angle
    };
}
function transform(transform, a) {
    const theta = Geometry.degreesToRadians(transform.angle);
    const cos = Math.cos(theta);
    const sin = Math.sin(theta);
    return {
        x: a.x * cos - a.y * sin + transform.x,
        y: a.x * sin + a.y * cos + transform.y
    };
}
function transformDirection(transform, a) {
    const theta = Geometry.degreesToRadians(transform.angle);
    const cos = Math.cos(theta);
    const sin = Math.sin(theta);
    return {
        x: a.x * cos - a.y * sin,
        y: a.x * sin + a.y * cos
    };
}


//# sourceURL=src/core/graphics/elements.ts
function RK4(f, y0, t0, h, steps, result = new Array(steps)) {
    if (steps == 0) {
        return result;
    }
    result[0] = y0;
    let yp = y0;
    let tp = t0;
    for(let i = 1; i < steps; i++){
        const k1 = f(tp, yp);
        const k2 = f(tp + h / 2, yp + h * k1 / 2);
        const k3 = f(tp + h / 2, yp + h * k2 / 2);
        const k4 = f(tp + h, yp + h * k3);
        const yi = yp + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4);
        const ti = tp + h;
        result[i] = yi;
        yp = yi;
        tp = ti;
    }
    return result;
}
function linearApproximation(points, t) {
    let i1, i2;
    const w = t * (points.length - 1);
    i1 = Math.floor(w);
    i2 = i1 + 1;
    const k = w - i1;
    if (i1 < 0) {
        i1 = 0;
        i2 = 0;
    }
    if (i1 >= points.length - 1) {
        i1 = points.length - 1;
        i2 = points.length - 1;
    }
    return points[i1] * (1 - k) + points[i2] * k;
}
function findSegment(bounds, k) {
    for(let i = 0; i < bounds.length - 1; i++){
        const b1 = bounds[i];
        const b2 = bounds[i + 1];
        if (k >= b1 && k <= b2) {
            return [
                i,
                k - b1
            ];
        }
    }
    if (k < bounds[0]) {
        return [
            0,
            0
        ];
    } else {
        return [
            bounds.length - 2,
            bounds[bounds.length - 1] - bounds[bounds.length - 2]
        ];
    }
}
function linearInvert(points, result = new Array(points.length)) {
    const s0 = points[0];
    const s1 = points[points.length - 1];
    let ptr = 0;
    for(let i = 0; i < points.length; i++){
        const si = s0 + (s1 - s0) * i / (points.length - 1);
        while(ptr + 2 < points.length && si >= points[ptr + 1]){
            ptr += 1;
        }
        const sA = points[ptr];
        const tA = ptr / (points.length - 1);
        const sB = points[ptr + 1];
        const tB = (ptr + 1) / (points.length - 1);
        const ti = (si - sA) / (sB - sA) * (tB - tA) + tA;
        result[i] = ti;
    }
    return result;
}
class CurveParameterization {
    getNormalAtT(t) {
        const tangent = this.getTangentAtT(t);
        return {
            x: -tangent.y,
            y: tangent.x
        };
    }
}
class BezierCurveParameterization extends CurveParameterization {
    k3x;
    k2x;
    k1x;
    k0x;
    k3y;
    k2y;
    k1y;
    k0y;
    tToS;
    sToT;
    len;
    constructor(p1, p2, p3, p4){
        super();
        this.k3x = 3 * (p2.x - p3.x) + p4.x - p1.x;
        this.k2x = 3 * (p1.x + p3.x - 2 * p2.x);
        this.k1x = 3 * (p2.x - p1.x);
        this.k0x = p1.x;
        this.k3y = 3 * (p2.y - p3.y) + p4.y - p1.y;
        this.k2y = 3 * (p1.y + p3.y - 2 * p2.y);
        this.k1y = 3 * (p2.y - p1.y);
        this.k0y = p1.y;
        const steps = 100;
        this.tToS = RK4((t)=>this.getDsDtAtT(t), 0, 0, 1 / (steps - 1), steps);
        this.len = this.tToS[steps - 1];
        this.sToT = linearInvert(this.tToS);
    }
    getPointAtT(t) {
        return {
            x: this.k0x + t * (this.k1x + t * (this.k2x + t * this.k3x)),
            y: this.k0y + t * (this.k1y + t * (this.k2y + t * this.k3y))
        };
    }
    getTangentAtT(t) {
        const t2 = t * t;
        const dxdt = 3 * t2 * this.k3x + 2 * t * this.k2x + this.k1x;
        const dydt = 3 * t2 * this.k3y + 2 * t * this.k2y + this.k1y;
        const length = Math.sqrt(dxdt * dxdt + dydt * dydt);
        return {
            x: dxdt / length,
            y: dydt / length
        };
    }
    getDsDtAtT(t) {
        const t2 = t * t;
        const dxdt = 3 * t2 * this.k3x + 2 * t * this.k2x + this.k1x;
        const dydt = 3 * t2 * this.k3y + 2 * t * this.k2y + this.k1y;
        return Math.sqrt(dxdt * dxdt + dydt * dydt);
    }
    getSFromT(t) {
        return linearApproximation(this.tToS, t);
    }
    getTFromS(s) {
        return linearApproximation(this.sToT, s / this.len);
    }
    getLength() {
        return this.len;
    }
}
class LineSegmentParametrization extends CurveParameterization {
    p1;
    p2;
    length;
    tangent;
    constructor(p1, p2){
        super();
        this.p1 = p1;
        this.p2 = p2;
        this.length = Math.sqrt((p2.x - p1.x) * (p2.x - p1.x) + (p2.y - p1.y) * (p2.y - p1.y));
        this.tangent = {
            x: (p2.x - p1.x) / this.length,
            y: (p2.y - p1.y) / this.length
        };
    }
    getTangentAtT(t) {
        return this.tangent;
    }
    getPointAtT(t) {
        return {
            x: this.p1.x + (this.p2.x - this.p1.x) * t,
            y: this.p1.y + (this.p2.y - this.p1.y) * t
        };
    }
    getSFromT(t) {
        return t * this.length;
    }
    getTFromS(s) {
        return s / this.length;
    }
    getLength() {
        return this.length;
    }
}
class MultiCurveParametrization {
    segments;
    len;
    sBounds;
    constructor(segments){
        this.segments = segments;
        this.len = 0;
        this.sBounds = new Array(this.segments.length + 1);
        this.sBounds[0] = 0;
        for(let i = 0; i < this.segments.length; i++){
            this.len += this.segments[i].getLength();
            this.sBounds[i + 1] = this.len;
        }
    }
    getSegmentAtS(s) {
        const [pi, ps] = findSegment(this.sBounds, s);
        const p = this.segments[pi];
        const pt = p.getTFromS(ps);
        return [
            p,
            pt
        ];
    }
    getPointAtS(s) {
        const [p, t] = this.getSegmentAtS(s);
        return p.getPointAtT(t);
    }
    getTangentAtS(s) {
        const [p, t] = this.getSegmentAtS(s);
        return p.getTangentAtT(t);
    }
    getNormalAtS(s) {
        const [p, k] = this.getSegmentAtS(s);
        return p.getNormalAtT(k);
    }
    getFrameAtS(s) {
        const [p, t] = this.getSegmentAtS(s);
        return {
            p: p.getPointAtT(t),
            t: p.getTangentAtT(t),
            n: p.getNormalAtT(t)
        };
    }
    getLength() {
        return this.len;
    }
    getSegments() {
        return this.segments;
    }
}


//# sourceURL=src/core/graphics/bezier_curve.ts
class CoordinateSystem {
}
class CartesianCoordinates extends CoordinateSystem {
    origin;
    constructor(origin = {
        x: 0,
        y: 0
    }){
        super(), this.origin = origin;
    }
    getBaseTransform() {
        return {
            x: this.origin.x,
            y: this.origin.y,
            angle: 0
        };
    }
    transformPoint(x, y) {
        return {
            x,
            y
        };
    }
    transformDirectionAtPoint(x, y, dx, dy) {
        return {
            x: dx,
            y: dy
        };
    }
    transformPointWithBase(x, y) {
        return {
            x: x + this.origin.x,
            y: y + this.origin.y
        };
    }
    transformDirectionAtPointWithBase(x, y, dx, dy) {
        return {
            x: dx,
            y: dy
        };
    }
    getLocalTransform(x, y) {
        return {
            x,
            y,
            angle: 0
        };
    }
}
const sqrt60 = Math.sqrt(60);
class PolarCoordinates extends CoordinateSystem {
    origin;
    radial1;
    radial2;
    distortY;
    constructor(origin = {
        x: 0,
        y: 0
    }, radial1 = 0, radial2 = 1, distortY = false){
        super(), this.origin = origin, this.radial1 = radial1, this.radial2 = radial2, this.distortY = distortY;
    }
    getBaseTransform() {
        return {
            x: this.origin.x,
            y: this.origin.y,
            angle: 0
        };
    }
    transformRadial(radial) {
        if (this.distortY) {
            return Math.sqrt(Math.max(0, (this.radial1 + this.radial2) * radial - this.radial1 * this.radial2));
        } else {
            return radial;
        }
    }
    inverseTransformRadial(distance) {
        const y = distance / sqrt60;
        return y * y;
    }
    transformPoint(angle, radial) {
        return {
            x: this.transformRadial(radial) * Math.sin(Geometry.degreesToRadians(angle)),
            y: this.transformRadial(radial) * Math.cos(Geometry.degreesToRadians(angle))
        };
    }
    transformDirectionAtPoint(angle, radial, dx, dy) {
        const t = Geometry.degreesToRadians(-angle);
        return {
            x: dx * Math.cos(t) - dy * Math.sin(t),
            y: dx * Math.sin(t) + dy * Math.cos(t)
        };
    }
    getLocalTransform(angle, radial) {
        const t = Geometry.degreesToRadians(angle);
        return {
            x: this.transformRadial(radial) * Math.sin(t),
            y: this.transformRadial(radial) * Math.cos(t),
            angle: -angle
        };
    }
    transformPointWithBase(angle, radial) {
        const t = Geometry.degreesToRadians(angle);
        return {
            x: this.transformRadial(radial) * Math.sin(t) + this.origin.x,
            y: this.transformRadial(radial) * Math.cos(t) + this.origin.y
        };
    }
    transformDirectionAtPointWithBase(angle, radial, dx, dy) {
        const t = Geometry.degreesToRadians(-angle);
        return {
            x: dx * Math.cos(t) - dy * Math.sin(t),
            y: dx * Math.sin(t) + dy * Math.cos(t)
        };
    }
}
class BezierCurveCoordinates extends CoordinateSystem {
    origin;
    curve;
    constructor(origin = {
        x: 0,
        y: 0
    }, curve){
        super(), this.origin = origin;
        this.curve = curve;
    }
    getBaseTransform() {
        return {
            x: this.origin.x,
            y: this.origin.y,
            angle: 0
        };
    }
    transformPoint(x, y) {
        const frame = this.curve.getFrameAtS(x);
        return {
            x: frame.p.x + y * frame.n.x,
            y: frame.p.y + y * frame.n.y
        };
    }
    transformDirectionAtPoint(x, y, dx, dy) {
        const frame = this.curve.getFrameAtS(x);
        return {
            x: dx * frame.t.x + dy * frame.n.x,
            y: dx * frame.t.y + dy * frame.n.y
        };
    }
    getLocalTransform(x, y) {
        const frame = this.curve.getFrameAtS(x);
        const angle = Math.atan2(frame.t.y, frame.t.x) / Math.PI * 180;
        return {
            x: frame.p.x + y * frame.n.x,
            y: frame.p.y + y * frame.n.y,
            angle
        };
    }
    transformPointWithBase(x, y) {
        const p = this.transformPoint(x, y);
        return {
            x: p.x + this.origin.x,
            y: p.y + this.origin.y
        };
    }
    transformDirectionAtPointWithBase(x, y, dx, dy) {
        return this.transformDirectionAtPoint(x, y, dx, dy);
    }
    getLength() {
        return this.curve.getLength();
    }
    getCurve() {
        return this.curve;
    }
}
class CoordinateSystemHelper {
    coordinateSystem;
    constructor(coordinateSystem){
        this.coordinateSystem = coordinateSystem;
    }
    rect(x1, y1, x2, y2, style = {}, rx = 0, ry = 0) {
        const cs = this.coordinateSystem;
        if (cs instanceof CartesianCoordinates) {
            return makeRect(x1, y1, x2, y2, style, rx, ry);
        } else {
            const path = makePath(style);
            this.lineTo(path, x1, y1, x1, y2, true);
            this.lineTo(path, x1, y2, x2, y2, false);
            this.lineTo(path, x2, y2, x2, y1, false);
            this.lineTo(path, x2, y1, x1, y1, false);
            path.closePath();
            return path.path;
        }
    }
    ellipse(x1, y1, x2, y2, style = {}) {
        const cs = this.coordinateSystem;
        if (cs instanceof CartesianCoordinates) {
            return makeEllipse(x1, y1, x2, y2, style);
        } else {
            const path = makePath(style);
            const cx = (x1 + x2) / 2, cy = (y1 + y2) / 2;
            const rx = Math.abs(x2 - x1) / 2, ry = Math.abs(y2 - y1) / 2;
            const N = 32;
            for(let i = 0; i < N; i++){
                const theta1 = i / N * (Math.PI * 2);
                const theta2 = (i + 1) / N * (Math.PI * 2);
                this.lineTo(path, cx + rx * Math.cos(theta1), cy + ry * Math.sin(theta1), cx + rx * Math.cos(theta2), cy + ry * Math.sin(theta2), i == 0);
            }
            path.closePath();
            return path.path;
        }
    }
    line(x1, y1, x2, y2, style = {}) {
        const cs = this.coordinateSystem;
        if (cs instanceof CartesianCoordinates) {
            return makeLine(x1, y1, x2, y2, style);
        } else {
            const path = makePath(style);
            this.lineTo(path, x1, y1, x2, y2, true);
            return path.path;
        }
    }
    lineTo(path, x1, y1, x2, y2, newPath) {
        const cs = this.coordinateSystem;
        if (newPath) {
            const p = cs.transformPoint(x1, y1);
            path.moveTo(p.x, p.y);
        }
        if (cs instanceof CartesianCoordinates) {
            path.lineTo(x2, y2);
        }
        if (cs instanceof PolarCoordinates) {
            path.polarLineTo(0, 0, 90 - x1, cs.transformRadial(y1), 90 - x2, cs.transformRadial(y2), false);
        }
        if (cs instanceof BezierCurveCoordinates) {
            if (Math.abs(x1 - x2) < 1e-6) {
                const p = cs.transformPoint(x2, y2);
                path.lineTo(p.x, p.y);
            } else {
                let framePrevious = cs.getLocalTransform(x1, y1);
                const direction = Math.atan2(y2 - y1, x2 - x1);
                const segments = Math.max(2, Math.ceil(3 * cs.getCurve().getSegments().length * Math.abs(x2 - x1) / cs.getCurve().getLength()));
                for(let i = 1; i <= segments; i++){
                    const t = i / segments;
                    const frame = cs.getLocalTransform((x2 - x1) * t + x1, (y2 - y1) * t + y1);
                    const len = Geometry.pointDistance(frame, framePrevious) / 3;
                    const angle1 = Geometry.degreesToRadians(framePrevious.angle) + direction;
                    const angle2 = Geometry.degreesToRadians(frame.angle) + direction;
                    path.cubicBezierCurveTo(framePrevious.x + Math.cos(angle1) * len, framePrevious.y + Math.sin(angle1) * len, frame.x - Math.cos(angle2) * len, frame.y - Math.sin(angle2) * len, frame.x, frame.y);
                    framePrevious = frame;
                }
            }
        }
    }
    arcTo(path, rx, ry, x1, y1, x2, y2, sweepFlag = 1) {
        const cs = this.coordinateSystem;
        if (cs instanceof CartesianCoordinates) {
            path.arcTo(rx, ry, 0, 0, sweepFlag, x2, y2);
            return path.path;
        } else {
            this.lineTo(path, x1, y1, x2, y2, true);
            return path.path;
        }
    }
}


//# sourceURL=src/core/graphics/coordinate_system.ts
export { PathMaker, BezierCurveParameterization, MultiCurveParametrization, BezierCurveCoordinates, CoordinateSystemHelper };
