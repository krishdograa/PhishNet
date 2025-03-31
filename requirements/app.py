import sys
import os
from flask import Flask, request, jsonify

# Add src folder to Python path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from predict import predict_email  # Importing the predict_email function

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    email = request.json.get('email')
    if not email:
        return jsonify({"error": "Email text is required"}), 400

    # Adjusted model file path (relative to requirements folder)
    model_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'models', 'phishing_detector.pkl'))
    
    result = predict_email(model_file_path, email)
    return jsonify({"prediction": result})

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Phishing Email Detection API is running!"})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
