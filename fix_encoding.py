import pathlib

ROOT = pathlib.Path("c:/Users/Kui Ching/.gemini/test")

# Re-read and write with explicit UTF-8 to fix mojibake
q_path = ROOT / "questions.js"
s_path = ROOT / "scholars.js"

q_content = q_path.read_bytes().decode("utf-8", errors="ignore")
q_path.write_text(q_content, encoding="utf-8")

s_content = s_path.read_bytes().decode("utf-8", errors="ignore")
s_path.write_text(s_content, encoding="utf-8")

print("Files re-encoded to UTF-8")
