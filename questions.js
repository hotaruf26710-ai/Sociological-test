const SOCIUS_QUESTIONS = [
  {"id":"q01","unit":"第一篇章：结构的基石 (Unit 1: Substrate of Order)","unit_desc":"社会运作的底层逻辑是什么？谁设计了这套隐形的规则？","scenario":"感知世界：独自行走在大城市的深夜，那种“秩序感”让你觉得：","options":[
    {"label":"A","text":"是一种无形的默契，大家虽不相识却共同守护着安宁。","effects":{"scale":0.8,"force":0.4,"order":-0.8,"stance":-0.6}},
    {"label":"B","text":"是一种压抑的平衡，背后的资源争夺从未停止。","effects":{"scale":0.9,"force":-0.8,"order":0.8,"stance":0.8}},
    {"label":"C","text":"是一种迷人的疏离，每个人都是彼此世界里的路人。","effects":{"scale":-0.8,"force":0.6,"order":-0.1,"stance":-0.5}},
    {"label":"D","text":"是一套高效的程序，路灯和监控在精确地维持运转。","effects":{"scale":0.7,"force":-0.4,"order":-0.5,"stance":-0.3}}
  ]},
  {"id":"q02","unit":"第一篇章：结构的基石 (Unit 1: Substrate of Order)","unit_desc":"社会运作的底层逻辑是什么？谁设计了这套隐形的规则？","scenario":"步入机构：面对一家规章制度极其死板的机构，你的第一反应是：","options":[
    {"label":"A","text":"挺好的，这能给每个人提供明确的安全感和位置。","effects":{"scale":0.7,"force":0.3,"order":-0.7,"stance":-0.5}},
    {"label":"B","text":"很难受，这套规则显然是为了更方便地榨取我的精力。","effects":{"scale":0.8,"force":-0.7,"order":0.7,"stance":0.7}},
    {"label":"C","text":"无所谓，只要我能在这个缝隙里保持自己的独立就行。","effects":{"scale":-0.7,"force":0.5,"order":0.1,"stance":-0.4}},
    {"label":"D","text":"很好奇，这套非人情的逻辑是如何被设计出来的。","effects":{"scale":0.5,"force":0.6,"order":0.4,"stance":-0.8}}
  ]},
  {"id":"q03","unit":"第一篇章：结构的基石 (Unit 1: Substrate of Order)","unit_desc":"社会运作的底层逻辑是什么？谁设计了这套隐形的规则？","scenario":"极端设想：如果整个社会突然陷入没有规则的真空状态，你最恐惧的是：","options":[
    {"label":"A","text":"失去归属感，像断了线的风筝一样在荒野中游荡。","effects":{"scale":0.8,"force":0.7,"order":-0.9,"stance":-0.6}},
    {"label":"B","text":"失去反抗的目标，最终被更原始的暴力所吞噬。","effects":{"scale":0.9,"force":-0.8,"order":0.9,"stance":0.8}},
    {"label":"C","text":"失去社交的趣味，一切独特的个人魅力都变得毫无意义。","effects":{"scale":-0.9,"force":0.8,"order":-0.2,"stance":-0.5}},
    {"label":"D","text":"失去效率，所有的现代便利瞬间崩塌成废墟。","effects":{"scale":0.8,"force":-0.5,"order":-0.6,"stance":-0.2}}
  ]},
  {"id":"q04","unit":"第一篇章：结构的基石 (Unit 1: Substrate of Order)","unit_desc":"社会运作的底层逻辑是什么？谁设计了这套隐形的规则？","scenario":"教育反思：关于学校这门必修课，你认为它最真实的底色是：","options":[
    {"label":"A","text":"它教会我们如何成为社会这台机器里的一颗合格螺丝。","effects":{"scale":0.9,"force":0.4,"order":-0.8,"stance":-0.5}},
    {"label":"B","text":"它是一道隐形的墙，用来筛选谁能留下、谁该离开。","effects":{"scale":0.8,"force":0.6,"order":0.8,"stance":0.7}},
    {"label":"C","text":"它是一个巨大的舞台，让我们学习如何体面地与人周旋。","effects":{"scale":-0.7,"force":0.7,"order":0.0,"stance":-0.4}},
    {"label":"D","text":"它是一座工厂，将知识像零件一样安装进我们的脑中。","effects":{"scale":0.7,"force":-0.4,"order":-0.5,"stance":-0.2}}
  ]},
  {"id":"q05","unit":"第一篇章：结构的基石 (Unit 1: Substrate of Order)","unit_desc":"社会运作的底层逻辑是什么？谁设计了这套隐形的规则？","scenario":"集体归属：你参与集体活动的初衷，通常是因为：","options":[
    {"label":"A","text":"渴望融入某种伟大的共鸣，寻找超越个体的神圣感。","effects":{"scale":0.8,"force":0.9,"order":-0.8,"stance":-0.7}},
    {"label":"B","text":"意识到单打独斗没有出路，必须和同类站在一起。","effects":{"scale":0.7,"force":-0.8,"order":0.8,"stance":0.7}},
    {"label":"C","text":"享受这种与人产生连接、却又不必深交的轻盈感。","effects":{"scale":-0.9,"force":0.7,"order":-0.1,"stance":-0.4}},
    {"label":"D","text":"纯粹是为了完成任务或交换所需的资源。","effects":{"scale":0.5,"force":-0.6,"order":-0.2,"stance":-0.5}}
  ]},
  {"id":"q06","unit":"第二篇章：权力的幽灵 (Unit 2: Phantom of Power)","unit_desc":"权力如何在日常生活中无处不在地运作——而我们对此浑然不觉？","scenario":"门槛直觉：看到顶级会所的入会门槛，你内心的真实潜台词是：","options":[
    {"label":"A","text":"他们在筛选某种共同的品味和家庭教养。","effects":{"scale":0.5,"force":0.9,"order":0.7,"stance":0.6}},
    {"label":"B","text":"这是一种心理暗示，在训练我们对权力的敬畏。","effects":{"scale":-0.4,"force":0.8,"order":0.9,"stance":0.9}},
    {"label":"C","text":"这就是金钱铸造的围栏，简单且粗暴。","effects":{"scale":0.9,"force":-1.0,"order":0.9,"stance":0.8}},
    {"label":"D","text":"这只是为了维持一个特定环境的运营策略。","effects":{"scale":0.4,"force":-0.2,"order":-0.2,"stance":-0.7}}
  ]},
  {"id":"q07","unit":"第二篇章：权力的幽灵 (Unit 2: Phantom of Power)","unit_desc":"权力如何在日常生活中无处不在地运作——而我们对此浑然不觉？","scenario":"职场规范：关于那些约定俗成的职场礼仪或穿搭，你认为：","options":[
    {"label":"A","text":"这是一张入场券，用来证明你属于这个圈子。","effects":{"scale":0.6,"force":0.9,"order":0.8,"stance":0.7}},
    {"label":"B","text":"这是一套软性的枷锁，在悄悄修正你的身体和言行。","effects":{"scale":-0.5,"force":0.7,"order":0.9,"stance":0.9}},
    {"label":"C","text":"这种形式主义，实质上是管理层对员工的服从性测试。","effects":{"scale":0.8,"force":-0.7,"order":0.9,"stance":0.8}},
    {"label":"D","text":"挺有意思的，它反映了某种特定文化下的互动逻辑。","effects":{"scale":-0.6,"force":0.6,"order":0.1,"stance":-0.8}}
  ]},
  {"id":"q08","unit":"第二篇章：权力的幽灵 (Unit 2: Phantom of Power)","unit_desc":"权力如何在日常生活中无处不在地运作——而我们对此浑然不觉？","scenario":"审美变迁：当你发现某个小众品味突然变得大众化时，你会：","options":[
    {"label":"A","text":"感到这种品味已经贬值，因为它失去了阶层区隔的作用。","effects":{"scale":0.6,"force":1.0,"order":0.9,"stance":0.7}},
    {"label":"B","text":"觉得这是大众被某种主流审美话语集体俘获了。","effects":{"scale":0.8,"force":0.9,"order":0.9,"stance":1.0}},
    {"label":"C","text":"意识到这只是资本为了创造新需求而进行的新一轮割草。","effects":{"scale":0.9,"force":-0.8,"order":0.9,"stance":0.8}},
    {"label":"D","text":"只是单纯觉得风潮变了，对此保持中立的观察。","effects":{"scale":-0.5,"force":0.3,"order":-0.3,"stance":-0.9}}
  ]},
  {"id":"q09","unit":"第二篇章：权力的幽灵 (Unit 2: Phantom of Power)","unit_desc":"权力如何在日常生活中无处不在地运作——而我们对此浑然不觉？","scenario":"权威认知：你如何看待所谓的权威专家？","options":[
    {"label":"A","text":"他们掌握着定义什么是正确的最高级文化资本。","effects":{"scale":0.7,"force":0.9,"order":0.8,"stance":0.7}},
    {"label":"B","text":"他们是权力网络中的节点，负责通过知识来施行管理。","effects":{"scale":0.7,"force":0.8,"order":1.0,"stance":0.9}},
    {"label":"C","text":"他们往往是利益集团的代言人，在巩固现有的不平等。","effects":{"scale":0.8,"force":-0.7,"order":0.9,"stance":0.8}},
    {"label":"D","text":"他们是专业领域的领航员，虽然有时也会犯错。","effects":{"scale":0.5,"force":0.2,"order":-0.4,"stance":-0.9}}
  ]},
  {"id":"q10","unit":"第二篇章：权力的幽灵 (Unit 2: Phantom of Power)","unit_desc":"权力如何在日常生活中无处不在地运作——而我们对此浑然不觉？","scenario":"社会痛点：你认为这个世界最让你感到不公的地方在于：","options":[
    {"label":"A","text":"哪怕你再努力，也难以习得那种从小熏陶出的气质。","effects":{"scale":0.5,"force":1.0,"order":0.9,"stance":0.8}},
    {"label":"B","text":"你的一举一动都被无形的规则注视着，且你已习惯了它。","effects":{"scale":-0.6,"force":0.8,"order":0.9,"stance":0.9}},
    {"label":"C","text":"绝大多数的财富和机会都被极少数人牢牢攥在手里。","effects":{"scale":0.9,"force":-0.9,"order":1.0,"stance":0.8}},
    {"label":"D","text":"很多时候我们无法看清真相，只能在迷雾中摸索。","effects":{"scale":-0.4,"force":0.4,"order":0.3,"stance":-1.0}}
  ]},
  {"id":"q11","unit":"第三篇章：意义的剧场 (Unit 3: Theater of Meaning)","unit_desc":"我们在社会中扮演什么角色？意义、仪式与互动如何构造我们的世界？","scenario":"社交面貌：在社交场合表现出一个精致的自我，这让你感到：","options":[
    {"label":"A","text":"理所当然，社交本质上就是一场需要演技的舞台剧。","effects":{"scale":-1.0,"force":0.7,"order":-0.4,"stance":-0.9}},
    {"label":"B","text":"有点疲惫，因为我很难找到这背后的真实意义。","effects":{"scale":-0.5,"force":0.8,"order":0.6,"stance":-0.9}},
    {"label":"C","text":"很有必要，这种职业面具是对私生活的保护。","effects":{"scale":-0.8,"force":0.6,"order":-0.1,"stance":-0.6}},
    {"label":"D","text":"感到异化，觉得那个社交中的人根本不是我。","effects":{"scale":0.8,"force":-0.8,"order":0.9,"stance":0.9}}
  ]},
  {"id":"q12","unit":"第三篇章：意义的剧场 (Unit 3: Theater of Meaning)","unit_desc":"我们在社会中扮演什么角色？意义、仪式与互动如何构造我们的世界？","scenario":"驱动来源：你追求一份事业的动力，更多来自于：","options":[
    {"label":"A","text":"享受在那个特定领域里被大家认可的角色光环。","effects":{"scale":-0.8,"force":0.8,"order":-0.3,"stance":-0.8}},
    {"label":"B","text":"响应内心的某种感召，哪怕它看起来并不划算。","effects":{"scale":-0.6,"force":1.0,"order":0.5,"stance":-0.9}},
    {"label":"C","text":"这种互动中带给我的独特体验和个体成就感。","effects":{"scale":-0.9,"force":0.7,"order":0.1,"stance":-0.6}},
    {"label":"D","text":"获得更好的物质保障，改变自己的生活处境。","effects":{"scale":0.8,"force":-1.0,"order":0.8,"stance":0.9}}
  ]},
  {"id":"q13","unit":"第三篇章：意义的剧场 (Unit 3: Theater of Meaning)","unit_desc":"我们在社会中扮演什么角色？意义、仪式与互动如何构造我们的世界？","scenario":"网红打卡：面对网红景点排长队的现象，你的第一反应是：","options":[
    {"label":"A","text":"大家都在参与一场集体仪式，为了拍出一张符合人设的照片。","effects":{"scale":-0.9,"force":0.8,"order":-0.2,"stance":-0.7}},
    {"label":"B","text":"在这个干枯的世界里，人们在疯狂寻找某种神圣的错觉。","effects":{"scale":-0.4,"force":0.9,"order":0.6,"stance":-0.8}},
    {"label":"C","text":"典型的都市时尚流变，人们在追求瞬间的视觉刺激。","effects":{"scale":-0.8,"force":0.7,"order":0.1,"stance":-0.5}},
    {"label":"D","text":"一场精心策划的消费陷阱，充满了虚假的狂欢。","effects":{"scale":0.8,"force":-0.7,"order":0.9,"stance":1.0}}
  ]},
  {"id":"q14","unit":"第三篇章：意义的剧场 (Unit 3: Theater of Meaning)","unit_desc":"我们在社会中扮演什么角色？意义、仪式与互动如何构造我们的世界？","scenario":"互动尴尬：当你与重要人物如领导独处感到尴尬时，你的内心在：","options":[
    {"label":"A","text":"疯狂搜索合适的剧本，试图管理好对方对我的印象。","effects":{"scale":-1.0,"force":0.6,"order":-0.4,"stance":-0.9}},
    {"label":"B","text":"反思这种等级秩序背后的价值支撑点到底在哪。","effects":{"scale":-0.5,"force":0.8,"order":0.7,"stance":-0.9}},
    {"label":"C","text":"享受这种距离感，因为我并不想真的和他产生连接。","effects":{"scale":-0.8,"force":0.5,"order":0.2,"stance":-0.6}},
    {"label":"D","text":"感到被权力压制的局促，这种不平等的互动让人不适。","effects":{"scale":0.3,"force":-0.5,"order":0.9,"stance":1.0}}
  ]},
  {"id":"q15","unit":"第三篇章：意义的剧场 (Unit 3: Theater of Meaning)","unit_desc":"我们在社会中扮演什么角色？意义、仪式与互动如何构造我们的世界？","scenario":"财富本质：关于钱这个东西，你认为：","options":[
    {"label":"A","text":"它是展现社会地位最好的道具，让表演更真实。","effects":{"scale":-0.7,"force":0.8,"order":-0.2,"stance":-0.8}},
    {"label":"B","text":"它是理性的化身，把世界变成了一个精准算计的牢笼。","effects":{"scale":-0.4,"force":0.9,"order":0.7,"stance":-0.9}},
    {"label":"C","text":"它是一种冷漠的中介，让所有情感都变得像买卖一样。","effects":{"scale":-0.8,"force":0.5,"order":0.1,"stance":-0.7}},
    {"label":"D","text":"它是万恶之源，也是所有社会不平等的根基。","effects":{"scale":1.0,"force":-1.0,"order":1.0,"stance":1.0}}
  ]},
  {"id":"q16","unit":"第四篇章：逻辑的铁笼 (Unit 4: Iron Cage of Logic)","unit_desc":"理性与技术如何塑造并限制现代生活？效率是解放，还是囚禁？","scenario":"数据困局：当你面对无处不在的数据考核和评分系统时：","options":[
    {"label":"A","text":"感到一种绝望，仿佛自己被关进了一个透明的铁笼里。","effects":{"scale":-0.4,"force":0.8,"order":0.6,"stance":-1.0}},
    {"label":"B","text":"觉得人与人的沟通消失了，取而代之的是冰冷的指令。","effects":{"scale":0.8,"force":0.9,"order":-0.4,"stance":0.7}},
    {"label":"C","text":"意识到这只是为了规避风险而产生的一套过度防御逻辑。","effects":{"scale":1.0,"force":0.5,"order":0.7,"stance":0.8}},
    {"label":"D","text":"觉得没什么不好，量化能让社会运行得更公平高效。","effects":{"scale":0.7,"force":-0.6,"order":-0.8,"stance":-0.5}}
  ]},
  {"id":"q17","unit":"第四篇章：逻辑的铁笼 (Unit 4: Iron Cage of Logic)","unit_desc":"理性与技术如何塑造并限制现代生活？效率是解放，还是囚禁？","scenario":"观点争鸣：对于网络争端和观点撕裂，你倾向于认为：","options":[
    {"label":"A","text":"这种吵闹是无效的，大家只是在理性的荒原上互相吼叫。","effects":{"scale":-0.4,"force":0.9,"order":0.7,"stance":-0.9}},
    {"label":"B","text":"因为我们失去了真诚对话的共同语言，只剩下立场博弈。","effects":{"scale":0.8,"force":1.0,"order":-0.6,"stance":0.8}},
    {"label":"C","text":"这是因为风险社会中，大家对未来都没有安全感的表现。","effects":{"scale":0.9,"force":0.6,"order":0.8,"stance":0.7}},
    {"label":"D","text":"这是多元社会的常态，有助于各种声音被听见。","effects":{"scale":-0.3,"force":0.4,"order":-0.2,"stance":-0.8}}
  ]},
  {"id":"q18","unit":"第四篇章：逻辑的铁笼 (Unit 4: Iron Cage of Logic)","unit_desc":"理性与技术如何塑造并限制现代生活？效率是解放，还是囚禁？","scenario":"算法决策：如果有一个万能算法能决定你未来的职业，你的感受是：","options":[
    {"label":"A","text":"极度排斥，因为它彻底杀死了命运的神圣性和不可知性。","effects":{"scale":-0.4,"force":0.9,"order":0.6,"stance":-1.0}},
    {"label":"B","text":"感到不安，因为它剥夺了我们通过协商改变未来的权利。","effects":{"scale":0.7,"force":0.8,"order":-0.5,"stance":0.8}},
    {"label":"C","text":"充满怀疑，算法背后的漏洞可能会制造更大的社会灾难。","effects":{"scale":0.9,"force":0.4,"order":0.9,"stance":0.9}},
    {"label":"D","text":"乐于接受，只要它真的能帮我避开那些弯路和失败。","effects":{"scale":0.8,"force":-0.5,"order":-0.7,"stance":-0.4}}
  ]},
  {"id":"q19","unit":"第四篇章：逻辑的铁笼 (Unit 4: Iron Cage of Logic)","unit_desc":"理性与技术如何塑造并限制现代生活？效率是解放，还是囚禁？","scenario":"技术焦虑：面对日益强大的 AI 技术，你最担心的不仅仅是失业，而是：","options":[
    {"label":"A","text":"人类彻底失去了那种基于信仰和情感的生命意义。","effects":{"scale":-0.4,"force":1.0,"order":0.5,"stance":-0.9}},
    {"label":"B","text":"我们失去了对技术背后权力的监督与理性抗辩的能力。","effects":{"scale":0.8,"force":0.9,"order":-0.4,"stance":0.9}},
    {"label":"C","text":"我们正进入一个谁也无法预测后果的全球实验场。","effects":{"scale":1.0,"force":0.4,"order":0.8,"stance":0.8}},
    {"label":"D","text":"没什么好担心的，技术进化是文明必然的进程。","effects":{"scale":0.5,"force":-0.2,"order":-0.4,"stance":-0.9}}
  ]},
  {"id":"q20","unit":"第四篇章：逻辑的铁笼 (Unit 4: Iron Cage of Logic)","unit_desc":"理性与技术如何塑造并限制现代生活？效率是解放，还是囚禁？","scenario":"现代疏离：你认为现代人孤独感的源头是：","options":[
    {"label":"A","text":"每个人都成了庞大系统里一个可以被随时替换的零件。","effects":{"scale":-0.6,"force":0.8,"order":0.7,"stance":-0.9}},
    {"label":"B","text":"我们在屏幕背后敲字，却再也无法进行真正的灵魂共振。","effects":{"scale":0.8,"force":0.9,"order":-0.5,"stance":0.8}},
    {"label":"C","text":"生活中充满了各种无法掌控的变数，让人自顾不暇。","effects":{"scale":0.9,"force":0.6,"order":0.8,"stance":0.7}},
    {"label":"D","text":"社交半径太大了，导致我们的情感连接变得极其稀薄。","effects":{"scale":-0.3,"force":-0.4,"order":-0.6,"stance":-0.5}}
  ]},
  {"id":"q21","unit":"第五篇章：边界的震颤 (Unit 5: Tremor of Boundaries)","unit_desc":"在流动的当代世界，身份、风险与归属的边界正在如何瓦解与重塑？","scenario":"流动生存：你对说走就走的数字游民生活，内心深处的看法是：","options":[
    {"label":"A","text":"看起来很自由，但这种流动其实是一种极度的不稳定。","effects":{"scale":0.8,"force":0.7,"order":0.8,"stance":0.9}},
    {"label":"B","text":"这依然是特权者的游戏，建立在全球资源分配不均之上。","effects":{"scale":0.4,"force":-0.4,"order":0.9,"stance":0.9}},
    {"label":"C","text":"是一场极致的自我营销，必须不断把品味变现。","effects":{"scale":-0.8,"force":0.9,"order":0.7,"stance":0.7}},
    {"label":"D","text":"是在高度不确定的世界中，不得不采取的防御性迁徙。","effects":{"scale":0.9,"force":0.4,"order":0.8,"stance":0.8}}
  ]},
  {"id":"q22","unit":"第五篇章：边界的震颤 (Unit 5: Tremor of Boundaries)","unit_desc":"在流动的当代世界，身份、风险与归属的边界正在如何瓦解与重塑？","scenario":"全球格局：面对跨国家政或远程服务这些现象，你首先想到的是：","options":[
    {"label":"A","text":"一种脆弱的雇佣关系，人与人之间只有暂时的价值链接。","effects":{"scale":0.7,"force":0.5,"order":0.7,"stance":0.9}},
    {"label":"B","text":"一个复杂的交叉网格，涉及性别、国籍与阶级的多重剥削。","effects":{"scale":0.6,"force":-0.6,"order":1.0,"stance":1.0}},
    {"label":"C","text":"一场身体与情绪的博弈，外表和态度成了新的商品。","effects":{"scale":-0.7,"force":0.9,"order":0.7,"stance":0.7}},
    {"label":"D","text":"一种全球化的风险转嫁，问题的源头在更远的地方。","effects":{"scale":0.9,"force":0.4,"order":0.8,"stance":0.8}}
  ]},
  {"id":"q23","unit":"第五篇章：边界的震颤 (Unit 5: Tremor of Boundaries)","unit_desc":"在流动的当代世界，身份、风险与归属的边界正在如何瓦解与重塑？","scenario":"技术审美：当 AI 的创作水平超越人类时，你最敏锐的观察点是：","options":[
    {"label":"A","text":"审美的变迁变得太快了，人类的原创力正在变得廉价。","effects":{"scale":0.7,"force":0.8,"order":0.6,"stance":0.9}},
    {"label":"B","text":"这种技术的领先将让全球贫富差距变得更加无法逾越。","effects":{"scale":0.8,"force":-0.4,"order":0.9,"stance":1.0}},
    {"label":"C","text":"谁掌握了算法，谁就掌握了未来什么是美的定义权。","effects":{"scale":-0.6,"force":1.0,"order":0.8,"stance":0.7}},
    {"label":"D","text":"我们正在制造一个完全无法理解其逻辑的智慧生命。","effects":{"scale":0.9,"force":0.5,"order":0.8,"stance":0.8}}
  ]},
  {"id":"q24","unit":"第五篇章：边界的震颤 (Unit 5: Tremor of Boundaries)","unit_desc":"在流动的当代世界，身份、风险与归属的边界正在如何瓦解与重塑？","scenario":"标签认同：关于你身上的各种标签如性别、职业、家乡，你认为：","options":[
    {"label":"A","text":"它们越来越模糊了，像液体一样可以随时流向任何地方。","effects":{"scale":0.6,"force":0.7,"order":0.5,"stance":0.8}},
    {"label":"B","text":"它们不是孤立的，而是像锁链一样共同决定了我的处境。","effects":{"scale":0.5,"force":-0.3,"order":0.9,"stance":0.9}},
    {"label":"C","text":"它们是我可以利用的符号，用来在社交场域中兑换资本。","effects":{"scale":-0.8,"force":0.9,"order":0.7,"stance":0.6}},
    {"label":"D","text":"它们是我的救生衣，在动荡的世界里给我一点安全感。","effects":{"scale":0.8,"force":0.4,"order":0.6,"stance":0.7}}
  ]},
  {"id":"q25","unit":"第五篇章：边界的震颤 (Unit 5: Tremor of Boundaries)","unit_desc":"在流动的当代世界，身份、风险与归属的边界正在如何瓦解与重塑？","scenario":"终极成功：在当下，你觉得真正的成功者应该是：","options":[
    {"label":"A","text":"那些没有任何包袱，能随时抛弃过去快速变道的人。","effects":{"scale":0.7,"force":0.8,"order":0.6,"stance":0.9}},
    {"label":"B","text":"那些能看穿全球不平等链条，并在其中找到空隙的人。","effects":{"scale":0.6,"force":-0.4,"order":1.0,"stance":0.9}},
    {"label":"C","text":"那些能把自己的品味、身体与形象经营成顶级IP的人。","effects":{"scale":-0.9,"force":1.0,"order":0.8,"stance":0.7}},
    {"label":"D","text":"那些能预见风险，并带着大家成功避坑的生存专家。","effects":{"scale":0.9,"force":0.5,"order":0.8,"stance":0.8}}
  ]}
];
