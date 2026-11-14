from flask import Flask, send_from_directory, request, jsonify
from pathlib import Path
import json
current_dir = Path(__file__).resolve().parent
filepath = current_dir.parent / "furntend"
print(filepath)
app = Flask(str(filepath), static_folder=str(filepath), static_url_path="") #""= lochost

    
#@app
@app.route('/')#call func when user access 
def index():
    print(app.static_folder)
    return send_from_directory(app.static_folder, 'index.html')
    
@app.route('/rec', methods=['POST'])
def rec():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    if data == "+":
         x=1
    elif data == "-":
         x=-1
    with open( (current_dir/"now_index.txt") ,"r") as f:
            index=f.read()
    with open( (current_dir/"now_index.txt"),"w") as f:
            if int(index) >= 0:
                f.write(str(int(index)+x))
            else:
                f.write(str(index))
    print(data)
    return jsonify({"message": "Data received successfully", "data": data}), 200

@app.route('/qr', methods=['get'])
def qr():
    #get the curry qr code name
    with open((current_dir/"qr.json"),"r") as f:
        data=json.load(f)
    with open((current_dir/"now_index.txt"),"r") as f:
        index=f.read()
        print(index)
        print(data[int(index)])
    return data[int(index)]


def run(port=5000,url=""):
    app.run(debug=True, host='', port=port)


def start_app(filepath=filepath, port=5000, url=""):
    run(port, url)

start_app()