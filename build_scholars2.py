# -*- coding: utf-8 -*-
import json, os

photos = json.load(open("c:/Users/Kui Ching/.gemini/test/photos_b64.json", encoding="utf-8"))

scholars = [
    {
        "id": "marx", "name": "卡尔·马克思", "nameEn": "Karl Marx", "era": "古典",
        "vector": [1.0, -1.0, 1.0, 1.0], "type": "B-权力解构者",
        "quote": {
            "zh": "哲学家们只是用不同的方式解释世界，而问题在于改变世界。",
            "en": "The philosophers have only interpreted the world; the point is to change it.",
            "source": "Theses on Feuerbach (《关于费尔巴哈的提纲》)",
            "detail": "Thesis XI, 1845"
        },
        "description": "你看透了物质基础对社会结构的决定作用，倾向于从宏观冲突的角度去解构隐形的权力剥削，并抱有强烈的现实批判精神。你不满足于解释世界——你更想介入并改变它。",
        "photo": photos.get("marx", "")
    },
    {
        "id": "durkheim", "name": "埃米尔·涂尔干", "nameEn": "Emile Durkheim", "era": "古典",
        "vector": [0.8, -0.3, -0.8, -0.7], "type": "A-秩序建筑师",
        "quote": {
            "zh": "社会事实必须被当作物来研究。",
            "en": "Social facts must be treated as things.",
            "source": "The Rules of Sociological Method (《社会学方法的准则》)",
            "detail": "Chapter 2, 1895"
        },
        "description": "你重视宏观共识与系统秩序，相信社会是一个有机整体，规则与约束是维系人类团结与抵抗失范的基石。你用科学的眼光观察社会，寻找背后的结构性规律。",
        "photo": photos.get("durkheim", "")
    },
    {
        "id": "weber", "name": "马克斯·韦伯", "nameEn": "Max Weber", "era": "古典",
        "vector": [-0.4, 0.8, 0.3, -0.9], "type": "C-意义编织者",
        "quote": {
            "zh": "专家没有灵魂，享乐者没有心肝。",
            "en": "Specialists without spirit, sensualists without heart.",
            "source": "The Protestant Ethic and the Spirit of Capitalism (《新教伦理与资本主义精神》)",
            "detail": "Part II, Ch. 5, 1905"
        },
        "description": "理性与意义是你的核心关注点。你警惕现代社会铁笼的蔓延，更关注微观个体行动背后的动机与符号运作，坚持客观审慎的解释学立场。",
        "photo": photos.get("weber", "")
    },
    {
        "id": "simmel", "name": "乔治·齐美尔", "nameEn": "Georg Simmel", "era": "古典",
        "vector": [-0.8, 0.9, 0.4, -0.5], "type": "C-意义编织者",
        "quote": {
            "zh": "现代生活最深层的问题，源于个体在面对压倒性的社会力量时，仍企图保持其生存的自治与独特性。",
            "en": "The deepest problems of modern life derive from the claim of the individual to preserve autonomy in the face of overwhelming social forces.",
            "source": "The Metropolis and Mental Life (《大都市与精神生活》)",
            "detail": "1903"
        },
        "description": "你有一双能从日常细节中发现宏大命题的眼睛，着迷于货币、时尚、陌生人等微观现象背后的符号逻辑，在现代都市的喧嚣中敏锐捕捉个体与社会的张力。",
        "photo": photos.get("simmel", "")
    },
    {
        "id": "foucault", "name": "米歇尔·福柯", "nameEn": "Michel Foucault", "era": "现代",
        "vector": [-0.5, 1.0, 1.0, 1.0], "type": "B-权力解构者",
        "quote": {
            "zh": "权力无处不在；不是因为它包罗万象，而是因为它来自四面八方。",
            "en": "Power is everywhere; not because it embraces everything, but because it comes from everywhere.",
            "source": "The History of Sexuality, Vol. 1 (《性经验史》)",
            "detail": "Part 4, Ch. 2, 1976"
        },
        "description": "你能从微观的日常话语、知识与医学中捕捉到无处不在的权力规训，并试图打破那些看似自然的真理霸权。你质疑一切既定正常背后的权力运作。",
        "photo": photos.get("foucault", "")
    },
    {
        "id": "bourdieu", "name": "皮埃尔·布迪厄", "nameEn": "Pierre Bourdieu", "era": "现代",
        "vector": [0.5, 0.7, 0.8, 0.7], "type": "B-权力解构者",
        "quote": {
            "zh": "社会世界是累积的历史。",
            "en": "The social world is accumulated history.",
            "source": "The Forms of Capital (《资本的形态》)",
            "detail": "1986"
        },
        "description": "你对场域与惯习高度敏感，能清晰看到文化品味、教育资本、社交圈子如何在不着痕迹间完成阶级的再生产。你是识破自然化不平等的侦探。",
        "photo": photos.get("bourdieu", "")
    },
    {
        "id": "goffman", "name": "欧文·戈夫曼", "nameEn": "Erving Goffman", "era": "现代",
        "vector": [-0.9, 1.0, -0.2, -0.2], "type": "C-意义编织者",
        "quote": {
            "zh": "整个世界，说实话，就是一场婚礼。",
            "en": "All the world is a stage, and all the men and women merely performers.",
            "source": "The Presentation of Self in Everyday Life (《日常生活中的自我呈现》)",
            "detail": "Introduction, 1956"
        },
        "description": "你高度关注互动的微观细节——每个眼神、每个停顿、每件衣服都是你的分析对象。你深刻理解社交不过是一场精心布置的舞台表演，每个人都是演员，也是观众。",
        "photo": photos.get("goffman", "")
    },
    {
        "id": "habermas", "name": "尤尔根·哈贝马斯", "nameEn": "Juergen Habermas", "era": "现代",
        "vector": [0.6, 0.3, -0.5, 0.4], "type": "A-秩序建筑师",
        "quote": {
            "zh": "系统对生活世界的殖民。",
            "en": "The colonization of the lifeworld by the system.",
            "source": "The Theory of Communicative Action (《沟通行动理论》)",
            "detail": "Vol. 2, 1981"
        },
        "description": "你相信理性对话与民主审议的力量，警惕金钱与权力系统对日常生活意义的侵蚀，对公共理性抱有坚定信念，希望通过沟通达成社会共识。",
        "photo": photos.get("habermas", "")
    },
    {
        "id": "mears", "name": "阿什利·米尔斯", "nameEn": "Ashley Mears", "era": "当代",
        "vector": [-0.7, 0.9, 0.7, 0.6], "type": "C-意义编织者",
        "quote": {
            "zh": "审美资本的定价不仅关乎金钱，更关乎在欲望场域中被看见的社会权利。",
            "en": "The pricing of aesthetic capital is not just about money, but about the social right to be seen in the field of desire.",
            "source": "Very Important People (《定价美丽》)",
            "detail": "Ch. 3, 2011"
        },
        "description": "你洞察日常社交与互动中隐藏的符号资本运作，能看穿VIP圈子、时尚与美貌如何成为阶层区隔的工具，并以当代民族志的方式记录这一切。",
        "photo": photos.get("mears", "")
    },
    {
        "id": "beck", "name": "乌尔里希·贝克", "nameEn": "Ulrich Beck", "era": "当代",
        "vector": [0.3, 0.4, 0.5, 0.2], "type": "D-风险观测员",
        "quote": {
            "zh": "在风险社会中，未知的、意外的后果成了主导力量。",
            "en": "In the risk society, unknown and unintended consequences come to be a dominant force in history.",
            "source": "Risk Society: Towards a New Modernity (《风险社会》)",
            "detail": "Ch. 1, 1986"
        },
        "description": "你敏锐察觉当代社会的边界模糊与不确定性，更关注全球化与技术带来的系统性、弥散性风险——在风险社会中，贫困是等级制的，而雾霾则是民主的。",
        "photo": photos.get("beck", "")
    },
    {
        "id": "lan", "name": "蓝佩嘉", "nameEn": "Pei-chia Lan", "era": "当代",
        "vector": [-0.3, 0.6, 0.8, 0.8], "type": "B-权力解构者",
        "quote": {
            "zh": "跨国移工不仅在跨越地理边境，更是在跨越阶级与认同的深沟。",
            "en": "Transnational migrants cross not just geographical borders but the deep trenches of class and identity.",
            "source": "Global Cinderellas (《全球灰姑娘》)",
            "detail": "Introduction, 2006"
        },
        "description": "你有强烈的性别与阶级敏感性，关注劳动、身体与跨国流动中的权力不对等，能从家务劳动、照护工作等隐形场域中看到宏观制度对微观生命的深刻塑造。",
        "photo": photos.get("lan", "")
    },
    {
        "id": "bauman", "name": "齐格蒙·鲍曼", "nameEn": "Zygmunt Bauman", "era": "当代",
        "vector": [0.2, 0.6, 0.6, 0.5], "type": "D-风险观测员",
        "quote": {
            "zh": "在流动的现代性中，改变是唯一的永恒，不确定性是唯一的定数。",
            "en": "In liquid modernity, change is the only permanence, and uncertainty the only certainty.",
            "source": "Liquid Modernity (《流动的现代性》)",
            "detail": "Introduction, 2000"
        },
        "description": "你深感一切固态的承诺——工作、关系、认同——都在流动现代性中快速消融。你对当代社会的碎片化、不安全感有着清醒而忧郁的洞察，是这个时代忠实的目击者。",
        "photo": photos.get("bauman", "")
    }
]

out = "const SOCIUS_SCHOLARS = " + json.dumps(scholars, indent=2, ensure_ascii=False) + ";\n"
with open("c:/Users/Kui Ching/.gemini/test/scholars.js", "w", encoding="utf-8") as f:
    f.write(out)
print("Done.", len(scholars), "scholars written.")
