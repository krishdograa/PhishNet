from flask import Flask, request, jsonify, render_template
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from predict import predict_email

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    email = request.json.get('email')
    if not email:
        return jsonify({"error": "Email text is required"}), 400

    result = predict_email("models/phishing_detector.pkl", "data/preprocessed_data.pkl", email)
    return jsonify({"prediction": result})

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')  # Now renders the front-end

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)



@app.route('/debug-structure')
def debug_structure():
    structure = []
    for root, dirs, files in os.walk('.'):
        structure.append(f"{root}/")
        for d in dirs:
            structure.append(f"├── {d}/")
        for f in files:
            structure.append(f"│   ├── {f}")
    return "<pre>" + "\n".join(structure) + "</pre>"