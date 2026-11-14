"""Teeb index.html-ist GitHub Pagesi lehe docs/index.html.

index.html on Claude Artifacti lähtekood (ilma <html>/<head>/<body>).
See skript lisab dokumendi raami, Firebase'i teegid ja seadistuse.
Käivita: python3 build.py
"""
import pathlib, re

ROOT = pathlib.Path(__file__).parent
FIREBASE = "10.12.2"
src = (ROOT / "index.html").read_text(encoding="utf-8")

cut = src.index("<header")
head_part, body_part = src[:cut], src[cut:]

scripts = "\n".join(
    f'<script src="https://www.gstatic.com/firebasejs/{FIREBASE}/firebase-{m}-compat.js"></script>'
    for m in ("app", "auth", "firestore")
)

page = f"""<!doctype html>
<html lang="et">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="3x3 korvpalli oskuste hoov Eesti naistele ja tüdrukutele: 10 oskust, videod, treeningplaanid ja enesetestid. Eesti ja vene keeles.">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0;font-family:system-ui,sans-serif;font-size:14px}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
{head_part.strip()}
{scripts}
<script src="firebase-config.js"></script>
</head>
<body>
{body_part.strip()}
</body>
</html>
"""
(ROOT / "docs" / "index.html").write_text(page, encoding="utf-8")
print("docs/index.html valmis")
