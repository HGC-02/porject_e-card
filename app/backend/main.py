from pathlib import Path
import subprocess
import sys
import qrcodetui
import time
import atexit


current_dir = Path(__file__).resolve().parent
log=current_dir/"log/web.log"
time.sleep(1)
with open(log,"a") as f:
    web=subprocess.Popen([sys.executable,"-u", str(current_dir / "web.py")],stdout=f,stderr=subprocess.STDOUT)

try:
    qrcodetui.main()
finally:
    web.terminate()
atexit.register(web.terminate)