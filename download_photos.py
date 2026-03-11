"""
Downloads scholar portraits from Wikimedia Commons and saves them locally.
Falls back to placeholder SVG if download fails.
"""
import urllib.request
import os
import base64

SCHOLARS = [
    ("marx", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Karl_Marx_001.jpg/440px-Karl_Marx_001.jpg"),
    ("durkheim", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/%C3%89mile_Durkheim.jpg/440px-%C3%89mile_Durkheim.jpg"),
    ("weber", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Max_Weber_1894.jpg/440px-Max_Weber_1894.jpg"),
    ("simmel", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Georg_Simmel.jpg/440px-Georg_Simmel.jpg"),
    ("foucault", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Foucault_BNF.jpg/440px-Foucault_BNF.jpg"),
    ("bourdieu", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Pierre_Bourdieu%2C_1990.jpg/440px-Pierre_Bourdieu%2C_1990.jpg"),
    ("goffman", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Erving_Goffman.jpg/440px-Erving_Goffman.jpg"),
    ("habermas", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Habermas.jpg/440px-Habermas.jpg"),
    ("mears", None),  # No Wikimedia photo - use generated placeholder
    ("beck", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Ulrich_Beck.jpg/440px-Ulrich_Beck.jpg"),
    ("lan", None),   # No Wikimedia photo - use generated placeholder
    ("bauman", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Zygmunt_Bauman.jpg/440px-Zygmunt_Bauman.jpg"),
]

PLACEHOLDER_SVG = lambda initials, color: f"""<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'>
  <circle cx='100' cy='100' r='100' fill='{color}'/>
  <text x='100' y='115' text-anchor='middle' font-size='72' font-family='sans-serif' fill='white' font-weight='bold'>{initials}</text>
</svg>"""

PLACEHOLDER_COLORS = {
    "mears": "#7c3aed",
    "lan": "#0891b2",
}
PLACEHOLDER_INITIALS = {
    "mears": "AM",
    "lan": "PL",
}

headers = {
    'User-Agent': 'Mozilla/5.0 (SociusTrace/1.0; educational project) AppleWebKit/537.36'
}

photos = {}
out_dir = "c:/Users/Kui Ching/.gemini/test/photos"
os.makedirs(out_dir, exist_ok=True)

for scholar_id, url in SCHOLARS:
    path = f"{out_dir}/{scholar_id}.jpg"
    
    if url is None:
        # SVG placeholder
        svg = PLACEHOLDER_SVG(
            PLACEHOLDER_INITIALS.get(scholar_id, "?"),
            PLACEHOLDER_COLORS.get(scholar_id, "#6b7280")
        )
        b64 = base64.b64encode(svg.encode()).decode()
        photos[scholar_id] = f"data:image/svg+xml;base64,{b64}"
        print(f"[placeholder] {scholar_id}")
        continue

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
        with open(path, 'wb') as f:
            f.write(data)
        b64 = base64.b64encode(data).decode()
        photos[scholar_id] = f"data:image/jpeg;base64,{b64}"
        print(f"[ok] {scholar_id} ({len(data)//1024}KB)")
    except Exception as e:
        # Fallback to initials placeholder
        initials = scholar_id[:2].upper()
        svg = PLACEHOLDER_SVG(initials, "#6b7280")
        b64 = base64.b64encode(svg.encode()).decode()
        photos[scholar_id] = f"data:image/svg+xml;base64,{b64}"
        print(f"[fallback] {scholar_id}: {e}")

# Save result so build_scholars.py can import it
import json
with open("c:/Users/Kui Ching/.gemini/test/photos_b64.json", "w") as f:
    json.dump(photos, f)

print(f"\nDone. {len(photos)} photos encoded.")
