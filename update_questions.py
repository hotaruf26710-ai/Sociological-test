"""
generate_data.py — 一键生成 questions.js 和 scholars.js
从 JSON 数据中构建，避免 Python 源码中混入中文引号造成 SyntaxError
"""
import json, pathlib

ROOT = pathlib.Path("c:/Users/Kui Ching/.gemini/test")

# ─────────────────────────────────────────────────────────────────
# SCHOLARS
# ─────────────────────────────────────────────────────────────────
scholars = [
  {"id":"marx","name":"卡尔·马克思","nameEn":"Karl Marx","era":"古典",
   "vector":[1.0,-1.0,1.0,1.0],"type":"B-权力解构者",
   "quote":{"zh":"哲学家们只是用不同的方式解释世界，而问题在于改变世界。",
            "en":"The philosophers have only interpreted the world; the point is to change it.",
            "source":"Theses on Feuerbach (《关于费尔巴哈的提纲》)","detail":"Thesis XI, 1845"},
   "description":"你看透了物质基础对社会结构的决定作用，倾向于从宏观冲突的角度去解构隐形的权力剥削，并抱有强烈的现实批判精神。你不满足于解释世界——你更想介入并改变它。",
   "photo":"photos/marx.jpg.png"},
  {"id":"durkheim","name":"埃米尔·涂尔干","nameEn":"Emile Durkheim","era":"古典",
   "vector":[1.0,0.5,-1.0,-0.8],"type":"A-秩序建筑师",
   "quote":{"zh":"社会事实必须被当作物来研究。",
            "en":"Social facts must be treated as things.",
            "source":"The Rules of Sociological Method (《社会学方法的准则》)","detail":"Chapter 2, 1895"},
   "description":"你重视宏观共识与系统秩序，相信社会是一个有机整体，规则与约束是维系人类团结与抵抗失范的基石。你用科学的眼光观察社会，寻找背后的结构性规律。",
   "photo":"photos/durkheim.jpg.png"},
  {"id":"weber","name":"马克斯·韦伯","nameEn":"Max Weber","era":"古典",
   "vector":[-0.6,1.0,0.6,-1.0],"type":"C-意义编织者",
   "quote":{"zh":"专家没有灵魂，享乐者没有心肝。",
            "en":"Specialists without spirit, sensualists without heart.",
            "source":"The Protestant Ethic and the Spirit of Capitalism (《新教伦理与资本主义精神》)","detail":"Part II, Ch. 5, 1905"},
   "description":"理性与意义是你的核心关注点。你警惕现代社会铁笼的蔓延，更关注微观个体行动背后的动机与符号运作，坚持客观审慎的解释学立场。",
   "photo":"photos/weber.jpg.png"},
  {"id":"simmel","name":"乔治·齐美尔","nameEn":"Georg Simmel","era":"古典",
   "vector":[-0.9,0.7,-0.2,-0.6],"type":"C-意义编织者",
   "quote":{"zh":"现代生活最深层的问题，源于个体在面对压倒性的社会力量时，仍企图保持其生存的自治与独特性。",
            "en":"The deepest problems of modern life derive from the claim of the individual to preserve autonomy in the face of overwhelming social forces.",
            "source":"The Metropolis and Mental Life (《大都市与精神生活》)","detail":"1903"},
   "description":"你有一双能从日常细节中发现宏大命题的眼睛，着迷于货币、时尚、陌生人等微观现象背后的符号逻辑，在现代都市的喧嚣中敏锐捕捉个体与社会的张力。",
   "photo":"photos/simmel.jpg.png"},
  {"id":"foucault","name":"米歇尔·福柯","nameEn":"Michel Foucault","era":"现代",
   "vector":[-0.6,0.9,1.0,1.0],"type":"B-权力解构者",
   "quote":{"zh":"权力无处不在；不是因为它包罗万象，而是因为它来自四面八方。",
            "en":"Power is everywhere; not because it embraces everything, but because it comes from everywhere.",
            "source":"The History of Sexuality, Vol. 1 (《性经验史》)","detail":"Part 4, Ch. 2, 1976"},
   "description":"你能从微观的日常话语、知识与医学中捕捉到无处不在的权力规训，并试图打破那些看似自然的真理霸权。你质疑一切既定正常背后的权力运作。",
   "photo":"photos/foucault.jpg.png"},
  {"id":"bourdieu","name":"皮埃尔·布迪厄","nameEn":"Pierre Bourdieu","era":"现代",
   "vector":[0.6,1.0,1.0,0.8],"type":"B-权力解构者",
   "quote":{"zh":"社会世界是累积的历史。","en":"The social world is accumulated history.",
            "source":"The Forms of Capital (《资本的形态》)","detail":"1986"},
   "description":"你对场域与惯习高度敏感，能清晰看到文化品味、教育资本、社交圈子如何在不着痕迹间完成阶级的再生产。你是识破自然化不平等的侦探。",
   "photo":"photos/boudieu.jpg.png"},
  {"id":"goffman","name":"欧文·戈夫曼","nameEn":"Erving Goffman","era":"现代",
   "vector":[-1.0,0.7,-0.3,-0.9],"type":"C-意义编织者",
   "quote":{"zh":"整个世界，说实话，就是一场婚礼。",
            "en":"All the world is a stage, and all the men and women merely performers.",
            "source":"The Presentation of Self in Everyday Life (《日常生活中的自我呈现》)","detail":"Introduction, 1956"},
   "description":"你高度关注互动的微观细节——每个眼神、每个停顿、每件衣服都是你的分析对象。你深刻理解社交不过是一场精心布置的舞台表演，每个人都是演员，也是观众。",
   "photo":"photos/goffman.jpg.png"},
  {"id":"habermas","name":"尤尔根·哈贝马斯","nameEn":"Juergen Habermas","era":"现代",
   "vector":[0.8,0.9,-0.5,0.7],"type":"A-秩序建筑师",
   "quote":{"zh":"系统对生活世界的殖民。","en":"The colonization of the lifeworld by the system.",
            "source":"The Theory of Communicative Action (《沟通行动理论》)","detail":"Vol. 2, 1981"},
   "description":"你相信理性对话与民主审议的力量，警惕金钱与权力系统对日常生活意义的侵蚀，对公共理性抱有坚定信念，希望通过沟通达成社会共识。",
   "photo":"photos/habermas.jpg.png"},
  {"id":"mears","name":"阿什利·米尔斯","nameEn":"Ashley Mears","era":"当代",
   "vector":[-0.8,1.0,0.8,0.7],"type":"C-意义编织者",
   "quote":{"zh":"审美资本的定价不仅关乎金钱，更关乎在欲望场域中被看见的社会权利。",
            "en":"The pricing of aesthetic capital is not just about money, but about the social right to be seen in the field of desire.",
            "source":"Very Important People (《定价美丽》)","detail":"Ch. 3, 2011"},
   "description":"你洞察日常社交与互动中隐藏的符号资本运作，能看穿VIP圈子、时尚与美貌如何成为阶层区隔的工具，并以当代民族志的方式记录这一切。",
   "photo":"photos/mears.jpg.png"},
  {"id":"beck","name":"乌尔里希·贝克","nameEn":"Ulrich Beck","era":"当代",
   "vector":[0.9,0.5,0.8,0.7],"type":"D-风险观测员",
   "quote":{"zh":"在风险社会中，未知的、意外的后果成了主导力量。",
            "en":"In the risk society, unknown and unintended consequences come to be a dominant force in history.",
            "source":"Risk Society: Towards a New Modernity (《风险社会》)","detail":"Ch. 1, 1986"},
   "description":"你敏锐察觉当代社会的边界模糊与不确定性，更关注全球化与技术带来的系统性、弥散性风险——在风险社会中，贫困是等级制的，而雾霾则是民主的。",
   "photo":"photos/becker.jpg.png"},
  {"id":"lan","name":"蓝佩嘉","nameEn":"Pei-chia Lan","era":"当代",
   "vector":[0.5,-0.4,0.9,0.9],"type":"B-权力解构者",
   "quote":{"zh":"跨国移工不仅在跨越地理边境，更是在跨越阶级与认同的深沟。",
            "en":"Transnational migrants cross not just geographical borders but the deep trenches of class and identity.",
            "source":"Global Cinderellas (《全球灰姑娘》)","detail":"Introduction, 2006"},
   "description":"你有强烈的性别与阶级敏感性，关注劳动、身体与跨国流动中的权力不对等，能从家务劳动、照护工作等隐形场域中看到宏观制度对微观生命的深刻塑造。",
   "photo":"photos/pei-chia lan.jpg.png"},
  {"id":"bauman","name":"齐格蒙·鲍曼","nameEn":"Zygmunt Bauman","era":"当代",
   "vector":[0.7,0.7,0.7,0.9],"type":"D-风险观测员",
   "quote":{"zh":"在流动的现代性中，改变是唯一的永恒，不确定性是唯一的定数。",
            "en":"In liquid modernity, change is the only permanence, and uncertainty the only certainty.",
            "source":"Liquid Modernity (《流动的现代性》)","detail":"Introduction, 2000"},
   "description":"你深感一切固态的承诺——工作、关系、认同——都在流动现代性中快速消融。你对当代社会的碎片化、不安全感有着清醒而忧郁的洞察，是这个时代忠实的目击者。",
   "photo":"photos/bauman.jpg.png"},
]

# ─────────────────────────────────────────────────────────────────
# UNIT META
# ─────────────────────────────────────────────────────────────────
UNIT_FULL = {
    "结构的基石": "第一篇章：结构的基石 (Unit 1: Substrate of Order)",
    "权力的幽灵": "第二篇章：权力的幽灵 (Unit 2: Phantom of Power)",
    "意义的剧场": "第三篇章：意义的剧场 (Unit 3: Theater of Meaning)",
    "逻辑的铁笼": "第四篇章：逻辑的铁笼 (Unit 4: Iron Cage of Logic)",
    "边界的震颤": "第五篇章：边界的震颤 (Unit 5: Tremor of Boundaries)",
}
UNIT_DESC = {
    "结构的基石": "社会运作的底层逻辑是什么？谁设计了这套隐形的规则？",
    "权力的幽灵": "权力如何在日常生活中无处不在地运作——而我们对此浑然不觉？",
    "意义的剧场": "我们在社会中扮演什么角色？意义、仪式与互动如何构造我们的世界？",
    "逻辑的铁笼": "理性与技术如何塑造并限制现代生活？效率是解放，还是囚禁？",
    "边界的震颤": "在流动的当代世界，身份、风险与归属的边界正在如何瓦解与重塑？",
}

# ─────────────────────────────────────────────────────────────────
# QUESTIONS (raw data — weights field renamed to effects on output)
# ─────────────────────────────────────────────────────────────────
raw_questions = json.loads(r"""
[
  {"id":1,"unit":"结构的基石","context":"感知世界：独自行走在大城市的深夜，那种"秩序感"让你觉得：","options":[{"tag":"A","text":"是一种无形的默契，大家虽不相识却共同守护着安宁。","w":{"scale":0.8,"force":0.4,"order":-0.8,"stance":-0.6}},{"tag":"B","text":"是一种压抑的平衡，背后的资源争夺从未停止。","w":{"scale":0.9,"force":-0.8,"order":0.8,"stance":0.8}},{"tag":"C","text":"是一种迷人的疏离，每个人都是彼此世界里的路人。","w":{"scale":-0.8,"force":0.6,"order":-0.1,"stance":-0.5}},{"tag":"D","text":"是一套高效的程序，路灯和监控在精确地维持运转。","w":{"scale":0.7,"force":-0.4,"order":-0.5,"stance":-0.3}}]},
  {"id":2,"unit":"结构的基石","context":"步入机构：面对一家规章制度极其死板的机构，你的第一反应是：","options":[{"tag":"A","text":"挺好的，这能给每个人提供明确的安全感和位置。","w":{"scale":0.7,"force":0.3,"order":-0.7,"stance":-0.5}},{"tag":"B","text":"很难受，这套规则显然是为了更方便地榨取我的精力。","w":{"scale":0.8,"force":-0.7,"order":0.7,"stance":0.7}},{"tag":"C","text":"无所谓，只要我能在这个缝隙里保持自己的独立就行。","w":{"scale":-0.7,"force":0.5,"order":0.1,"stance":-0.4}},{"tag":"D","text":"很好奇，这套非人情的逻辑是如何被设计出来的。","w":{"scale":0.5,"force":0.6,"order":0.4,"stance":-0.8}}]},
  {"id":3,"unit":"结构的基石","context":"极端设想：如果整个社会突然陷入没有规则的真空状态，你最恐惧的是：","options":[{"tag":"A","text":"失去归属感，像断了线的风筝一样在荒野中游荡。","w":{"scale":0.8,"force":0.7,"order":-0.9,"stance":-0.6}},{"tag":"B","text":"失去反抗的目标，最终被更原始的暴力所吞噬。","w":{"scale":0.9,"force":-0.8,"order":0.9,"stance":0.8}},{"tag":"C","text":"失去社交的趣味，一切独特的个人魅力都变得毫无意义。","w":{"scale":-0.9,"force":0.8,"order":-0.2,"stance":-0.5}},{"tag":"D","text":"失去效率，所有的现代便利瞬间崩塌成废墟。","w":{"scale":0.8,"force":-0.5,"order":-0.6,"stance":-0.2}}]},
  {"id":4,"unit":"结构的基石","context":"教育反思：关于学校这门必修课，你认为它最真实的底色是：","options":[{"tag":"A","text":"它教会我们如何成为社会这台机器里的一颗合格螺丝。","w":{"scale":0.9,"force":0.4,"order":-0.8,"stance":-0.5}},{"tag":"B","text":"它是一道隐形的墙，用来筛选谁能留下、谁该离开。","w":{"scale":0.8,"force":0.6,"order":0.8,"stance":0.7}},{"tag":"C","text":"它是一个巨大的舞台，让我们学习如何体面地与人周旋。","w":{"scale":-0.7,"force":0.7,"order":0.0,"stance":-0.4}},{"tag":"D","text":"它是一座工厂，将知识像零件一样安装进我们的脑中。","w":{"scale":0.7,"force":-0.4,"order":-0.5,"stance":-0.2}}]},
  {"id":5,"unit":"结构的基石","context":"集体归属：你参与集体活动的初衷，通常是因为：","options":[{"tag":"A","text":"渴望融入某种伟大的共鸣，寻找超越个体的神圣感。","w":{"scale":0.8,"force":0.9,"order":-0.8,"stance":-0.7}},{"tag":"B","text":"意识到单打独斗没有出路，必须和同类站在一起。","w":{"scale":0.7,"force":-0.8,"order":0.8,"stance":0.7}},{"tag":"C","text":"享受这种与人产生连接、却又不必深交的轻盈感。","w":{"scale":-0.9,"force":0.7,"order":-0.1,"stance":-0.4}},{"tag":"D","text":"纯粹是为了完成任务或交换所需的资源。","w":{"scale":0.5,"force":-0.6,"order":-0.2,"stance":-0.5}}]},
  {"id":6,"unit":"权力的幽灵","context":"门槛直觉：看到顶级会所的入会门槛，你内心的真实潜台词是：","options":[{"tag":"A","text":"他们在筛选某种共同的品味和家庭教养。","w":{"scale":0.5,"force":0.9,"order":0.7,"stance":0.6}},{"tag":"B","text":"这是一种心理暗示，在训练我们对权力的敬畏。","w":{"scale":-0.4,"force":0.8,"order":0.9,"stance":0.9}},{"tag":"C","text":"这就是金钱铸造的围栏，简单且粗暴。","w":{"scale":0.9,"force":-1.0,"order":0.9,"stance":0.8}},{"tag":"D","text":"这只是为了维持一个特定环境的运营策略。","w":{"scale":0.4,"force":-0.2,"order":-0.2,"stance":-0.7}}]},
  {"id":7,"unit":"权力的幽灵","context":"职场规范：关于那些约定俗成的职场礼仪或穿搭，你认为：","options":[{"tag":"A","text":"这是一张入场券，用来证明你属于这个圈子。","w":{"scale":0.6,"force":0.9,"order":0.8,"stance":0.7}},{"tag":"B","text":"这是一套软性的枷锁，在悄悄修正你的身体和言行。","w":{"scale":-0.5,"force":0.7,"order":0.9,"stance":0.9}},{"tag":"C","text":"这种形式主义，实质上是管理层对员工的服从性测试。","w":{"scale":0.8,"force":-0.7,"order":0.9,"stance":0.8}},{"tag":"D","text":"挺有意思的，它反映了某种特定文化下的互动逻辑。","w":{"scale":-0.6,"force":0.6,"order":0.1,"stance":-0.8}}]},
  {"id":8,"unit":"权力的幽灵","context":"审美变迁：当你发现某个小众品味突然变得大众化时，你会：","options":[{"tag":"A","text":"感到这种品味已经贬值，因为它失去了阶层区隔的作用。","w":{"scale":0.6,"force":1.0,"order":0.9,"stance":0.7}},{"tag":"B","text":"觉得这是大众被某种主流审美话语集体俘获了。","w":{"scale":0.8,"force":0.9,"order":0.9,"stance":1.0}},{"tag":"C","text":"意识到这只是资本为了创造新需求而进行的新一轮割草。","w":{"scale":0.9,"force":-0.8,"order":0.9,"stance":0.8}},{"tag":"D","text":"只是单纯觉得风潮变了，对此保持中立的观察。","w":{"scale":-0.5,"force":0.3,"order":-0.3,"stance":-0.9}}]},
  {"id":9,"unit":"权力的幽灵","context":"权威认知：你如何看待所谓的权威专家？","options":[{"tag":"A","text":"他们掌握着定义什么是正确的最高级文化资本。","w":{"scale":0.7,"force":0.9,"order":0.8,"stance":0.7}},{"tag":"B","text":"他们是权力网络中的节点，负责通过知识来施行管理。","w":{"scale":0.7,"force":0.8,"order":1.0,"stance":0.9}},{"tag":"C","text":"他们往往是利益集团的代言人，在巩固现有的不平等。","w":{"scale":0.8,"force":-0.7,"order":0.9,"stance":0.8}},{"tag":"D","text":"他们是专业领域的领航员，虽然有时也会犯错。","w":{"scale":0.5,"force":0.2,"order":-0.4,"stance":-0.9}}]},
  {"id":10,"unit":"权力的幽灵","context":"社会痛点：你认为这个世界最让你感到不公的地方在于：","options":[{"tag":"A","text":"哪怕你再努力，也难以习得那种从小熏陶出的气质。","w":{"scale":0.5,"force":1.0,"order":0.9,"stance":0.8}},{"tag":"B","text":"你的一举一动都被无形的规则注视着，且你已习惯了它。","w":{"scale":-0.6,"force":0.8,"order":0.9,"stance":0.9}},{"tag":"C","text":"绝大多数的财富和机会都被极少数人牢牢攥在手里。","w":{"scale":0.9,"force":-0.9,"order":1.0,"stance":0.8}},{"tag":"D","text":"很多时候我们无法看清真相，只能在迷雾中摸索。","w":{"scale":-0.4,"force":0.4,"order":0.3,"stance":-1.0}}]},
  {"id":11,"unit":"意义的剧场","context":"社交面貌：在社交场合表现出一个精致的自我，这让你感到：","options":[{"tag":"A","text":"理所当然，社交本质上就是一场需要演技的舞台剧。","w":{"scale":-1.0,"force":0.7,"order":-0.4,"stance":-0.9}},{"tag":"B","text":"有点疲惫，因为我很难找到这背后的真实意义。","w":{"scale":-0.5,"force":0.8,"order":0.6,"stance":-0.9}},{"tag":"C","text":"很有必要，这种职业面具是对私生活的保护。","w":{"scale":-0.8,"force":0.6,"order":-0.1,"stance":-0.6}},{"tag":"D","text":"感到异化，觉得那个社交中的人根本不是我。","w":{"scale":0.8,"force":-0.8,"order":0.9,"stance":0.9}}]},
  {"id":12,"unit":"意义的剧场","context":"驱动来源：你追求一份事业的动力，更多来自于：","options":[{"tag":"A","text":"享受在那个特定领域里被大家认可的角色光环。","w":{"scale":-0.8,"force":0.8,"order":-0.3,"stance":-0.8}},{"tag":"B","text":"响应内心的某种感召，哪怕它看起来并不划算。","w":{"scale":-0.6,"force":1.0,"order":0.5,"stance":-0.9}},{"tag":"C","text":"这种互动中带给我的独特体验和个体成就感。","w":{"scale":-0.9,"force":0.7,"order":0.1,"stance":-0.6}},{"tag":"D","text":"获得更好的物质保障，改变自己的生活处境。","w":{"scale":0.8,"force":-1.0,"order":0.8,"stance":0.9}}]},
  {"id":13,"unit":"意义的剧场","context":"网红打卡：面对网红景点排长队的现象，你的第一反应是：","options":[{"tag":"A","text":"大家都在参与一场集体仪式，为了拍出一张符合人设的照片。","w":{"scale":-0.9,"force":0.8,"order":-0.2,"stance":-0.7}},{"tag":"B","text":"在这个干枯的世界里，人们在疯狂寻找某种神圣的错觉。","w":{"scale":-0.4,"force":0.9,"order":0.6,"stance":-0.8}},{"tag":"C","text":"典型的都市时尚流变，人们在追求瞬间的视觉刺激。","w":{"scale":-0.8,"force":0.7,"order":0.1,"stance":-0.5}},{"tag":"D","text":"一场精心策划的消费陷阱，充满了虚假的狂欢。","w":{"scale":0.8,"force":-0.7,"order":0.9,"stance":1.0}}]},
  {"id":14,"unit":"意义的剧场","context":"互动尴尬：当你与重要人物如领导独处感到尴尬时，你的内心在：","options":[{"tag":"A","text":"疯狂搜索合适的剧本，试图管理好对方对我的印象。","w":{"scale":-1.0,"force":0.6,"order":-0.4,"stance":-0.9}},{"tag":"B","text":"反思这种等级秩序背后的价值支撑点到底在哪。","w":{"scale":-0.5,"force":0.8,"order":0.7,"stance":-0.9}},{"tag":"C","text":"享受这种距离感，因为我并不想真的和他产生连接。","w":{"scale":-0.8,"force":0.5,"order":0.2,"stance":-0.6}},{"tag":"D","text":"感到被权力压制的局促，这种不平等的互动让人不适。","w":{"scale":0.3,"force":-0.5,"order":0.9,"stance":1.0}}]},
  {"id":15,"unit":"意义的剧场","context":"财富本质：关于钱这个东西，你认为：","options":[{"tag":"A","text":"它是展现社会地位最好的道具，让表演更真实。","w":{"scale":-0.7,"force":0.8,"order":-0.2,"stance":-0.8}},{"tag":"B","text":"它是理性的化身，把世界变成了一个精准算计的牢笼。","w":{"scale":-0.4,"force":0.9,"order":0.7,"stance":-0.9}},{"tag":"C","text":"它是一种冷漠的中介，让所有情感都变得像买卖一样。","w":{"scale":-0.8,"force":0.5,"order":0.1,"stance":-0.7}},{"tag":"D","text":"它是万恶之源，也是所有社会不平等的根基。","w":{"scale":1.0,"force":-1.0,"order":1.0,"stance":1.0}}]},
  {"id":16,"unit":"逻辑的铁笼","context":"数据困局：当你面对无处不在的数据考核和评分系统时：","options":[{"tag":"A","text":"感到一种绝望，仿佛自己被关进了一个透明的铁笼里。","w":{"scale":-0.4,"force":0.8,"order":0.6,"stance":-1.0}},{"tag":"B","text":"觉得人与人的沟通消失了，取而代之的是冰冷的指令。","w":{"scale":0.8,"force":0.9,"order":-0.4,"stance":0.7}},{"tag":"C","text":"意识到这只是为了规避风险而产生的一套过度防御逻辑。","w":{"scale":1.0,"force":0.5,"order":0.7,"stance":0.8}},{"tag":"D","text":"觉得没什么不好，量化能让社会运行得更公平高效。","w":{"scale":0.7,"force":-0.6,"order":-0.8,"stance":-0.5}}]},
  {"id":17,"unit":"逻辑的铁笼","context":"观点争鸣：对于网络争端和观点撕裂，你倾向于认为：","options":[{"tag":"A","text":"这种吵闹是无效的，大家只是在理性的荒原上互相吼叫。","w":{"scale":-0.4,"force":0.9,"order":0.7,"stance":-0.9}},{"tag":"B","text":"因为我们失去了真诚对话的共同语言，只剩下立场博弈。","w":{"scale":0.8,"force":1.0,"order":-0.6,"stance":0.8}},{"tag":"C","text":"这是因为风险社会中，大家对未来都没有安全感的表现。","w":{"scale":0.9,"force":0.6,"order":0.8,"stance":0.7}},{"tag":"D","text":"这是多元社会的常态，有助于各种声音被听见。","w":{"scale":-0.3,"force":0.4,"order":-0.2,"stance":-0.8}}]},
  {"id":18,"unit":"逻辑的铁笼","context":"算法决策：如果有一个万能算法能决定你未来的职业，你的感受是：","options":[{"tag":"A","text":"极度排斥，因为它彻底杀死了命运的神圣性和不可知性。","w":{"scale":-0.4,"force":0.9,"order":0.6,"stance":-1.0}},{"tag":"B","text":"感到不安，因为它剥夺了我们通过协商改变未来的权利。","w":{"scale":0.7,"force":0.8,"order":-0.5,"stance":0.8}},{"tag":"C","text":"充满怀疑，算法背后的漏洞可能会制造更大的社会灾难。","w":{"scale":0.9,"force":0.4,"order":0.9,"stance":0.9}},{"tag":"D","text":"乐于接受，只要它真的能帮我避开那些弯路和失败。","w":{"scale":0.8,"force":-0.5,"order":-0.7,"stance":-0.4}}]},
  {"id":19,"unit":"逻辑的铁笼","context":"技术焦虑：面对日益强大的 AI 技术，你最担心的不仅仅是失业，而是：","options":[{"tag":"A","text":"人类彻底失去了那种基于信仰和情感的生命意义。","w":{"scale":-0.4,"force":1.0,"order":0.5,"stance":-0.9}},{"tag":"B","text":"我们失去了对技术背后权力的监督与理性抗辩的能力。","w":{"scale":0.8,"force":0.9,"order":-0.4,"stance":0.9}},{"tag":"C","text":"我们正进入一个谁也无法预测后果的全球实验场。","w":{"scale":1.0,"force":0.4,"order":0.8,"stance":0.8}},{"tag":"D","text":"没什么好担心的，技术进化是文明必然的进程。","w":{"scale":0.5,"force":-0.2,"order":-0.4,"stance":-0.9}}]},
  {"id":20,"unit":"逻辑的铁笼","context":"现代疏离：你认为现代人孤独感的源头是：","options":[{"tag":"A","text":"每个人都成了庞大系统里一个可以被随时替换的零件。","w":{"scale":-0.6,"force":0.8,"order":0.7,"stance":-0.9}},{"tag":"B","text":"我们在屏幕背后敲字，却再也无法进行真正的灵魂共振。","w":{"scale":0.8,"force":0.9,"order":-0.5,"stance":0.8}},{"tag":"C","text":"生活中充满了各种无法掌控的变数，让人自顾不暇。","w":{"scale":0.9,"force":0.6,"order":0.8,"stance":0.7}},{"tag":"D","text":"社交半径太大了，导致我们的情感连接变得极其稀薄。","w":{"scale":-0.3,"force":-0.4,"order":-0.6,"stance":-0.5}}]},
  {"id":21,"unit":"边界的震颤","context":"流动生存：你对说走就走的数字游民生活，内心深处的看法是：","options":[{"tag":"A","text":"看起来很自由，但这种流动其实是一种极度的不稳定。","w":{"scale":0.8,"force":0.7,"order":0.8,"stance":0.9}},{"tag":"B","text":"这依然是特权者的游戏，建立在全球资源分配不均之上。","w":{"scale":0.4,"force":-0.4,"order":0.9,"stance":0.9}},{"tag":"C","text":"是一场极致的自我营销，必须不断把品味变现。","w":{"scale":-0.8,"force":0.9,"order":0.7,"stance":0.7}},{"tag":"D","text":"是在高度不确定的世界中，不得不采取的防御性迁徙。","w":{"scale":0.9,"force":0.4,"order":0.8,"stance":0.8}}]},
  {"id":22,"unit":"边界的震颤","context":"全球格局：面对跨国家政或远程服务这些现象，你首先想到的是：","options":[{"tag":"A","text":"一种脆弱的雇佣关系，人与人之间只有暂时的价值链接。","w":{"scale":0.7,"force":0.5,"order":0.7,"stance":0.9}},{"tag":"B","text":"一个复杂的交叉网格，涉及性别、国籍与阶级的多重剥削。","w":{"scale":0.6,"force":-0.6,"order":1.0,"stance":1.0}},{"tag":"C","text":"一场身体与情绪的博弈，外表和态度成了新的商品。","w":{"scale":-0.7,"force":0.9,"order":0.7,"stance":0.7}},{"tag":"D","text":"一种全球化的风险转嫁，问题的源头在更远的地方。","w":{"scale":0.9,"force":0.4,"order":0.8,"stance":0.8}}]},
  {"id":23,"unit":"边界的震颤","context":"技术审美：当 AI 的创作水平超越人类时，你最敏锐的观察点是：","options":[{"tag":"A","text":"审美的变迁变得太快了，人类的原创力正在变得廉价。","w":{"scale":0.7,"force":0.8,"order":0.6,"stance":0.9}},{"tag":"B","text":"这种技术的领先将让全球贫富差距变得更加无法逾越。","w":{"scale":0.8,"force":-0.4,"order":0.9,"stance":1.0}},{"tag":"C","text":"谁掌握了算法，谁就掌握了未来什么是美的定义权。","w":{"scale":-0.6,"force":1.0,"order":0.8,"stance":0.7}},{"tag":"D","text":"我们正在制造一个完全无法理解其逻辑的智慧生命。","w":{"scale":0.9,"force":0.5,"order":0.8,"stance":0.8}}]},
  {"id":24,"unit":"边界的震颤","context":"标签认同：关于你身上的各种标签如性别、职业、家乡，你认为：","options":[{"tag":"A","text":"它们越来越模糊了，像液体一样可以随时流向任何地方。","w":{"scale":0.6,"force":0.7,"order":0.5,"stance":0.8}},{"tag":"B","text":"它们不是孤立的，而是像锁链一样共同决定了我的处境。","w":{"scale":0.5,"force":-0.3,"order":0.9,"stance":0.9}},{"tag":"C","text":"它们是我可以利用的符号，用来在社交场域中兑换资本。","w":{"scale":-0.8,"force":0.9,"order":0.7,"stance":0.6}},{"tag":"D","text":"它们是我的救生衣，在动荡的世界里给我一点安全感。","w":{"scale":0.8,"force":0.4,"order":0.6,"stance":0.7}}]},
  {"id":25,"unit":"边界的震颤","context":"终极成功：在当下，你觉得真正的成功者应该是：","options":[{"tag":"A","text":"那些没有任何包袱，能随时抛弃过去快速变道的人。","w":{"scale":0.7,"force":0.8,"order":0.6,"stance":0.9}},{"tag":"B","text":"那些能看穿全球不平等链条，并在其中找到空隙的人。","w":{"scale":0.6,"force":-0.4,"order":1.0,"stance":0.9}},{"tag":"C","text":"那些能把自己的品味、身体与形象经营成顶级IP的人。","w":{"scale":-0.9,"force":1.0,"order":0.8,"stance":0.7}},{"tag":"D","text":"那些能预见风险，并带着大家成功避坑的生存专家。","w":{"scale":0.9,"force":0.5,"order":0.8,"stance":0.8}}]}
]
""")

questions = []
for q in raw_questions:
    unit_key = q["unit"]
    questions.append({
        "id": f"q{q['id']:02d}",
        "unit": UNIT_FULL[unit_key],
        "unit_desc": UNIT_DESC[unit_key],
        "scenario": q["context"],
        "options": [
            {"label": o["tag"], "text": o["text"],
             "effects": {ax: o["w"][ax] for ax in ("scale","force","order","stance")}}
            for o in q["options"]
        ]
    })

# ─────────────────────────────────────────────────────────────────
# WRITE OUTPUT FILES
# ─────────────────────────────────────────────────────────────────
q_path = ROOT / "questions.js"
s_path = ROOT / "scholars.js"

with open(q_path, "w", encoding="utf-8") as f:
    f.write("const SOCIUS_QUESTIONS = " + json.dumps(questions, indent=2, ensure_ascii=False) + ";\n")
print(f"✅ questions.js — {len(questions)} questions")

with open(s_path, "w", encoding="utf-8") as f:
    f.write("const SOCIUS_SCHOLARS = " + json.dumps(scholars, indent=2, ensure_ascii=False) + ";\n")
print(f"✅ scholars.js   — {len(scholars)} scholars")

# quick axis coverage check
axes = ["scale","force","order","stance"]
print("\n=== Axis coverage (mean absolute value per option) ===")
for ax in axes:
    vals = [o["effects"][ax] for q in questions for o in q["options"]]
    neg = sum(v for v in vals if v < 0)
    pos = sum(v for v in vals if v > 0)
    print(f"  {ax:6}: neg_sum={neg:+.1f}  pos_sum={pos:+.1f}  nonzero={sum(1 for v in vals if v)}/100")
