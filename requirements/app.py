import sys
import os
from flask import Flask, request, jsonify
from src.predict import predict_email  # Importing the predict_email function

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    email = request.json.get('email')
    if not email:
        return jsonify({"error": "Email text is required"}), 400

    # Call the prediction function with the email text, model is loaded in predict.py
    result = predict_email("models/phishing_detector.pkl", email)
    return jsonify({"prediction": result})

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Phishing Email Detection API is running!"})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
