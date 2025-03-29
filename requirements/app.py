import sys
import os
from flask import Flask, request, jsonify, render_template
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from predict import predict_email

app = Flask(__name__)

# Route to render the web page
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')  # Now renders the front-end

# Prediction route for API requests (Postman)
@app.route('/predict', methods=['POST'])
def predict():
    # Check if request is from the form or API
    if request.content_type == 'application/json':
        email = request.json.get('email')
    else:
        email = request.form.get('email')  # For form submissions

    if not email:
        return jsonify({"error": "Email text is required"}), 400

    result = predict_email("models/phishing_detector.pkl", "data/preprocessed_data.pkl", email)

    # Return result to the web page or API response
    if request.content_type == 'application/json':
        return jsonify({"prediction": result})
    else:
        return render_template('index.html', prediction=result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
