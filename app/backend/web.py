from flask import Flask, send_from_directory, request, jsonify
app = ""
def init(fileroot):
    global app
    app = Flask(fileroot, static_folder="static", static_url_path="") #""= lochost
    
#@app
@app.route('/')#call func when user access 
def index():
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
