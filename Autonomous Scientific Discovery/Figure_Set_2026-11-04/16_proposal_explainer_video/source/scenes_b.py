"""Scenes 8-14."""
B = {}

B["s08"] = dict(css="""
#root .it{left:150px;width:1620px;height:130px;border-top:3px solid #1F2A36;}
#root .it .n{position:absolute;left:0;top:18px;font:900 76px/1 "HFSerif";color:#8A6A2F;}
#root .it .t{position:absolute;left:150px;top:18px;font:900 46px "HFSerif";}
#root .it .d{position:absolute;left:150px;top:80px;font:400 28px "HFSans";color:#546A86;}
#s08-i1{top:290px;} #s08-i2{top:440px;} #s08-i3{top:590px;} #s08-i4{top:740px;}
""", html="""
<div class="tag" id="s08-tag">02 · 意义</div>
<div class="h" id="s08-h">拆开之后，能做到的四件事</div>
<div class="abs it" id="s08-i1"><div class="n">1</div><div class="t">可检验的前沿曲线</div><div class="d">任何案例复核达不到 V3，边界就后退——可证伪</div></div>
<div class="abs it" id="s08-i2"><div class="n">2</div><div class="t">被定位的空白</div><div class="d">“该领域在 O6 尚无强验证案例”，可以直接读出</div></div>
<div class="abs it" id="s08-i3"><div class="n">3</div><div class="t">可计算的速率</div><div class="d">每个时代推进几级 · 哪些领域最快 · 哪些二十年未动</div></div>
<div class="abs it" id="s08-i4"><div class="n">4</div><div class="t">可复查的记录</div><div class="d">每个层级判定至少附一个独立来源，缺失即标记</div></div>
""", js="""
IN("#s08-tag",0.2); IN("#s08-h",0.4);
IN("#s08-i1",C[1]); IN("#s08-i2",C[2]); IN("#s08-i3",C[3]); IN("#s08-i4",C[4]);
""")

# fig1.png is 3140x1360; shown at width 1820 (scale 0.5796) -> 788 tall, inside a clipped viewport
B["s09"] = dict(css="""
#s09-vp{left:50px;top:150px;width:1820px;height:788px;overflow:hidden;}
#s09-cam{position:absolute;left:0;top:0;width:1820px;height:788px;}
#s09-img{position:absolute;left:0;top:0;width:1820px;height:788px;}
#root .hl{position:absolute;border:5px solid #B23A3A;}
#s09-hx{left:0;top:665px;width:1820px;height:60px;}
#s09-hy{left:0;top:180px;width:200px;height:400px;}
#s09-ht{left:300px;top:85px;width:1520px;height:50px;}
#s09-cap{left:150px;top:70px;font:900 46px "HFSerif";}
""", html="""
<div id="s09-cap" class="abs">主图 · AI 已解决问题的前沿版图</div>
<div id="s09-vp" class="abs" data-layout-allow-overflow>
  <div id="s09-cam">
    <img id="s09-img" src="assets/fig1.png" alt="The expanding frontier of AI-solved problems">
    <div class="hl" id="s09-hx"></div><div class="hl" id="s09-hy"></div><div class="hl" id="s09-ht"></div>
  </div>
</div>
""", js="""
IN("#s09-cap",0.2); tl.fromTo("#s09-vp",{opacity:0},{opacity:1,duration:1.2,ease:"power2.out"},0.4);
const HL=(s,a,b)=>{tl.fromTo(s,{opacity:0},{opacity:1,duration:0.3},a); tl.to(s,{opacity:0,duration:0.3},b);};
const CAM=(sc,x0,y0,t,d)=>tl.to("#s09-cam",{scale:sc,x:-x0*sc,y:-y0*sc,transformOrigin:"0px 0px",duration:d,ease:"power2.inOut"},t);
HL("#s09-hx",C[1]+0.3,C[1]+2.2); HL("#s09-hy",C[1]+2.3,C[2]);
CAM(1.6,380,120,C[2]+0.5,1.6);
CAM(1,0,0,C[3],1.0);
CAM(2.2,280,40,C[4],1.8);
tl.fromTo("#s09-ht",{opacity:0},{opacity:1,duration:0.4},C[4]+1.8);
tl.to("#s09-cam",{x:-993*2.2,duration:8.2,ease:"none"},C[4]+3);
CAM(1,0,0,END-2.6,1.4);
""")

B["s10"] = dict(css="""
#root .big{top:300px;font:900 150px/1 "HFSerif";}
#root .bl{top:470px;font:700 32px "HFSans";color:#546A86;}
#s10-a{left:150px;color:#546A86;} #s10-al{left:150px;}
#s10-b{left:720px;color:#2E4057;} #s10-bl{left:720px;}
#s10-c{left:1230px;color:#B23A3A;} #s10-cl{left:1230px;}
#root .ar{top:330px;font:900 80px "HFSerif";color:#546A86;}
#s10-src{left:150px;top:590px;width:1620px;font:400 30px/1.7 "HFSans";color:#1F2A36;}
#s10-f{left:150px;top:780px;width:1620px;font:700 30px/1.8 "HFSans";color:#2E4057;}
""", html="""
<div class="tag" id="s10-tag">03 · 已完成</div>
<div class="h" id="s10-h">调研的基础工作已经完成</div>
<div class="abs big" id="s10-a">0</div><div class="abs bl" id="s10-al">条记录</div>
<div class="abs ar" id="s10-r1" style="left:560px">→</div>
<div class="abs big" id="s10-b">0</div><div class="abs bl" id="s10-bl">个案例完成三轴编码</div>
<div class="abs ar" id="s10-r2" style="left:1070px">→</div>
<div class="abs big" id="s10-c">0</div><div class="abs bl" id="s10-cl">个领域</div>
<div id="s10-src" class="abs">来源：陶哲轩 · AI 对埃尔德什问题的贡献表（至 2026.6）<br>Wu, Fu, Cong &amp; Wang · Awesome-Agentic-Labs　·　1956–2026 里程碑合集</div>
<div id="s10-f" class="abs">博弈 · 感知与语言 · 计算与算法 · 数学 · 物理与天文 · 地球与气候 · 化学 · 材料 · 生物与蛋白质 · 医学 · 工程与控制 · 科研过程本身</div>
""", js="""
IN("#s10-tag",0.2); IN("#s10-h",0.4);
IN("#s10-a",C[0]+5); NUM("#s10-a",974,C[0]+5,1.6); IN("#s10-al",C[0]+5.4); IN("#s10-src",C[0]+7.5);
IN("#s10-r1",C[1],0); IN("#s10-b",C[1]+0.3); NUM("#s10-b",84,C[1]+0.3); IN("#s10-bl",C[1]+0.6);
IN("#s10-r2",C[1]+4,0); IN("#s10-c",C[1]+4.3); NUM("#s10-c",12,C[1]+4.3,0.8); IN("#s10-cl",C[1]+4.6); IN("#s10-f",C[1]+5);
""")

B["s11"] = dict(css="""
#root .ax{left:150px;width:1000px;height:70px;font:700 36px/70px "HFSans";}
#root .ax span{display:inline-block;width:240px;font-family:"HFSerif";font-weight:900;}
#root .ok{color:#2E4057;} #root .no{color:#B23A3A;}
#s11-a1{top:290px;} #s11-a2{top:370px;} #s11-a3{top:450px;}
#s11-jt{left:150px;top:580px;font:900 40px "HFSerif";}
#root .j{width:390px;height:190px;top:650px;border-left:6px solid #B23A3A;padding-left:22px;box-sizing:border-box;font:700 32px/1.4 "HFSans";}
#root .j i{display:block;font-style:normal;font:400 28px/1.45 "HFSans";color:#546A86;margin-top:6px;}
#s11-j1{left:150px;} #s11-j2{left:560px;} #s11-j3{left:970px;} #s11-j4{left:1380px;}
#s11-need{left:150px;top:870px;font:900 40px "HFSerif";color:#B23A3A;}
""", html="""
<div class="tag" id="s11-tag">03 · 瓶颈</div>
<div class="h" id="s11-h">下一步，不是更多的检索</div>
<div class="abs ax ok" id="s11-a1"><span>开放度</span>← 问题陈述 ✓</div>
<div class="abs ax ok" id="s11-a2"><span>自主性</span>← 方法描述 ✓</div>
<div class="abs ax no" id="s11-a3"><span>验证强度</span>← 文献检索 ✕　须读原始证据</div>
<div id="s11-jt" class="abs">四项判断构成瓶颈</div>
<div class="abs j" id="s11-j1">V3 / V2 边界<i>复现是否第三方？实验是否覆盖核心主张？</i></div>
<div class="abs j" id="s11-j2">AI 的实际贡献<i>产出核心结果，还是在人给的候选中挑选？</i></div>
<div class="abs j" id="s11-j3">O6 空白是否真实<i>确实没有，还是没收集到？</i></div>
<div class="abs j" id="s11-j4">争议案例裁定<i>争议 10 · 推翻 1，需要判断而非计数</i></div>
<div id="s11-need" class="abs">→ 需要领域内的研究者</div>
""", js="""
IN("#s11-tag",0.2); IN("#s11-h",0.4);
IN("#s11-a1",C[1]+1.5); IN("#s11-a2",C[1]+4.5); IN("#s11-a3",C[1]+7);
IN("#s11-jt",C[2]); IN("#s11-j1",C[2]+2); IN("#s11-j2",C[2]+4); IN("#s11-j3",C[2]+6); IN("#s11-j4",C[2]+8); IN("#s11-need",C[3]);
""")

B["s12"] = dict(css="""
#root .k{top:300px;width:520px;}
#root .k b{display:block;font:900 110px/1.1 "HFSerif";color:#2E4057;}
#root .k span{display:block;font:700 32px "HFSans";color:#546A86;margin-top:10px;}
#s12-k1{left:150px;} #s12-k2{left:700px;} #s12-k3{left:1250px;}
#s12-q{left:150px;top:560px;width:1620px;font:400 32px/1.6 "HFSans";}
#s12-from{left:150px;top:760px;font:900 54px "HFSerif";color:#8A9BB0;}
#s12-strike{left:150px;top:796px;width:330px;height:5px;background:#B23A3A;}
#s12-arr{left:540px;top:752px;font:900 60px "HFSerif";color:#1F2A36;}
#s12-to{left:660px;top:760px;font:900 54px "HFSerif";color:#B23A3A;}
""", html="""
<div class="tag" id="s12-tag">04 · 请求</div>
<div class="h" id="s12-h">请求：每个领域一位研究者</div>
<div class="abs k" id="s12-k1"><b>1 位</b><span>研究者 / 每个领域</span></div>
<div class="abs k" id="s12-k2"><b>15–20</b><span>个案例</span></div>
<div class="abs k" id="s12-k3"><b>½ 天</b><span>每人大约半天</span></div>
<div id="s12-q" class="abs">判定验证等级与 AI 的实际贡献，并回答：本领域在 O6 层级，是否存在强验证案例？</div>
<div id="s12-from" class="abs">文献汇编</div><div id="s12-strike" class="abs"></div>
<div id="s12-arr" class="abs">→</div>
<div id="s12-to" class="abs">可以被引用的判断</div>
""", js="""
IN("#s12-tag",0.2); IN("#s12-h",0.4);
IN("#s12-k1",C[0]+4); IN("#s12-k2",C[0]+7); IN("#s12-q",C[0]+9); IN("#s12-k3",C[1]);
IN("#s12-from",C[2]+1); GROW("#s12-strike",C[2]+3.5,0.5); IN("#s12-arr",C[2]+4.5,0); IN("#s12-to",C[2]+5);
""")

B["s13"] = dict(css="""
#s13-line{left:150px;top:400px;width:1620px;height:6px;background:#1F2A36;}
#root .st{top:360px;width:520px;}
#root .st .dot{width:46px;height:46px;border-radius:50%;background:#B23A3A;margin-top:20px;}
#root .st .m{font:700 28px "HFSans";color:#8A6A2F;margin-top:30px;}
#root .st .t{font:900 50px "HFSerif";margin-top:6px;}
#root .st .d{font:400 28px/1.6 "HFSans";color:#546A86;margin-top:14px;width:480px;}
#s13-p1{left:150px;} #s13-p2{left:700px;} #s13-p3{left:1250px;}
""", html="""
<div class="tag" id="s13-tag">05 · 计划</div>
<div class="h" id="s13-h">三个月：AI 筛选 → 专家审阅 → 形成词典</div>
<div id="s13-line" class="abs"></div>
<div class="abs st" id="s13-p1"><div class="dot"></div><div class="m">第 0–1 月</div><div class="t">AI 筛选</div><div class="d">扫描全部记录，扩展至 200+ 候选；<br>先报告漏检率与抽取错误率</div></div>
<div class="abs st" id="s13-p2"><div class="dot"></div><div class="m">第 1–2 月</div><div class="t">专家审阅</div><div class="d">报告机器与专家的一致率；<br>逐案归因分歧，暴露系统偏差</div></div>
<div class="abs st" id="s13-p3"><div class="dot"></div><div class="m">第 2–3 月</div><div class="t">问题词典</div><div class="d">按领域 · 开放度 · 验证强度检索；<br>前沿曲线可由案例表重算</div></div>
""", js="""
IN("#s13-tag",0.2); IN("#s13-h",0.4); GROW("#s13-line",C[0]+1,1.4);
IN("#s13-p1",C[1]); IN("#s13-p2",C[2]); IN("#s13-p3",C[3]);
""")

B["s14"] = dict(css="""
#root .no{left:150px;font:900 70px "HFSerif";color:#8A9BB0;}
#s14-n1{top:300px;} #s14-n2{top:400px;}
#root .sk{left:150px;height:6px;background:#B23A3A;}
#s14-k1{top:345px;width:290px;} #s14-k2{top:445px;width:290px;}
#s14-y{left:150px;top:560px;font:900 80px/1.3 "HFSerif";color:#1F2A36;}
#s14-t{left:150px;top:800px;font:700 32px "HFSans";color:#546A86;}
#s14-th{left:150px;top:880px;font:900 44px "HFSerif";color:#B23A3A;}
""", html="""
<div id="s14-n1" class="abs no">不看发布</div><div id="s14-k1" class="abs sk"></div>
<div id="s14-n2" class="abs no">不看榜单</div><div id="s14-k2" class="abs sk"></div>
<div id="s14-y" class="abs">只看：解决到了哪里<br>凭什么证据</div>
<div id="s14-t" class="abs">从可计算任务到开放科学 · 人工智能解题编年史</div>
<div id="s14-th" class="abs">感谢收看</div>
""", js="""
IN("#s14-n1",0.3); GROW("#s14-k1",1.2,0.5); IN("#s14-n2",1.4); GROW("#s14-k2",2.3,0.5);
IN("#s14-y",2.8); IN("#s14-t",4.5); IN("#s14-th",C[2]);
""")
