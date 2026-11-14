from flask import Flask, send_from_directory, request, jsonify
from pathlib import Path

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
    #add func of sent back to the logic proc 
    return jsonify({"message": "Data received successfully", "data": data}), 200

def run(port=5000,url=""):
    app.run(debug=True, host='', port=port)


def start_app(filepath=filepath, port=5000, url=""):
    run(port, url)

start_app()