from pathlib import Path
import re
import subprocess
import tempfile

root = Path(__file__).resolve().parents[1]
html = (root / "index.html").read_text(encoding="utf-8")

scripts = re.findall(r"<script(?:\\s[^>]*)?>([\\s\\S]*?)</script\\s*>", html, re.IGNORECASE)
if len(scripts) != 1:
    raise SystemExit(f"Expected one inline application script, found {len(scripts)}")

if re.search(r"<script[^>]+src=[\"']https?://", html, re.IGNORECASE):
    raise SystemExit("Unexpected remote JavaScript dependency")

required_sections = ["MAGERIT", "ENS", "controles", "evidencias"]
lower_html = html.lower()
missing = [section for section in required_sections if section.lower() not in lower_html]
if missing:
    raise SystemExit(f"Expected application content is missing: {missing}")

with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as handle:
    handle.write(scripts[0])
    script_path = Path(handle.name)

try:
    subprocess.run(["node", "--check", str(script_path)], check=True)
finally:
    script_path.unlink(missing_ok=True)

print("ENS BLACKOUT static application validation passed.")
