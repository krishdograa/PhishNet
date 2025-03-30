from flask import Flask, request, jsonify
from src.predict import predict_email  # Assuming your predict function is properly imported

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 415
    
    data = request.get_json()
    email_text = data.get("email")
    if not email_text:
        return jsonify({"error": "No email text provided"}), 400

    prediction = predict_email(email_text)
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True)
