import pickle

def predict_email(model_file, vectorizer_file, email_text):
    # Load the model
    with open(model_file, "rb") as f:
        model = pickle.load(f)

    # Load the vectorizer
    with open(vectorizer_file, "rb") as f:
        _, _, vectorizer = pickle.load(f)

    # Vectorize the input email
    email_vector = vectorizer.transform([email_text]).toarray()

    # Make a prediction
    prediction = model.predict(email_vector)
    return "Phishing" if prediction[0] == 1 else "Not Phishing"

if __name__ == "__main__":
    email_text = """Hi Team,

Hope you're having a productive week.

Just a reminder about our Q3 planning meeting scheduled for next week. Please find the proposed agenda attached to this email.

Meeting Details:

Date: Wednesday, April 2nd, 2025
Time: 9:00 AM - 11:00 AM PST
Location: Conference Room B
Please review the agenda beforehand and come prepared to discuss your team's progress and priorities for the next quarter.

If you have any questions or cannot attend, please let me know by the end of the day on Monday.

Thanks,
John"""
    print(email_text)
    result = predict_email("models/phishing_detector.pkl", "data/preprocessed_data.pkl", email_text)
    print(f"Prediction: {result}")
