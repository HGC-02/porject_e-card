from pathlib import Path
import shutil
import subprocess
import sys
import os
current_dir = Path(__file__).resolve().parent
ud=current_dir/"userdata"
scr=Path(ud/"qr")
qr=current_dir/"furntend/qr"

def fix():
    with open(ud/"qr.json","w") as f:
        f.write("[]")

if qr.is_dir() and qr.iterdir():
    for i in qr.iterdir():
        if i.is_file() or i.is_symlink():
            i.unlink
else:
    Path(qr).mkdir(parents=True, exist_ok=True)
shutil.copytree(scr, qr, dirs_exist_ok=True)
with open(ud/"qr.json","r") as f:
    x=f.read()
with open(current_dir/"backend/qr.json","w") as f:
    if x:
        f.write(x)
    else:
        f.write("[]")
        fix()
with open(current_dir/"backend/now_index.txt","w")as f:
    f.write("0")



command = current_dir/"backend/main.py"  
if sys.platform == "win32":
    
    print("win")
    subprocess.run([sys.executable, command])
    


else:
    os.execvp("python3", ["python3", current_dir/"backend/main.py"])
