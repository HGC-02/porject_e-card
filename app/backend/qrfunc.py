import qrcode
import json
from pathlib import Path

current_dir = Path(__file__).resolve().parent
filepath = current_dir.parent / "furntend" /"qr"

def generate_qr_code(data,filename, filepath=filepath):
    img=qrcode.make(data)
    img.save(filepath / filename)
    return str(filepath / filename)
def add_to_json_file(qr_code_path, name,filename):
    payload=[
        {"qr_name":name,
         "qr_code_path": qr_code_path,
         "file_name":filename}
    ] 
    with open(filename, 'w') as f:
        json.dump(payload, f)
def add_link(link,name):
    qr_code_path = generate_qr_code(link, f"{name}.png")
    add_to_json_file(qr_code_path, name)