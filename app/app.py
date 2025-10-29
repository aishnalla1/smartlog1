from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "SmartLog AI Log Analyzer is running!"

@app.route('/analyze', methods=['POST'])
def analyze_log():
    log_data = request.json.get("log", "")
    if "error" in log_data.lower():
        result = "Error detected! Please check the system logs."
    else:
        result = "No critical issues found."
    return jsonify({"analysis_result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
