import json
import re

text = """
## Unit 1: Structural Foundation (Order & System)
01. Relay race: A. Precision roles / B. Individual talent
02. Power outage: A. Official dispatch / B. Local mutual aid
03. City planning: A. Functional zones / B. Organic chaos
04. Education: A. Norm compliance / B. Individual critique
05. Taxes: A. Contribution to whole / B. External burden
06. Slang: A. Disruption of efficiency / B. Evolutionary creativity
07. Law: A. Value consensus / B. Conflict management
08. Holidays: A. Collective solidarity / B. Functional rest
09. Landmarks: A. Organizational power / B. Individual sacrifice
10. Bridge: A. Rules for public good / B. Rules for resource holders

## Unit 2: Phantom of Power (Power & Inequality)
11. Security guards: A. Order & Safety / B. Social exclusion
12. Jargon: A. Professional depth / B. Symbolic dominance
13. Elite life: A. Individual willpower / B. Invisible resources
14. Etiquette: A. Social lubricant / B. Invisible shackles
15. Charity: A. Responsibility / B. Calculated PR
16. "Old Money" style: A. Quality pursuit / B. Class distinction
17. Flat orgs: A. Ideal equality / B. Hidden power
18. CCTV: A. Protection / B. Surveillance
19. Expensive gifts: A. Generosity / B. Symbolic debt
20. Bridge: A. Duty to norms / B. Social dramaturgy

## Unit 3: Theater of Meaning (Interaction & Symbolism)
21. Social masks: A. Stage roles / B. Inauthenticity
22. Elevator silence: A. Civil inattention / B. Urban coldness
23. Table manners: A. Identity ritual / B. Redundant tradition
24. Social media: A. Impression management / B. Self-recording
25. First meeting: A. Cues & Vibes / B. Institutional background
26. Public crying: A. Personal narrative / B. Normative breach
27. Titles: A. First names (Fluid) / B. Honorifics (Structure)
28. Bad gifts: A. Relationship maintenance / B. Material value
29. Silence: A. Symbolic signal / B. Communication breakdown
30. Bridge: A. Meaning-making / B. Rational calculation

## Unit 4: Iron Cage (Rationalization & Tech)
31. GPS navigation: A. Algorithmic efficiency / B. Intuitive path
32. Schedule: A. Mastery & Order / B. Suffocation
33. Standardized tests: A. Meritocratic fairness / B. Erasure of richness
34. Smart home: A. Total liberation / B. Loss of agency
35. KPIs: A. Objective metric / B. Dehumanized data
36. Dating apps: A. Optimized matching / B. Romantic unpredictability
37. Insurance: A. Risk management / B. Psychological safety
38. Data footprint: A. Personalization / B. Objectification
39. Fast food: A. Rationalized quality / B. Loss of ritual
40. Bridge: A. Scientific certainty / B. Fragile tremor

## Unit 5: Tremor of Boundaries (Contemporary Risk)
41. One-career life: A. Identity security / B. Stagnation
42. Climate change: A. Distant disaster / B. Global risk society
43. Digital nomads: A. True freedom / B. Precarious connectivity
44. AI art: A. Broken barriers / B. Threat to humanity
45. Gender fluidity: A. Diverse inclusion / B. Cognitive burden
46. Competency: A. Specialization / B. Interdisciplinary agility
47. Crypto: A. Risk bubble / B. Institutional challenge
48. Privacy: A. Collective safety / B. Individual boundary
49. Online intimacy: A. Pure souls / B. Virtual phantom
50. Global ties: A. Relational nodes / B. Uncontrollable danger
"""

lines = text.strip().split('\n')
questions = []
current_unit = ""

for line in lines:
    line = line.strip()
    if not line:
        continue
    if line.startswith('## '):
        current_unit = line[3:].strip()
    elif re.match(r'^\d+\.', line):
        # Example format: 01. Relay race: A. Precision roles / B. Individual talent
        match = re.match(r'^(\d+)\.\s+(.*?):\s+A\.\s+(.*?)\s+/\s+B\.\s+(.*)$', line)
        if match:
            q_id = f"q{int(match.group(1)):02d}"
            scenario = match.group(2).strip()
            opt_a_text = match.group(3).strip()
            opt_b_text = match.group(4).strip()
            
            questions.append({
                "id": q_id,
                "unit": current_unit,
                "scenario": scenario,
                "options": [
                    {
                        "label": "A",
                        "text": opt_a_text,
                        "effects": {
                            "scale": 0.0,
                            "force": 0.0,
                            "order": 0.0,
                            "stance": 0.0
                        }
                    },
                    {
                        "label": "B",
                        "text": opt_b_text,
                        "effects": {
                            "scale": 0.0,
                            "force": 0.0,
                            "order": 0.0,
                            "stance": 0.0
                        }
                    }
                ]
            })

with open('c:/Users/Kui Ching/.gemini/test/questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"Successfully converted {len(questions)} questions to questions.json")
