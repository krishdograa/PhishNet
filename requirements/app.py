import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.predict import predict_email  # Now it should find the src folder

from flask import Flask, request, jsonify

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
    return jsonify({"message": "Phishing Email Detection API is running!"})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)


