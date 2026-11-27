import qrcode
import json
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
filepath = current_dir.parent / "furntend" /"qr"

def generate_qr_code(data,filename, filepath=filepath):
    img=qrcode.make(data)
    img.save(filepath / filename)
    return str(filepath / filename)

def add_to_json_file( name,filename):
    payload=[
        {"qr_name":name,
         "file_name":filename}
    ] 
    with open(current_dir/"qr.json",'r') as f:
        x=json.load(f)
        if x:
            payload.extend(x)
            print(payload)
    with open(current_dir/"qr.json","w") as f:
        json.dump(payload,f)

def add_link(link,name):
    qr_code_path = generate_qr_code(link, f"{name}.png")
    print(qr_code_path)
    add_to_json_file( name,(f"{name}.png"))
