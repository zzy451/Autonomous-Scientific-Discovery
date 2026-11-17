// ============================================================
// Priority Queue (based on Adam Hooper's js-priority-queue)
// ============================================================
function PriorityQueue(options) {
    this.comparator = options.comparator || function(a,b){return a-b};
    this.data = [];
    this.length = 0;
}
PriorityQueue.prototype.queue = function(value) {
    this.data.push(value);
    this.length++;
    this._bubbleUp(this.data.length - 1);
};
PriorityQueue.prototype.dequeue = function() {
    var ret = this.data[0];
    var last = this.data.pop();
    this.length--;
    if (this.data.length > 0) {
        this.data[0] = last;
        this._sinkDown(0);
    }
    return ret;
};
PriorityQueue.prototype._bubbleUp = function(pos) {
    while (pos > 0) {
        var parent = Math.floor((pos - 1) / 2);
        if (this.comparator(this.data[pos], this.data[parent]) < 0) {
            var tmp = this.data[parent];
            this.data[parent] = this.data[pos];
            this.data[pos] = tmp;
            pos = parent;
        } else break;
    }
};
PriorityQueue.prototype._sinkDown = function(pos) {
    var len = this.data.length;
    while (true) {
        var left = 2*pos+1, right = 2*pos+2, smallest = pos;
        if (left < len && this.comparator(this.data[left], this.data[smallest]) < 0) smallest = left;
        if (right < len && this.comparator(this.data[right], this.data[smallest]) < 0) smallest = right;
        if (smallest !== pos) {
            var tmp = this.data[pos];
            this.data[pos] = this.data[smallest];
            this.data[smallest] = tmp;
            pos = smallest;
        } else break;
    }
};

// ============================================================
// Language generation (from mewo2/naming-language)
// ============================================================
function shuffled(list) {
    var newlist = [];
    for (var i = 0; i < list.length; i++) newlist.push(list[i]);
    for (var i = list.length - 1; i > 0; i--) {
        var tmp = newlist[i];
        var j = randrange(i);
        newlist[i] = newlist[j];
        newlist[j] = tmp;
    }
    return newlist;
}
function choose(list, exponent) {
    exponent = exponent || 1;
    return list[Math.floor(Math.pow(Math.random(), exponent) * list.length)];
}
function randrange(lo, hi) {
    if (hi == undefined) { hi = lo; lo = 0; }
    return Math.floor(Math.random() * (hi - lo)) + lo;
}
function join(list, sep) {
    if (list.length == 0) return '';
    sep = sep || '';
    var s = list[0];
    for (var i = 1; i < list.length; i++) { s += sep; s += list[i]; }
    return s;
}
function capitalize(word) {
    return word[0].toUpperCase() + word.slice(1);
}
function spell(lang, syll) {
    if (lang.noortho) return syll;
    var s = '';
    for (var i = 0; i < syll.length; i++) {
        var c = syll[i];
        s += lang.cortho[c] || lang.vortho[c] || defaultOrtho[c] || c;
    }
    return s;
}
function makeSyllable(lang) {
    while (true) {
        var syll = "";
        for (var i = 0; i < lang.structure.length; i++) {
            var ptype = lang.structure[i];
            if (lang.structure[i+1] == '?') {
                i++;
                if (Math.random() < 0.5) continue;
            }
            syll += choose(lang.phonemes[ptype], lang.exponent);
        }
        var bad = false;
        for (var i = 0; i < lang.restricts.length; i++) {
            if (lang.restricts[i].test(syll)) { bad = true; break; }
        }
        if (bad) continue;
        return spell(lang, syll);
    }
}
function getMorpheme(lang, key) {
    if (lang.nomorph) return makeSyllable(lang);
    key = key || '';
    var list = lang.morphemes[key] || [];
    var extras = 10;
    if (key) extras = 1;
    while (true) {
        var n = randrange(list.length + extras);
        if (list[n]) return list[n];
        var morph = makeSyllable(lang);
        var bad = false;
        for (var k in lang.morphemes) {
            if (lang.morphemes[k].includes(morph)) { bad = true; break; }
        }
        if (bad) continue;
        list.push(morph);
        lang.morphemes[key] = list;
        return morph;
    }
}
function makeWord(lang, key) {
    var nsylls = randrange(lang.minsyll, lang.maxsyll + 1);
    var w = '';
    var keys = [];
    keys[randrange(nsylls)] = key;
    for (var i = 0; i < nsylls; i++) w += getMorpheme(lang, keys[i]);
    return w;
}
function getWord(lang, key) {
    key = key || '';
    var ws = lang.words[key] || [];
    var extras = 3;
    if (key) extras = 2;
    while (true) {
        var n = randrange(ws.length + extras);
        var w = ws[n];
        if (w) return w;
        w = makeWord(lang, key);
        var bad = false;
        for (var k in lang.words) {
            if (lang.words[k].includes(w)) { bad = true; break; }
        }
        if (bad) continue;
        ws.push(w);
        lang.words[key] = ws;
        return w;
    }
}
function makeName(lang, key) {
    key = key || '';
    lang.genitive = lang.genitive || getMorpheme(lang, 'of');
    lang.definite = lang.definite || getMorpheme(lang, 'the');
    while (true) {
        var name = null;
        if (Math.random() < 0.5) {
            name = capitalize(getWord(lang, key));
        } else {
            var w1 = capitalize(getWord(lang, Math.random() < 0.6 ? key : ''));
            var w2 = capitalize(getWord(lang, Math.random() < 0.6 ? key : ''));
            if (w1 == w2) continue;
            if (Math.random() > 0.5) {
                name = join([w1, w2], lang.joiner);
            } else {
                name = join([w1, lang.genitive, w2], lang.joiner);
            }
        }
        if (Math.random() < 0.1) {
            name = join([lang.definite, name], lang.joiner);
        }
        if ((name.length < lang.minchar) || (name.length > lang.maxchar)) continue;
        var used = false;
        for (var i = 0; i < lang.names.length; i++) {
            var name2 = lang.names[i];
            if ((name.indexOf(name2) != -1) || (name2.indexOf(name) != -1)) { used = true; break; }
        }
        if (used) continue;
        lang.names.push(name);
        return name;
    }
}
var defaultOrtho = {
    'ʃ': 'sh', 'ʒ': 'zh', 'ʧ': 'ch', 'ʤ': 'j',
    'ŋ': 'ng', 'j': 'y', 'x': 'kh', 'ɣ': 'gh', 'ʔ': '’',
    A: "á", E: "é", I: "í", O: "ó", U: "ú"
};
var corthsets = [
    {name:"Default", orth:{}},
    {name:"Slavic", orth:{'ʃ':'š','ʒ':'ž','ʧ':'č','ʤ':'ǧ','j':'j'}},
    {name:"German", orth:{'ʃ':'sch','ʒ':'zh','ʧ':'tsch','ʤ':'dz','j':'j','x':'ch'}},
    {name:"French", orth:{'ʃ':'ch','ʒ':'j','ʧ':'tch','ʤ':'dj','x':'kh'}},
    {name:"Chinese", orth:{'ʃ':'x','ʧ':'q','ʤ':'j'}}
];
var vorthsets = [
    {name:"Acutes", orth:{}},
    {name:"Umlauts", orth:{A:"ä",E:"ë",I:"ï",O:"ö",U:"ü"}},
    {name:"Welsh", orth:{A:"â",E:"ê",I:"y",O:"ô",U:"w"}},
    {name:"Diphthongs", orth:{A:"au",E:"ei",I:"ie",O:"ou",U:"oo"}},
    {name:"Doubles", orth:{A:"aa",E:"ee",I:"ii",O:"oo",U:"uu"}}
];
var consets = [
    {name:"Minimal",C:"ptkmnls"},
    {name:"English-ish",C:"ptkbdgmnlrsʃzʒʧ"},
    {name:"Piraha",C:"ptkmnh"},
    {name:"Hawaiian-ish",C:"hklmnpwʔ"},
    {name:"Greenlandic-ish",C:"ptkqvsgrmnŋlj"},
    {name:"Arabic-ish",C:"tksʃdb qɣxmnlrwj"},
    {name:"Arabic-lite",C:"tkdgmnsʃ"},
    {name:"English-lite",C:"ptkbdgmnszʒʧhjw"}
];
var ssets = [{name:"Just s",S:"s"},{name:"s sh",S:"sʃ"},{name:"s sh f",S:"sʃf"}];
var lsets = [{name:"r l",L:"rl"},{name:"Just r",L:"r"},{name:"Just l",L:"l"},{name:"w j",L:"wj"},{name:"r l w j",L:"rlwj"}];
var fsets = [{name:"m n",F:"mn"},{name:"s k",F:"sk"},{name:"m n ng",F:"mnŋ"},{name:"s sh z zh",F:"sʃzʒ"}];
var vowsets = [
    {name:"Standard 5",V:"aeiou"},{name:"3-vowel",V:"aiu"},{name:"Extra AEI",V:"aeiouAEI"},
    {name:"Extra U",V:"aeiouU"},{name:"5-vowel alt",V:"aiuAI"},{name:"3-vowel eou",V:"eou"},
    {name:"Extra AOU",V:"aeiouAOU"}
];
var syllstructs = ["CVC","CVV?C","CVVC?","CVC?","CV","VC","CVF","C?VC","CVF?",
    "CL?VC","CL?VF","S?CVC","S?CVF","S?CVC?","C?VF","C?VC?","C?VF?","C?L?VC","VC","CVL?C?","C?VL?C","C?VLC?"];
var ressets = [{name:"None",res:[]},{name:"Double",res:[/(.)\1/]},{name:"Hard",res:[/[sʃf][sʃ]/,/(.)\1/,/[rl][rl]/]}];

function makeBasicLanguage() {
    return {
        phonemes:{C:"ptkmnls",V:"aeiou",S:"s",F:"mn",L:"rl"},
        structure:"CVC",exponent:2,restricts:[],cortho:{},vortho:{},
        noortho:true,nomorph:true,nowordpool:true,
        minsyll:1,maxsyll:1,morphemes:{},words:{},names:[],joiner:' ',maxchar:12,minchar:5
    };
}
function makeRandomLanguage() {
    var lang = makeBasicLanguage();
    lang.noortho = false;
    lang.nomorph = false;
    lang.nowordpool = false;
    lang.phonemes.C = shuffled(choose(consets, 2).C);
    lang.phonemes.V = shuffled(choose(vowsets, 2).V);
    lang.phonemes.L = shuffled(choose(lsets, 2).L);
    lang.phonemes.S = shuffled(choose(ssets, 2).S);
    lang.phonemes.F = shuffled(choose(fsets, 2).F);
    lang.structure = choose(syllstructs);
    lang.restricts = ressets[2].res;
    lang.cortho = choose(corthsets, 2).orth;
    lang.vortho = choose(vorthsets, 2).orth;
    lang.minsyll = randrange(1, 3);
    if (lang.structure.length < 3) lang.minsyll++;
    lang.maxsyll = randrange(lang.minsyll + 1, 7);
    lang.joiner = choose('   -');
    return lang;
}

// ============================================================
// Terrain generation (from mewo2/terrain)
// ============================================================
function runif(lo, hi) { return lo + Math.random() * (hi - lo); }
var rnorm = (function () {
    var z2 = null;
    function rnorm() {
        if (z2 != null) { var tmp = z2; z2 = null; return tmp; }
        var x1=0, x2=0, w=2.0;
        while (w >= 1) { x1 = runif(-1,1); x2 = runif(-1,1); w = x1*x1 + x2*x2; }
        w = Math.sqrt(-2 * Math.log(w) / w);
        z2 = x2 * w;
        return x1 * w;
    }
    return rnorm;
})();
function randomVector(scale) { return [scale * rnorm(), scale * rnorm()]; }

var defaultExtent = {width: 1, height: 1};

function generatePoints(n, extent) {
    extent = extent || defaultExtent;
    var pts = [];
    for (var i = 0; i < n; i++) pts.push([(Math.random()-0.5)*extent.width, (Math.random()-0.5)*extent.height]);
    return pts;
}
function centroid(pts) {
    var x=0, y=0;
    for (var i = 0; i < pts.length; i++) { x += pts[i][0]; y += pts[i][1]; }
    return [x/pts.length, y/pts.length];
}
function improvePoints(pts, n, extent) {
    n = n || 1;
    extent = extent || defaultExtent;
    for (var i = 0; i < n; i++) {
        pts = voronoi(pts, extent).polygons(pts).map(centroid);
    }
    return pts;
}
function generateGoodPoints(n, extent) {
    extent = extent || defaultExtent;
    var pts = generatePoints(n, extent);
    pts = pts.sort(function(a,b){return a[0]-b[0]});
    return improvePoints(pts, 1, extent);
}
function voronoi(pts, extent) {
    extent = extent || defaultExtent;
    var w = extent.width/2, h = extent.height/2;
    return d3.voronoi().extent([[-w,-h],[w,h]])(pts);
}
function makeMesh(pts, extent) {
    extent = extent || defaultExtent;
    var vor = voronoi(pts, extent);
    var vxs = [], vxids = {}, adj = [], edges = [], tris = [];
    for (var i = 0; i < vor.edges.length; i++) {
        var e = vor.edges[i];
        if (e == undefined) continue;
        var e0 = vxids[e[0]], e1 = vxids[e[1]];
        if (e0 == undefined) { e0 = vxs.length; vxids[e[0]] = e0; vxs.push(e[0]); }
        if (e1 == undefined) { e1 = vxs.length; vxids[e[1]] = e1; vxs.push(e[1]); }
        adj[e0] = adj[e0] || []; adj[e0].push(e1);
        adj[e1] = adj[e1] || []; adj[e1].push(e0);
        edges.push([e0, e1, e.left, e.right]);
        tris[e0] = tris[e0] || [];
        if (!tris[e0].includes(e.left)) tris[e0].push(e.left);
        if (e.right && !tris[e0].includes(e.right)) tris[e0].push(e.right);
        tris[e1] = tris[e1] || [];
        if (!tris[e1].includes(e.left)) tris[e1].push(e.left);
        if (e.right && !tris[e1].includes(e.right)) tris[e1].push(e.right);
    }
    var mesh = {pts:pts, vor:vor, vxs:vxs, adj:adj, tris:tris, edges:edges, extent:extent};
    mesh.map = function(f) { var mapped = vxs.map(f); mapped.mesh = mesh; return mapped; };
    return mesh;
}
function generateGoodMesh(n, extent) {
    extent = extent || defaultExtent;
    var pts = generateGoodPoints(n, extent);
    return makeMesh(pts, extent);
}
function isedge(mesh, i) { return (mesh.adj[i].length < 3); }
function isnearedge(mesh, i) {
    var x = mesh.vxs[i][0], y = mesh.vxs[i][1];
    var w = mesh.extent.width, h = mesh.extent.height;
    return x < -0.45*w || x > 0.45*w || y < -0.45*h || y > 0.45*h;
}
function neighbours(mesh, i) {
    var onbs = mesh.adj[i], nbs = [];
    for (var i = 0; i < onbs.length; i++) nbs.push(onbs[i]);
    return nbs;
}
function distance(mesh, i, j) {
    var p = mesh.vxs[i], q = mesh.vxs[j];
    return Math.sqrt((p[0]-q[0])*(p[0]-q[0]) + (p[1]-q[1])*(p[1]-q[1]));
}
function quantile(h, q) {
    var sortedh = [];
    for (var i = 0; i < h.length; i++) sortedh[i] = h[i];
    sortedh.sort(d3.ascending);
    return d3.quantile(sortedh, q);
}
function zero(mesh) {
    var z = [];
    for (var i = 0; i < mesh.vxs.length; i++) z[i] = 0;
    z.mesh = mesh;
    return z;
}
function slope(mesh, direction) {
    return mesh.map(function(x) { return x[0]*direction[0] + x[1]*direction[1]; });
}
function cone(mesh, s) {
    return mesh.map(function(x) { return Math.pow(x[0]*x[0]+x[1]*x[1], 0.5) * s; });
}
function map(h, f) { var newh = h.map(f); newh.mesh = h.mesh; return newh; }
function normalize(h) {
    var lo = d3.min(h), hi = d3.max(h);
    return map(h, function(x){return (x-lo)/(hi-lo)});
}
function peaky(h) { return map(normalize(h), Math.sqrt); }
function add() {
    var n = arguments[0].length;
    var newvals = zero(arguments[0].mesh);
    for (var i = 0; i < n; i++) {
        for (var j = 0; j < arguments.length; j++) newvals[i] += arguments[j][i];
    }
    return newvals;
}
function mountains(mesh, n, r) {
    r = r || 0.05;
    var mounts = [];
    for (var i = 0; i < n; i++) mounts.push([mesh.extent.width*(Math.random()-0.5), mesh.extent.height*(Math.random()-0.5)]);
    var newvals = zero(mesh);
    for (var i = 0; i < mesh.vxs.length; i++) {
        var p = mesh.vxs[i];
        for (var j = 0; j < n; j++) {
            var m = mounts[j];
            newvals[i] += Math.pow(Math.exp(-((p[0]-m[0])*(p[0]-m[0])+(p[1]-m[1])*(p[1]-m[1]))/(2*r*r)), 2);
        }
    }
    return newvals;
}
function relax(h) {
    var newh = zero(h.mesh);
    for (var i = 0; i < h.length; i++) {
        var nbs = neighbours(h.mesh, i);
        if (nbs.length < 3) { newh[i] = 0; continue; }
        newh[i] = d3.mean(nbs.map(function(j){return h[j]}));
    }
    return newh;
}
function downhill(h) {
    if (h.downhill) return h.downhill;
    function downfrom(i) {
        if (isedge(h.mesh, i)) return -2;
        var best = -1, besth = h[i];
        var nbs = neighbours(h.mesh, i);
        for (var j = 0; j < nbs.length; j++) {
            if (h[nbs[j]] < besth) { besth = h[nbs[j]]; best = nbs[j]; }
        }
        return best;
    }
    var downs = [];
    for (var i = 0; i < h.length; i++) downs[i] = downfrom(i);
    h.downhill = downs;
    return downs;
}
function fillSinks(h, epsilon) {
    epsilon = epsilon || 1e-5;
    var infinity = 999999;
    var newh = zero(h.mesh);
    for (var i = 0; i < h.length; i++) {
        if (isnearedge(h.mesh, i)) newh[i] = h[i]; else newh[i] = infinity;
    }
    while (true) {
        var changed = false;
        for (var i = 0; i < h.length; i++) {
            if (newh[i] == h[i]) continue;
            var nbs = neighbours(h.mesh, i);
            for (var j = 0; j < nbs.length; j++) {
                if (h[i] >= newh[nbs[j]] + epsilon) { newh[i] = h[i]; changed = true; break; }
                var oh = newh[nbs[j]] + epsilon;
                if ((newh[i] > oh) && (oh > h[i])) { newh[i] = oh; changed = true; }
            }
        }
        if (!changed) return newh;
    }
}
function getFlux(h) {
    var dh = downhill(h);
    var idxs = [], flux = zero(h.mesh);
    for (var i = 0; i < h.length; i++) { idxs[i] = i; flux[i] = 1/h.length; }
    idxs.sort(function(a,b){return h[b]-h[a]});
    for (var i = 0; i < h.length; i++) {
        var j = idxs[i];
        if (dh[j] >= 0) flux[dh[j]] += flux[j];
    }
    return flux;
}
function trislope(h, i) {
    var nbs = neighbours(h.mesh, i);
    if (nbs.length != 3) return [0,0];
    var p0=h.mesh.vxs[nbs[0]], p1=h.mesh.vxs[nbs[1]], p2=h.mesh.vxs[nbs[2]];
    var x1=p1[0]-p0[0], x2=p2[0]-p0[0], y1=p1[1]-p0[1], y2=p2[1]-p0[1];
    var det = x1*y2 - x2*y1;
    var h1 = h[nbs[1]]-h[nbs[0]], h2 = h[nbs[2]]-h[nbs[0]];
    return [(y2*h1-y1*h2)/det, (-x2*h1+x1*h2)/det];
}
function getSlope(h) {
    var dh = downhill(h);
    var sl = zero(h.mesh);
    for (var i = 0; i < h.length; i++) {
        var s = trislope(h, i);
        sl[i] = Math.sqrt(s[0]*s[0] + s[1]*s[1]);
    }
    return sl;
}
function erosionRate(h) {
    var flux = getFlux(h), sl = getSlope(h);
    var newh = zero(h.mesh);
    for (var i = 0; i < h.length; i++) {
        var river = Math.sqrt(flux[i]) * sl[i];
        var creep = sl[i] * sl[i];
        var total = 1000*river + creep;
        if (total > 200) total = 200;
        newh[i] = total;
    }
    return newh;
}
function erode(h, amount) {
    var er = erosionRate(h);
    var newh = zero(h.mesh);
    var maxr = d3.max(er);
    for (var i = 0; i < h.length; i++) newh[i] = h[i] - amount * (er[i] / maxr);
    return newh;
}
function doErosion(h, amount, n) {
    n = n || 1;
    h = fillSinks(h);
    for (var i = 0; i < n; i++) { h = erode(h, amount); h = fillSinks(h); }
    return h;
}
function setSeaLevel(h, q) {
    var newh = zero(h.mesh);
    var delta = quantile(h, q);
    for (var i = 0; i < h.length; i++) newh[i] = h[i] - delta;
    return newh;
}
function cleanCoast(h, iters) {
    for (var iter = 0; iter < iters; iter++) {
        var changed = 0, newh = zero(h.mesh);
        for (var i = 0; i < h.length; i++) {
            newh[i] = h[i];
            var nbs = neighbours(h.mesh, i);
            if (h[i] <= 0 || nbs.length != 3) continue;
            var count = 0, best = -999999;
            for (var j = 0; j < nbs.length; j++) {
                if (h[nbs[j]] > 0) count++; else if (h[nbs[j]] > best) best = h[nbs[j]];
            }
            if (count > 1) continue;
            newh[i] = best / 2; changed++;
        }
        h = newh; newh = zero(h.mesh);
        for (var i = 0; i < h.length; i++) {
            newh[i] = h[i];
            var nbs = neighbours(h.mesh, i);
            if (h[i] > 0 || nbs.length != 3) continue;
            var count = 0, best = 999999;
            for (var j = 0; j < nbs.length; j++) {
                if (h[nbs[j]] <= 0) count++; else if (h[nbs[j]] < best) best = h[nbs[j]];
            }
            if (count > 1) continue;
            newh[i] = best / 2; changed++;
        }
        h = newh;
    }
    return h;
}
function cityScore(h, cities) {
    var score = map(getFlux(h), Math.sqrt);
    for (var i = 0; i < h.length; i++) {
        if (h[i] <= 0 || isnearedge(h.mesh, i)) { score[i] = -999999; continue; }
        score[i] += 0.01 / (1e-9 + Math.abs(h.mesh.vxs[i][0]) - h.mesh.extent.width/2);
        score[i] += 0.01 / (1e-9 + Math.abs(h.mesh.vxs[i][1]) - h.mesh.extent.height/2);
        for (var j = 0; j < cities.length; j++) {
            score[i] -= 0.02 / (distance(h.mesh, cities[j], i) + 1e-9);
        }
    }
    return score;
}
function placeCity(render) {
    render.cities = render.cities || [];
    var score = cityScore(render.h, render.cities);
    var newcity = d3.scan(score, d3.descending);
    render.cities.push(newcity);
}
function placeCities(render) {
    var n = render.params.ncities;
    for (var i = 0; i < n; i++) placeCity(render);
}
function contour(h, level) {
    level = level || 0;
    var edges = [];
    for (var i = 0; i < h.mesh.edges.length; i++) {
        var e = h.mesh.edges[i];
        if (e[3] == undefined) continue;
        if (isnearedge(h.mesh, e[0]) || isnearedge(h.mesh, e[1])) continue;
        if ((h[e[0]] > level && h[e[1]] <= level) || (h[e[1]] > level && h[e[0]] <= level)) {
            edges.push([e[2], e[3]]);
        }
    }
    return mergeSegments(edges);
}
function getRivers(h, limit) {
    var dh = downhill(h), flux = getFlux(h);
    var links = [], above = 0;
    for (var i = 0; i < h.length; i++) { if (h[i] > 0) above++; }
    limit *= above / h.length;
    for (var i = 0; i < dh.length; i++) {
        if (isnearedge(h.mesh, i)) continue;
        if (flux[i] > limit && h[i] > 0 && dh[i] >= 0) {
            var up = h.mesh.vxs[i], down = h.mesh.vxs[dh[i]];
            if (h[dh[i]] > 0) links.push([up, down]);
            else links.push([up, [(up[0]+down[0])/2, (up[1]+down[1])/2]]);
        }
    }
    return mergeSegments(links).map(relaxPath);
}
function getTerritories(render) {
    var h = render.h, cities = render.cities;
    var n = render.params.nterrs;
    if (n > render.cities.length) n = render.cities.length;
    var flux = getFlux(h);
    var terr = [];
    var queue = new PriorityQueue({comparator: function(a,b){return a.score-b.score}});
    function weight(u, v) {
        var horiz = distance(h.mesh, u, v);
        var vert = h[v] - h[u];
        if (vert > 0) vert /= 10;
        var diff = 1 + 0.25 * Math.pow(vert/horiz, 2);
        diff += 100 * Math.sqrt(flux[u]);
        if (h[u] <= 0) diff = 100;
        if ((h[u] > 0) != (h[v] > 0)) return 1000;
        return horiz * diff;
    }
    for (var i = 0; i < n; i++) {
        terr[cities[i]] = cities[i];
        var nbs = neighbours(h.mesh, cities[i]);
        for (var j = 0; j < nbs.length; j++) {
            queue.queue({score: weight(cities[i], nbs[j]), city: cities[i], vx: nbs[j]});
        }
    }
    while (queue.length) {
        var u = queue.dequeue();
        if (terr[u.vx] != undefined) continue;
        terr[u.vx] = u.city;
        var nbs = neighbours(h.mesh, u.vx);
        for (var i = 0; i < nbs.length; i++) {
            var v = nbs[i];
            if (terr[v] != undefined) continue;
            queue.queue({score: u.score + weight(u.vx, v), city: u.city, vx: v});
        }
    }
    terr.mesh = h.mesh;
    return terr;
}
function getBorders(render) {
    var terr = render.terr, h = render.h;
    var edges = [];
    for (var i = 0; i < terr.mesh.edges.length; i++) {
        var e = terr.mesh.edges[i];
        if (e[3] == undefined) continue;
        if (isnearedge(terr.mesh, e[0]) || isnearedge(terr.mesh, e[1])) continue;
        if (h[e[0]] < 0 || h[e[1]] < 0) continue;
        if (terr[e[0]] != terr[e[1]]) edges.push([e[2], e[3]]);
    }
    return mergeSegments(edges).map(relaxPath);
}
function mergeSegments(segs) {
    var adj = {};
    for (var i = 0; i < segs.length; i++) {
        var seg = segs[i];
        var a0 = adj[seg[0]] || [], a1 = adj[seg[1]] || [];
        a0.push(seg[1]); a1.push(seg[0]);
        adj[seg[0]] = a0; adj[seg[1]] = a1;
    }
    var done = [], paths = [], path = null;
    while (true) {
        if (path == null) {
            for (var i = 0; i < segs.length; i++) {
                if (done[i]) continue;
                done[i] = true;
                path = [segs[i][0], segs[i][1]];
                break;
            }
            if (path == null) break;
        }
        var changed = false;
        for (var i = 0; i < segs.length; i++) {
            if (done[i]) continue;
            if (adj[path[0]].length == 2 && segs[i][0] == path[0]) { path.unshift(segs[i][1]); }
            else if (adj[path[0]].length == 2 && segs[i][1] == path[0]) { path.unshift(segs[i][0]); }
            else if (adj[path[path.length-1]].length == 2 && segs[i][0] == path[path.length-1]) { path.push(segs[i][1]); }
            else if (adj[path[path.length-1]].length == 2 && segs[i][1] == path[path.length-1]) { path.push(segs[i][0]); }
            else continue;
            done[i] = true; changed = true; break;
        }
        if (!changed) { paths.push(path); path = null; }
    }
    return paths;
}
function relaxPath(path) {
    var newpath = [path[0]];
    for (var i = 1; i < path.length - 1; i++) {
        newpath.push([0.25*path[i-1][0]+0.5*path[i][0]+0.25*path[i+1][0],
                      0.25*path[i-1][1]+0.5*path[i][1]+0.25*path[i+1][1]]);
    }
    newpath.push(path[path.length - 1]);
    return newpath;
}
function dropEdge(h, p) {
    p = p || 4;
    var newh = zero(h.mesh);
    for (var i = 0; i < h.length; i++) {
        var v = h.mesh.vxs[i];
        var x = 2.4*v[0]/h.mesh.extent.width, y = 2.4*v[1]/h.mesh.extent.height;
        newh[i] = h[i] - Math.exp(10*(Math.pow(Math.pow(x,p)+Math.pow(y,p),1/p)-1));
    }
    return newh;
}
function generateCoast(params) {
    var mesh = generateGoodMesh(params.npts, params.extent);
    var h = add(slope(mesh, randomVector(4)), cone(mesh, runif(-1,-1)), mountains(mesh, params.mountainCount || 50, params.mountainRadius || 0.05));
    for (var i = 0; i < 10; i++) h = relax(h);
    h = peaky(h);
    h = doErosion(h, runif(0,0.1), 5);
    h = setSeaLevel(h, runif(0.2, 0.6));
    h = fillSinks(h);
    h = cleanCoast(h, 3);
    return h;
}
function terrCenter(h, terr, city, landOnly) {
    var x=0, y=0, n=0;
    for (var i = 0; i < terr.length; i++) {
        if (terr[i] != city) continue;
        if (landOnly && h[i] <= 0) continue;
        x += terr.mesh.vxs[i][0]; y += terr.mesh.vxs[i][1]; n++;
    }
    return [x/n, y/n];
}

// ============================================================
// Visualization functions
// ============================================================
function makeD3Path(path) {
    var p = d3.path();
    p.moveTo(1000*path[0][0], 1000*path[0][1]);
    for (var i = 1; i < path.length; i++) p.lineTo(1000*path[i][0], 1000*path[i][1]);
    return p.toString();
}
function visualizeVoronoi(svg, field, lo, hi) {
    if (hi == undefined) hi = d3.max(field) + 1e-9;
    if (lo == undefined) lo = d3.min(field) - 1e-9;
    var mappedvals = field.map(function(x){return x > hi ? 1 : x < lo ? 0 : (x-lo)/(hi-lo)});
    var tris = svg.selectAll('path.field').data(field.mesh.tris);
    tris.enter().append('path').classed('field', true);
    tris.exit().remove();
    svg.selectAll('path.field')
        .attr('d', makeD3Path)
        .style('fill', function(d,i){return d3.interpolateViridis(mappedvals[i])});
}
function drawPaths(svg, cls, paths) {
    var p = svg.selectAll('path.' + cls).data(paths);
    p.enter().append('path').classed(cls, true);
    p.exit().remove();
    svg.selectAll('path.' + cls).attr('d', makeD3Path);
}
function visualizeSlopes(svg, render) {
    var h = render.h;
    var strokes = [];
    var r = 0.25 / Math.sqrt(h.length);
    for (var i = 0; i < h.length; i++) {
        if (h[i] <= 0 || isnearedge(h.mesh, i)) continue;
        var nbs = neighbours(h.mesh, i);
        nbs.push(i);
        var s = 0, s2 = 0;
        for (var j = 0; j < nbs.length; j++) {
            var slopes = trislope(h, nbs[j]);
            s += slopes[0] / 10; s2 += slopes[1];
        }
        s /= nbs.length; s2 /= nbs.length;
        if (Math.abs(s) < runif(0.1, 0.4)) continue;
        var l = r * runif(1, 2) * (1 - 0.2 * Math.pow(Math.atan(s), 2)) * Math.exp(s2/100);
        var x = h.mesh.vxs[i][0], y = h.mesh.vxs[i][1];
        if (Math.abs(l*s) > 2*r) {
            var n = Math.floor(Math.abs(l*s/r));
            l /= n; if (n > 4) n = 4;
            for (var j = 0; j < n; j++) {
                var u = rnorm()*r, v = rnorm()*r;
                strokes.push([[x+u-l, y+v+l*s], [x+u+l, y+v-l*s]]);
            }
        } else {
            strokes.push([[x-l, y+l*s], [x+l, y-l*s]]);
        }
    }
    var lines = svg.selectAll('line.slope').data(strokes);
    lines.enter().append('line').classed('slope', true);
    lines.exit().remove();
    svg.selectAll('line.slope')
        .attr('x1', function(d){return 1000*d[0][0]})
        .attr('y1', function(d){return 1000*d[0][1]})
        .attr('x2', function(d){return 1000*d[1][0]})
        .attr('y2', function(d){return 1000*d[1][1]});
}
function visualizeCities(svg, render) {
    var cities = render.cities, h = render.h;
    var n = render.params.nterrs;
    var circs = svg.selectAll('circle.city').data(cities);
    circs.enter().append('circle').classed('city', true);
    circs.exit().remove();
    svg.selectAll('circle.city')
        .attr('cx', function(d){return 1000*h.mesh.vxs[d][0]})
        .attr('cy', function(d){return 1000*h.mesh.vxs[d][1]})
        .attr('r', function(d,i){return i >= n ? 4 : 10})
        .style('fill', 'white')
        .style('stroke-width', 5)
        .style('stroke-linecap', 'round')
        .style('stroke', 'black')
        .raise();
}
function drawLabels(svg, render) {
    var params = render.params;
    var h = render.h;
    var terr = render.terr;
    var cities = render.cities;
    var nterrs = render.params.nterrs;
    var avoids = [render.rivers, render.coasts, render.borders];
    var lang = makeRandomLanguage();
    var citylabels = [];
    function penalty(label) {
        var pen = 0;
        if (label.x0 < -0.45*h.mesh.extent.width) pen += 100;
        if (label.x1 > 0.45*h.mesh.extent.width) pen += 100;
        if (label.y0 < -0.45*h.mesh.extent.height) pen += 100;
        if (label.y1 > 0.45*h.mesh.extent.height) pen += 100;
        for (var i = 0; i < citylabels.length; i++) {
            var olabel = citylabels[i];
            if (label.x0 < olabel.x1 && label.x1 > olabel.x0 && label.y0 < olabel.y1 && label.y1 > olabel.y0) pen += 100;
        }
        for (var i = 0; i < cities.length; i++) {
            var c = h.mesh.vxs[cities[i]];
            if (label.x0 < c[0] && label.x1 > c[0] && label.y0 < c[1] && label.y1 > c[1]) pen += 100;
        }
        for (var i = 0; i < avoids.length; i++) {
            var avoid = avoids[i];
            for (var j = 0; j < avoid.length; j++) {
                var avpath = avoid[j];
                for (var k = 0; k < avpath.length; k++) {
                    var pt = avpath[k];
                    if (pt[0] > label.x0 && pt[0] < label.x1 && pt[1] > label.y0 && pt[1] < label.y1) pen++;
                }
            }
        }
        return pen;
    }
    for (var i = 0; i < cities.length; i++) {
        var x = h.mesh.vxs[cities[i]][0], y = h.mesh.vxs[cities[i]][1];
        var text = makeName(lang, 'city');
        var size = i < nterrs ? params.fontsizes.city : params.fontsizes.town;
        var sx = 0.65*size/1000*text.length, sy = size/1000;
        var posslabels = [
            {x:x+0.8*sy, y:y+0.3*sy, align:'start', x0:x+0.7*sy, y0:y-0.6*sy, x1:x+0.7*sy+sx, y1:y+0.6*sy},
            {x:x-0.8*sy, y:y+0.3*sy, align:'end', x0:x-0.9*sy-sx, y0:y-0.7*sy, x1:x-0.9*sy, y1:y+0.7*sy},
            {x:x, y:y-0.8*sy, align:'middle', x0:x-sx/2, y0:y-1.9*sy, x1:x+sx/2, y1:y-0.7*sy},
            {x:x, y:y+1.2*sy, align:'middle', x0:x-sx/2, y0:y+0.1*sy, x1:x+sx/2, y1:y+1.3*sy}
        ];
        var label = posslabels[d3.scan(posslabels, function(a,b){return penalty(a)-penalty(b)})];
        label.text = text; label.size = size;
        citylabels.push(label);
    }
    var texts = svg.selectAll('text.city').data(citylabels);
    texts.enter().append('text').classed('city', true);
    texts.exit().remove();
    svg.selectAll('text.city')
        .attr('x', function(d){return 1000*d.x})
        .attr('y', function(d){return 1000*d.y})
        .style('font-size', function(d){return d.size})
        .style('text-anchor', function(d){return d.align})
        .text(function(d){return d.text}).raise();
    var reglabels = [];
    for (var i = 0; i < nterrs; i++) {
        var city = cities[i];
        var text = makeName(lang, 'region');
        var sy = params.fontsizes.region / 1000;
        var sx = 0.6 * text.length * sy;
        var lc = terrCenter(h, terr, city, true);
        var oc = terrCenter(h, terr, city, false);
        var best = 0, bestscore = -999999;
        for (var j = 0; j < h.length; j++) {
            var score = 0;
            var v = h.mesh.vxs[j];
            score -= 3000*Math.sqrt((v[0]-lc[0])*(v[0]-lc[0])+(v[1]-lc[1])*(v[1]-lc[1]));
            score -= 1000*Math.sqrt((v[0]-oc[0])*(v[0]-oc[0])+(v[1]-oc[1])*(v[1]-oc[1]));
            if (terr[j] != city) score -= 3000;
            for (var k = 0; k < cities.length; k++) {
                var u = h.mesh.vxs[cities[k]];
                if (Math.abs(v[0]-u[0]) < sx && Math.abs(v[1]-sy/2-u[1]) < sy) score -= k < nterrs ? 4000 : 500;
                if (v[0]-sx/2 < citylabels[k].x1 && v[0]+sx/2 > citylabels[k].x0 && v[1]-sy < citylabels[k].y1 && v[1] > citylabels[k].y0) score -= 5000;
            }
            for (var k = 0; k < reglabels.length; k++) {
                var rl = reglabels[k];
                if (v[0]-sx/2 < rl.x+rl.width/2 && v[0]+sx/2 > rl.x-rl.width/2 && v[1]-sy < rl.y && v[1] > rl.y-rl.size) score -= 20000;
            }
            if (h[j] <= 0) score -= 500;
            if (v[0]+sx/2 > 0.5*h.mesh.extent.width) score -= 50000;
            if (v[0]-sx/2 < -0.5*h.mesh.extent.width) score -= 50000;
            if (v[1] > 0.5*h.mesh.extent.height) score -= 50000;
            if (v[1]-sy < -0.5*h.mesh.extent.height) score -= 50000;
            if (score > bestscore) { bestscore = score; best = j; }
        }
        reglabels.push({text:text, x:h.mesh.vxs[best][0], y:h.mesh.vxs[best][1], size:sy, width:sx});
    }
    texts = svg.selectAll('text.region').data(reglabels);
    texts.enter().append('text').classed('region', true);
    texts.exit().remove();
    svg.selectAll('text.region')
        .attr('x', function(d){return 1000*d.x})
        .attr('y', function(d){return 1000*d.y})
        .style('font-size', function(d){return 1000*d.size})
        .style('text-anchor', 'middle')
        .text(function(d){return d.text}).raise();
}
function drawMap(svg, render) {
    render.rivers = getRivers(render.h, 0.01);
    render.coasts = contour(render.h, 0);
    render.terr = getTerritories(render);
    render.borders = getBorders(render);
    drawPaths(svg, 'river', render.rivers);
    drawPaths(svg, 'coast', render.coasts);
    drawPaths(svg, 'border', render.borders);
    visualizeSlopes(svg, render);
    visualizeCities(svg, render);
    drawLabels(svg, render);
}

// ============================================================
// Interactive demo state
// ============================================================
var meshPts = 4096;
var sharedMesh = null;

function ensureMesh() {
    if (!sharedMesh) sharedMesh = generateGoodMesh(meshPts);
    return sharedMesh;
}

// --- Section 1: Random Points ---
function doRandomPoints() {
    sharedMesh = null;
    var pts = generateGoodPoints(meshPts);
    var svg = d3.select('#svg-points');
    svg.selectAll('*').remove();
    var circle = svg.selectAll('circle').data(pts);
    circle.enter().append('circle')
        .attr('cx', function(d){return 1000*d[0]})
        .attr('cy', function(d){return 1000*d[1]})
        .attr('r', 100/Math.sqrt(pts.length))
        .style('fill', '#333');
    sharedMesh = makeMesh(pts);
}

// --- Section 2: Voronoi ---
function doShowVoronoi() {
    var mesh = ensureMesh();
    var svg = d3.select('#svg-voronoi');
    svg.selectAll('*').remove();
    var vor = mesh.vor;
    // Draw Voronoi edges
    for (var i = 0; i < vor.edges.length; i++) {
        var e = vor.edges[i];
        if (!e) continue;
        svg.append('line')
            .attr('x1', 1000*e[0][0]).attr('y1', 1000*e[0][1])
            .attr('x2', 1000*e[1][0]).attr('y2', 1000*e[1][1])
            .style('stroke', '#aaa').style('stroke-width', 0.5);
    }
    // Draw points
    var circle = svg.selectAll('circle').data(mesh.pts);
    circle.enter().append('circle')
        .attr('cx', function(d){return 1000*d[0]})
        .attr('cy', function(d){return 1000*d[1]})
        .attr('r', 2)
        .style('fill', '#c33');
}

// --- Section 3: Height Map ---
var hmHeight = null;
function ensureHeight() {
    var mesh = ensureMesh();
    if (!hmHeight || hmHeight.mesh !== mesh) {
        hmHeight = zero(mesh);
    }
    return hmHeight;
}
function redrawHeightmap() {
    var svg = d3.select('#svg-heightmap');
    svg.selectAll('*').remove();
    visualizeVoronoi(svg, hmHeight);
    var coasts = contour(hmHeight, 0);
    drawPaths(svg, 'coast', coasts);
}
function doAddSlope() {
    hmHeight = add(ensureHeight(), slope(ensureMesh(), randomVector(4)));
    redrawHeightmap();
}
function doAddCone() {
    hmHeight = add(ensureHeight(), cone(ensureMesh(), -0.5));
    redrawHeightmap();
}
function doAddInvCone() {
    hmHeight = add(ensureHeight(), cone(ensureMesh(), 0.5));
    redrawHeightmap();
}
function doAddBlobs() {
    hmHeight = add(ensureHeight(), mountains(ensureMesh(), 5));
    redrawHeightmap();
}
function doNormalize() {
    hmHeight = normalize(ensureHeight());
    redrawHeightmap();
}
function doRound() {
    hmHeight = peaky(ensureHeight());
    redrawHeightmap();
}
function doRelax() {
    hmHeight = relax(ensureHeight());
    redrawHeightmap();
}
function doSetSea() {
    hmHeight = setSeaLevel(ensureHeight(), 0.5);
    redrawHeightmap();
}
function resetHeightmap() {
    hmHeight = zero(ensureMesh());
    redrawHeightmap();
}

// --- Section 4: Erosion ---
var erHeight = null;
function doGenCoast() {
    var params = {npts: meshPts, extent: defaultExtent};
    erHeight = generateCoast(params);
    sharedMesh = erHeight.mesh;
    var svg = d3.select('#svg-erosion');
    svg.selectAll('*').remove();
    visualizeVoronoi(svg, erHeight);
    drawPaths(svg, 'coast', contour(erHeight, 0));
}
function doErode() {
    if (!erHeight) { doGenCoast(); return; }
    erHeight = doErosion(erHeight, 0.1, 5);
    erHeight = setSeaLevel(erHeight, 0.5);
    erHeight = fillSinks(erHeight);
    erHeight = cleanCoast(erHeight, 3);
    var svg = d3.select('#svg-erosion');
    svg.selectAll('*').remove();
    visualizeVoronoi(svg, erHeight);
    drawPaths(svg, 'coast', contour(erHeight, 0));
}
function doCleanCoast() {
    if (!erHeight) return;
    erHeight = cleanCoast(erHeight, 3);
    var svg = d3.select('#svg-erosion');
    svg.selectAll('*').remove();
    visualizeVoronoi(svg, erHeight);
    drawPaths(svg, 'coast', contour(erHeight, 0));
}

// --- Section 5: Rendering features ---
var renderH = null;
var showCoast = true, showRivers = true, showSlopes = true;
function ensureRenderH() {
    if (!renderH) {
        if (erHeight) { renderH = erHeight; }
        else {
            var params = {npts: meshPts, extent: defaultExtent};
            renderH = generateCoast(params);
        }
    }
    return renderH;
}
function redrawRender() {
    var h = ensureRenderH();
    var svg = d3.select('#svg-render');
    svg.selectAll('*').remove();
    visualizeVoronoi(svg, h);
    if (showCoast) drawPaths(svg, 'coast', contour(h, 0));
    if (showRivers) drawPaths(svg, 'river', getRivers(h, 0.01));
    if (showSlopes) {
        var render = {h: h, params: {nterrs: 5}};
        visualizeSlopes(svg, render);
    }
}
function toggleCoast() {
    showCoast = !showCoast;
    redrawRender();
}
function toggleRivers() {
    showRivers = !showRivers;
    redrawRender();
}
function toggleSlopes() {
    showSlopes = !showSlopes;
    redrawRender();
}

// --- Section 6: Cities ---
var cityRender = null;
function ensureCityRender() {
    if (!cityRender) {
        var h = ensureRenderH();
        cityRender = {h: h, cities: [], params: {ncities: 15, nterrs: 5, fontsizes:{region:40,city:25,town:20}}};
    }
    return cityRender;
}
function redrawCities() {
    var r = ensureCityRender();
    var svg = d3.select('#svg-cities');
    svg.selectAll('*').remove();
    visualizeVoronoi(svg, r.h);
    drawPaths(svg, 'coast', contour(r.h, 0));
    drawPaths(svg, 'river', getRivers(r.h, 0.01));
    visualizeCities(svg, r);
}
function doAddCity() {
    var r = ensureCityRender();
    placeCity(r);
    redrawCities();
}
function resetCities() {
    if (cityRender) cityRender.cities = [];
    redrawCities();
}

// --- Section 7: Territories ---
function doShowTerritories() {
    var r = ensureCityRender();
    while (r.cities.length < r.params.nterrs) {
        placeCity(r);
    }
    r.terr = getTerritories(r);
    r.borders = getBorders(r);
    var svg = d3.select('#svg-territories');
    svg.selectAll('*').remove();
    // color territories
    var h = r.h;
    var terr = r.terr;
    var colors = d3.schemeCategory10;
    var cityColor = {};
    for (var i = 0; i < r.cities.length; i++) {
        cityColor[r.cities[i]] = colors[i % colors.length];
    }
    var tris = svg.selectAll('path.field').data(h.mesh.tris);
    tris.enter().append('path').classed('field', true);
    svg.selectAll('path.field')
        .attr('d', makeD3Path)
        .style('fill', function(d,i){
            if (h[i] <= 0) return '#a5bfdd';
            if (terr[i] != undefined) return cityColor[terr[i]] || '#ddd';
            return '#ddd';
        })
        .style('opacity', 0.5);
    drawPaths(svg, 'coast', contour(h, 0));
    drawPaths(svg, 'border', r.borders);
    visualizeCities(svg, r);
}

// --- Section 8: Full Map ---
function doFullMap() {
    var overlay = document.getElementById('loading-overlay');
    overlay.style.display = 'flex';
    setTimeout(function() {
        var svg = d3.select('#svg-fullmap');
        var params = {
            extent: defaultExtent,
            generator: generateCoast,
            npts: 16384,
            ncities: 15,
            nterrs: 5,
            fontsizes: {region: 40, city: 25, town: 20}
        };
        svg.selectAll('*').remove();
        var render = {params: params};
        render.h = params.generator(params);
        placeCities(render);
        drawMap(svg, render);
        overlay.style.display = 'none';
    }, 50);
}

function doExportSVG() {
    var svgEl = document.getElementById('svg-fullmap');
    if (!svgEl.firstChild) {
        alert('Generate a map first!');
        return;
    }
    var serializer = new XMLSerializer();
    var source = serializer.serializeToString(svgEl);
    // Add XML declaration and namespace
    if (!source.match(/^<\?xml/)) {
        source = '<?xml version="1.0" standalone="no"?>\r\n' + source;
    }
    if (!source.match(/xmlns/)) {
        source = source.replace('<svg', '<svg xmlns="http://www.w3.org/2000/svg"');
    }
    // Add styles inline
    var styleBlock = '<defs><style type="text/css"><![CDATA[\n' +
        'path.coast { stroke: #333; stroke-width: 3; fill: none; stroke-linecap: round; stroke-linejoin: round; }\n' +
        'path.river { stroke: #36a; stroke-width: 2; fill: none; stroke-linecap: round; stroke-linejoin: round; }\n' +
        'path.border { stroke: #a33; stroke-width: 2.5; fill: none; stroke-dasharray: 6,6; stroke-linecap: round; stroke-linejoin: round; }\n' +
        'line.slope { stroke: #797; stroke-width: 1; stroke-linecap: round; }\n' +
        "text.city { font-family: 'Palatino Linotype', Palatino, Georgia, serif; fill: #333; }\n" +
        "text.region { font-family: 'Palatino Linotype', Palatino, Georgia, serif; fill: rgba(80,50,50,0.6); text-transform: uppercase; letter-spacing: 0.1em; font-style: italic; }\n" +
        ']]></style></defs>';
    source = source.replace('>', '>' + styleBlock);
    var blob = new Blob([source], {type: 'image/svg+xml;charset=utf-8'});
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = 'fantasy-map.svg';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}
