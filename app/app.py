from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "SmartLog AI Log  updated  is running!"

@app.route('/analyze', methods=['POST'])
def analyze_logs():
    try:
        # Get the log text from request JSON
        data = request.get_json()
        logs = data.get('logs', '')

        if not logs:
            return jsonify({"error": "No logs provided"}), 400

        # Basic AI-like pattern detection (simple but explainable)
        lines = logs.split('\n')
        errors = [line for line in lines if 'error' in line.lower()]
        warnings = [line for line in lines if 'warn' in line.lower()]
        info = [line for line in lines if 'info' in line.lower()]

        response = {
            "total_lines": len(lines),
            "error_count": len(errors),
            "warning_count": len(warnings),
            "info_count": len(info),
            "errors_found": errors[:5]  # show first 5 errors
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
