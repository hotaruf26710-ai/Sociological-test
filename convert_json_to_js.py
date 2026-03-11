import json

with open('c:/Users/Kui Ching/.gemini/test/questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

with open('c:/Users/Kui Ching/.gemini/test/questions.js', 'w', encoding='utf-8') as f:
    f.write("export const questions = ")
    json.dump(questions, f, indent=2, ensure_ascii=False)
    f.write(";\n")

with open('c:/Users/Kui Ching/.gemini/test/scholars.json', 'r', encoding='utf-8') as f:
    scholars = json.load(f)

with open('c:/Users/Kui Ching/.gemini/test/scholars.js', 'w', encoding='utf-8') as f:
    f.write("export const scholars = ")
    json.dump(scholars, f, indent=2, ensure_ascii=False)
    f.write(";\n")

print("Successfully generated JS data files.")
