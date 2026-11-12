from pathlib import Path
import re
import subprocess
import tempfile

root = Path(__file__).resolve().parents[1]
html = (root / "index.html").read_text(encoding="utf-8")

scripts = re.findall(r"<script[^>]*>(.*?)</script>", html, re.IGNORECASE | re.DOTALL)
if len(scripts) != 1:
    raise SystemExit(f"Expected one inline application script, found {len(scripts)}")

if re.search(r"<script[^>]+src=[\"']https?://", html, re.IGNORECASE):
    raise SystemExit("Unexpected remote JavaScript dependency")

required_sections = ["MAGERIT", "ENS", "controles", "evidencias", "SIMULACIÓN"]
lower_html = html.lower()
missing = [section for section in required_sections if section.lower() not in lower_html]
if missing:
    raise SystemExit(f"Expected application content is missing: {missing}")

script = scripts[0]
unsafe_user_rendering = re.search(
    r"innerHTML\s*=\s*`[^\`]*\$\{\s*(?:msg|cmd|cmdStr)\s*\}",
    script,
)
if unsafe_user_rendering:
    raise SystemExit("Potential HTML injection: user input is interpolated into innerHTML")

for required_guard in (
    "youMsg.querySelector('.message').textContent = msg;",
    "div.textContent = text;",
    "message.textContent = text;",
):
    if required_guard not in script:
        raise SystemExit(f"Expected safe text rendering is missing: {required_guard}")

with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as handle:
    handle.write(script)
    script_path = Path(handle.name)

try:
    subprocess.run(["node", "--check", str(script_path)], check=True)
finally:
    script_path.unlink(missing_ok=True)

print("ENS BLACKOUT static application and safe-rendering validation passed.")
