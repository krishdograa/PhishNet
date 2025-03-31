import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

def predict_email(model_file, email_text):
    # Load the trained model and vectorizer
    try:
        with open(model_file, "rb") as f:
            model, vectorizer = pickle.load(f)  # Expecting two objects: model and vectorizer
    except Exception as e:
        print(f"Error loading model: {e}")  # Print error for debugging
        return "Error: Unable to load model"
    
    # Vectorize the input email
    email_vector = vectorizer.transform([email_text])
        
    # Make prediction
    prediction = model.predict(email_vector)
    
    return "Phishing" if prediction[0] == 1 else "Not Phishing"

if __name__ == "__main__":
    email_text = """Subject: Hey Bro! Just Checking In
Hey [Brother’s Name],

Hope you're doing well! Just wanted to check in and see how things are going. How’s everything at your end?

Let’s catch up soon—maybe a call or hangout this weekend? Let me know what works for you!

Take care,
[Your Name]

"""
    result = predict_email("models/phishing_detector_xgboost.pkl", email_text)
    print(f"Prediction: {result}")
