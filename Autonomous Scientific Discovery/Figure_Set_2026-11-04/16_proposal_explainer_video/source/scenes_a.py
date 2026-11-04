"""Scenes 1-7. Each: css, html, js. JS sees tl, C (cue start times), END, IN, NUM, GROW."""
INK, NAVY, SLATE, MIST, PALE, RED, GOLD = "#1F2A36", "#2E4057", "#546A86", "#8A9BB0", "#DCE2EA", "#B23A3A", "#8A6A2F"

A = {}

A["s01"] = dict(css="""
#s01-k{left:150px;top:250px;font:700 30px "HFSans";letter-spacing:8px;color:#8A6A2F;}
#s01-t1{left:150px;top:310px;font:900 104px/1.15 "HFSerif";}
#s01-t2{left:150px;top:440px;font:900 104px/1.15 "HFSerif";color:#2E4057;}
#s01-rule{left:150px;top:600px;width:900px;height:4px;background:#1F2A36;}
#s01-en{left:150px;top:630px;font:400 30px "HFSans";color:#546A86;}
#s01-by{left:150px;top:680px;font:400 28px "HFSans";color:#546A86;}
#s01-q{left:150px;top:800px;font:700 48px "HFSerif";color:#B23A3A;}
""", html="""
<div id="s01-k" class="abs">研究提案解读</div>
<div id="s01-t1" class="abs">从可计算任务到开放科学</div>
<div id="s01-t2" class="abs">人工智能解题编年史</div>
<div id="s01-rule" class="abs"></div>
<div id="s01-en" class="abs">From Computable Tasks to Open Science: A Chronicle of AI Problem Solving</div>
<div id="s01-by" class="abs">Zhe Zhao · 2026 年 9 月</div>
<div id="s01-q" class="abs">AI 究竟真正解决了哪些科学问题？</div>
""", js="""
 IN("#s01-t2",C[1]+0.8,40); GROW("#s01-rule",C[1]+1.6,1.2);
IN("#s01-en",C[1]+2.4); IN("#s01-by",C[1]+2.8); IN("#s01-q",C[2]+2.5);
""")

A["s02"] = dict(css="""
#root .row{left:150px;width:1620px;height:170px;}
#root .lab{position:absolute;left:0;top:0;font:900 50px "HFSerif";}
#root .sub{position:absolute;left:0;top:76px;font:400 30px "HFSans";color:#546A86;}
#root .bar{position:absolute;left:760px;top:40px;width:860px;height:22px;background:#2E4057;}
#root .tick{position:absolute;top:62px;width:2px;height:18px;background:#2E4057;}
#root .x{position:absolute;left:760px;top:92px;font:700 30px "HFSans";color:#B23A3A;}
#s02-r1{top:290px;} #s02-r2{top:480px;}
#s02-n{left:150px;top:690px;font:900 150px/1 "HFSerif";color:#2E4057;}
#s02-nl{left:150px;top:860px;font:400 30px "HFSans";color:#546A86;}
#s02-p{left:1000px;top:690px;font:900 150px/1 "HFSerif";color:#B23A3A;}
#s02-pl{left:1000px;top:860px;font:400 30px "HFSans";color:#546A86;}
""", html="""
<div class="tag" id="s02-tag">01 · 背景</div>
<div class="h" id="s02-h">评判 AI 进展的两把尺子，都不可靠</div>
<div class="abs row" id="s02-r1"><div class="lab">尺子一 · 发布</div><div class="sub">发布会 · 预印本摘要 · 演示</div>
  <div class="bar" id="s02-b1"></div><div class="x" id="s02-x1">✕ 分不清“偶然成功一次”与“被独立复现”</div></div>
<div class="abs row" id="s02-r2"><div class="lab">尺子二 · 基准分数</div><div class="sub">代理指标，而非结果本身</div>
  <div class="bar" id="s02-b2"></div><div class="x" id="s02-x2">✕ 效度本身正受到质疑</div></div>
<div id="s02-n" class="abs">0</div><div id="s02-nl" class="abs">个大模型基准被审查，几乎每一个都至少有一处缺陷</div>
<div id="s02-p" class="abs">0%</div><div id="s02-pl" class="abs">使用了不确定性估计或统计检验 · arXiv 2511.04703</div>
""", js="""
IN("#s02-tag",0.2); IN("#s02-h",0.4);
IN("#s02-r1",C[1]); GROW("#s02-b1",C[1]+0.4); IN("#s02-x1",C[2]+1);
IN("#s02-r2",C[3]); GROW("#s02-b2",C[3]+0.4); IN("#s02-x2",C[4]+1.5);
IN("#s02-n",C[4]+4); NUM("#s02-n",445,C[4]+4,1.4); IN("#s02-nl",C[4]+4.5);
IN("#s02-p",C[4]+10); NUM("#s02-p",16,C[4]+10,1,"%"); IN("#s02-pl",C[4]+10.4);
""")

A["s03"] = dict(css="""
#s03-bar{left:150px;top:330px;width:1620px;height:30px;background:#B23A3A;}
#s03-bl{left:150px;top:380px;font:900 46px "HFSerif";color:#B23A3A;}
#root .q{left:150px;font:900 62px "HFSerif";}
#root .q b{display:inline-block;width:110px;color:#8A9BB0;font-family:"HFSerif";}
#s03-q1{top:500px;} #s03-q2{top:600px;} #s03-q3{top:700px;}
#s03-cost{left:150px;top:850px;font:400 32px "HFSans";color:#546A86;}
""", html="""
<div class="tag" id="s03-tag">01 · 背景</div>
<div class="h" id="s03-h">第三把尺子：真正被解决了的科学问题</div>
<div id="s03-bar" class="abs"></div>
<div id="s03-bl" class="abs">不问发布了什么，不问榜单第几</div>
<div id="s03-q1" class="abs q"><b>①</b>解决的是哪一个具体问题？</div>
<div id="s03-q2" class="abs q"><b>②</b>解决到了什么程度？</div>
<div id="s03-q3" class="abs q"><b>③</b>依据的是什么证据？</div>
<div id="s03-cost" class="abs">代价：每个案例都须人工核查，无法从排行榜汇总</div>
""", js="""
IN("#s03-tag",0.2); IN("#s03-h",0.4); GROW("#s03-bar",1.2,1.2); IN("#s03-bl",2.4);
IN("#s03-q1",C[1]+2.2); IN("#s03-q2",C[2]); IN("#s03-q3",C[3]); IN("#s03-cost",C[4]);
""")

A["s04"] = dict(css="""
#s04-chips{left:150px;top:300px;width:1620px;}
#root .chip{display:inline-block;margin:0 18px 18px 0;padding:14px 26px;border:3px solid #546A86;font:700 30px "HFSans";color:#2E4057;}
#s04-ax1{left:150px;top:480px;font:900 44px "HFSerif";color:#2E4057;}
#s04-ax2{left:960px;top:480px;font:900 44px "HFSerif";color:#B23A3A;}
#s04-empty{left:960px;top:550px;width:810px;height:96px;border:3px dashed #B23A3A;}
#s04-e0{left:990px;top:574px;font:700 34px "HFSans";color:#B23A3A;}
#s04-full{left:150px;top:550px;width:740px;height:96px;background:#546A86;}
#s04-f0{left:180px;top:574px;font:700 34px "HFSans";color:#F4F1EA;}
#s04-a{left:150px;top:740px;font:700 40px "HFSans";}
#s04-eq{left:880px;top:724px;font:900 70px "HFSerif";color:#B23A3A;}
#s04-b{left:1000px;top:740px;font:700 40px "HFSans";}
#s04-note{left:150px;top:830px;font:400 30px "HFSans";color:#546A86;}
""", html="""
<div class="tag" id="s04-tag">01 · 背景</div>
<div class="h" id="s04-h">前置问题：什么才算“解决”？</div>
<div id="s04-chips" class="abs"><span class="chip">自动驾驶实验室 L1–L5</span><span class="chip">智能体自主等级</span><span class="chip">发现系统能力分层</span><span class="chip">……至少六套</span></div>
<div id="s04-ax1" class="abs">它们都在评：系统有多自主</div>
<div id="s04-full" class="abs"></div><div id="s04-f0" class="abs">已有 6+ 套分类体系</div>
<div id="s04-ax2" class="abs">没人评：问题解决到什么程度</div>
<div id="s04-empty" class="abs"></div><div id="s04-e0" class="abs">0 套</div>
<div id="s04-a" class="abs">“在基准上超越人类”</div><div id="s04-eq" class="abs">≟</div>
<div id="s04-b" class="abs">“前所未知的结构 + 独立复现”</div>
<div id="s04-note" class="abs">同一个“解决”，装不进同一张表</div>
""", js="""
IN("#s04-tag",0.2); IN("#s04-h",0.4);
IN("#s04-chips",C[1]+0.5); IN("#s04-ax1",C[1]+4); GROW("#s04-full",C[1]+4.6); IN("#s04-f0",C[1]+5.2);
IN("#s04-ax2",C[1]+7); IN("#s04-empty",C[1]+7.6); IN("#s04-e0",C[1]+8.2);
IN("#s04-a",C[2]+1); IN("#s04-b",C[2]+3.5); IN("#s04-eq",C[2]+5.5); IN("#s04-note",C[2]+7);
""")

A["s05"] = dict(css="""
#s05-yax{left:340px;top:250px;width:4px;height:600px;background:#1F2A36;}
#s05-xax{left:340px;top:846px;width:1000px;height:4px;background:#1F2A36;}
#root .ol{left:90px;width:230px;white-space:nowrap;text-align:right;font:700 30px "HFSans";color:#2E4057;}
#root .vl{top:868px;width:200px;margin-left:-100px;text-align:center;font:700 30px "HFSans";color:#2E4057;}
#s05-yt{left:150px;top:200px;font:900 36px "HFSerif";}
#s05-xt{left:1360px;top:830px;font:900 36px "HFSerif";}
#s05-desc{left:1100px;top:250px;width:680px;font:400 30px/1.6 "HFSans";color:#546A86;}
#s05-auto{left:1100px;top:520px;width:680px;padding:22px 28px;border:3px solid #8A9BB0;font:700 30px/1.5 "HFSans";color:#8A9BB0;}
#s05-dot{left:924px;top:384px;width:32px;height:32px;border-radius:50%;background:#B23A3A;}
#s05-gx{left:938px;top:416px;width:4px;height:430px;border-left:3px dashed #B23A3A;}
#s05-gy{left:344px;top:398px;width:580px;height:4px;border-top:3px dashed #B23A3A;}
#s05-dl{left:720px;top:320px;font:900 40px "HFSerif";color:#B23A3A;}
""", html="""
<div class="tag" id="s05-tag">02 · 意义</div>
<div id="s05-yt" class="abs">问题开放度</div>
<div id="s05-yax" class="abs"></div><div id="s05-xax" class="abs"></div>
<div class="abs ol" id="s05-o1" style="top:780px">O1 规则世界</div>
<div class="abs ol" id="s05-o2" style="top:680px">O2 既定基准</div>
<div class="abs ol" id="s05-o3" style="top:580px">O3 新实例</div>
<div class="abs ol" id="s05-o4" style="top:480px">O4 需物理检验</div>
<div class="abs ol" id="s05-o5" style="top:380px">O5 开放数学</div>
<div class="abs ol" id="s05-o6" style="top:280px">O6 开放科学</div>
<div id="s05-xt" class="abs">验证强度</div>
<div class="abs vl" id="s05-v0" style="left:440px">V0 声明</div>
<div class="abs vl" id="s05-v1" style="left:640px">V1</div>
<div class="abs vl" id="s05-v2" style="left:790px">V2</div>
<div class="abs vl" id="s05-v3" style="left:940px">V3</div>
<div class="abs vl" id="s05-v4" style="left:1140px">V4 证明/复现</div>
<div id="s05-desc" class="abs">开放度：从问题陈述读出<br>验证强度：形式化证明、物理实验<br>或第三方复现，才算强验证</div>
<div id="s05-auto" class="abs">第三条轴 · 系统自主性 L0–L3<br>保留，但不再代替“解决程度”</div>
<div id="s05-gx" class="abs"></div><div id="s05-gy" class="abs"></div>
<div id="s05-dot" class="abs"></div><div id="s05-dl" class="abs">(V3, O5)</div>
""", js="""
IN("#s05-tag",0.2);
tl.fromTo("#s05-yax",{scaleY:0,transformOrigin:"center bottom"},{scaleY:1,duration:1,ease:"power3.inOut"},C[1]);
IN("#s05-yt",C[1]+0.5); ["o1","o2","o3","o4","o5","o6"].forEach((k,i)=>IN("#s05-"+k,C[1]+2.5+i*1.2,0));
GROW("#s05-xax",C[2]); IN("#s05-xt",C[2]+0.6); ["v0","v1","v2","v3","v4"].forEach((k,i)=>IN("#s05-"+k,C[2]+2+i*1.1,0));
IN("#s05-desc",C[2]+5); IN("#s05-auto",C[3]);
tl.fromTo("#s05-gx",{scaleY:0,transformOrigin:"center bottom"},{scaleY:1,duration:0.6},C[4]);
GROW("#s05-gy",C[4]); tl.fromTo("#s05-dot",{scale:0},{scale:1,duration:0.5,ease:"back.out(3)"},C[4]+0.7); IN("#s05-dl",C[4]+1);
""")

A["s06"] = dict(css="""
#root .bl{left:150px;font:900 48px "HFSerif";}
#root .track{left:520px;width:1100px;height:84px;background:#DCE2EA;}
#root .fill{position:absolute;left:0;top:0;height:84px;background:#2E4057;}
#root .val{left:520px;font:700 32px "HFSans";color:#546A86;}
#root .pct{left:1650px;font:900 60px "HFSerif";}
#s06-l3{top:380px;} #s06-t3{top:370px;} #s06-v3{top:470px;} #s06-p3{top:380px;color:#B23A3A;}
#s06-l1{top:600px;} #s06-t1{top:590px;} #s06-v1{top:690px;} #s06-p1{top:600px;color:#2E4057;}
#s06-ll{left:150px;top:300px;font:400 28px "HFSans";color:#546A86;}
#s06-big{left:150px;top:820px;font:900 56px "HFSerif";color:#B23A3A;}
""", html="""
<div class="tag" id="s06-tag">发现一</div>
<div class="h" id="s06-h">自主性与验证强度，方向相反</div>
<div id="s06-ll" class="abs">达到强验证（V3–V4）的案例占比</div>
<div class="abs bl" id="s06-l3">L3 最自主</div>
<div class="abs track" id="s06-t3"><div class="fill" id="s06-f3" style="width:0"></div></div>
<div class="abs val" id="s06-v3">12 个案例中 0 个</div><div class="abs pct" id="s06-p3">0%</div>
<div class="abs bl" id="s06-l1">L1</div>
<div class="abs track" id="s06-t1"><div class="fill" id="s06-f1" style="width:451px"></div></div>
<div class="abs val" id="s06-v1">59 个案例中 24 个</div><div class="abs pct" id="s06-p1">41%</div>
<div id="s06-big" class="abs">越自主 → 越少被独立验证</div>
""", js="""
IN("#s06-tag",0.2); IN("#s06-h",C[1]);
IN("#s06-ll",C[2]); IN("#s06-l3",C[2]+1); IN("#s06-t3",C[2]+1); IN("#s06-v3",C[2]+3); IN("#s06-p3",C[2]+4.2);
IN("#s06-l1",C[2]+5.5); IN("#s06-t1",C[2]+5.5); GROW("#s06-f1",C[2]+7,1.2); IN("#s06-v1",C[2]+7.5); IN("#s06-p1",C[2]+8.4);
IN("#s06-big",C[3]+0.5);
""")

A["s07"] = dict(css="""
#root .wb{bottom:400px;width:110px;background:#8A9BB0;}
#root .wn{width:110px;text-align:center;font:900 44px "HFSerif";}
#s07-axis{left:150px;top:680px;width:760px;height:4px;background:#1F2A36;}
#s07-wl{left:150px;top:700px;font:400 28px "HFSans";color:#546A86;}
#s07-sl{left:1060px;top:300px;font:400 28px "HFSans";color:#546A86;}
#s07-s1{left:1060px;top:350px;font:900 110px/1 "HFSerif";color:#2E4057;}
#s07-s1l{left:1060px;top:470px;font:400 28px "HFSans";color:#546A86;}
#s07-arr{left:1330px;top:380px;font:900 70px "HFSerif";color:#8A9BB0;}
#s07-s2{left:1450px;top:350px;font:900 110px/1 "HFSerif";color:#B23A3A;}
#s07-s2l{left:1450px;top:470px;font:400 28px "HFSans";color:#546A86;}
#s07-stack{left:150px;top:820px;width:1620px;height:64px;}
#root .seg{position:absolute;top:0;height:64px;color:#F4F1EA;font:700 28px/64px "HFSans";padding-left:14px;box-sizing:border-box;white-space:nowrap;}
#s07-keep{left:150px;top:900px;font:400 28px "HFSans";color:#546A86;}
""", html="""
<div class="tag" id="s07-tag">发现二</div>
<div class="h" id="s07-h">证据正在随时间变薄</div>
<div class="abs wb" id="s07-b0" style="left:190px;height:4px"></div>
<div class="abs wb" id="s07-b1" style="left:370px;height:12px"></div>
<div class="abs wb" id="s07-b2" style="left:550px;height:48px"></div>
<div class="abs wb" id="s07-b3" style="left:730px;height:156px;background:#B23A3A"></div>
<div class="abs wn" id="s07-n0" style="left:190px;top:610px">0</div>
<div class="abs wn" id="s07-n1" style="left:370px;top:600px">1</div>
<div class="abs wn" id="s07-n2" style="left:550px;top:564px">4</div>
<div class="abs wn" id="s07-n3" style="left:730px;top:456px;color:#B23A3A">13</div>
<div id="s07-axis" class="abs"></div><div id="s07-wl" class="abs">弱验证（V0–V1）案例数 · 按时代，早 → 近</div>
<div id="s07-sl" class="abs">强验证（V3–V4）占比</div>
<div id="s07-s1" class="abs">5/7</div><div id="s07-s1l" class="abs">最早时代</div>
<div id="s07-arr" class="abs">→</div>
<div id="s07-s2" class="abs">12/41</div><div id="s07-s2l" class="abs">2024–2026 · 案例最多</div>
<div id="s07-stack" class="abs">
  <div class="seg" id="s07-g0" style="left:0;width:1215px;background:#2E4057">已验证 63</div>
  <div class="seg" id="s07-g1" style="left:1215px;width:193px;background:#8A9BB0">声明 10</div>
  <div class="seg" id="s07-g2" style="left:1408px;width:193px;background:#B23A3A">争议 10</div>
  <div class="seg" id="s07-g3" style="left:1601px;width:19px;background:#1F2A36"></div>
</div>
<div id="s07-keep" class="abs">全部 84 个案例 · 被推翻 1 · 争议与被推翻的案例全部保留</div>
""", js="""
IN("#s07-tag",0.2); IN("#s07-h",0.4);
GROW("#s07-axis",C[1]); IN("#s07-wl",C[1]+0.4);
["0","1","2","3"].forEach((k,i)=>{ tl.fromTo("#s07-b"+k,{scaleY:0,transformOrigin:"center bottom"},{scaleY:1,duration:0.6,ease:"power3.out"},C[1]+3.6+i*0.9); IN("#s07-n"+k,C[1]+3.9+i*0.9,0); });
IN("#s07-sl",C[1]+7.5); IN("#s07-s1",C[1]+8.5); IN("#s07-s1l",C[1]+8.5); IN("#s07-arr",C[1]+9.6,0); IN("#s07-s2",C[1]+10); IN("#s07-s2l",C[2]+3);
["0","1","2","3"].forEach((k,i)=>IN("#s07-g"+k,C[3]+1+i*1.6,0)); IN("#s07-keep",C[4]);
""")
