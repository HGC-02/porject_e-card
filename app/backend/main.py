from pathlib import Path
import subprocess
import sys
import qrcodetui
import time
current_dir = Path(__file__).resolve().parent

time.sleep(1)
web=subprocess.Popen([sys.executable, str(current_dir / "web.py")],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

try:
    qrcodetui.main()
finally:
    web.terminate()