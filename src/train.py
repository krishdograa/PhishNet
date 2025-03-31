import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from xgboost import XGBClassifier

def train_model(data_file, model_file):
    # Load preprocessed data
    with open(data_file, "rb") as f:
        X, y, vectorizer = pickle.load(f)  # Unpack all three objects

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the XGBoost classifier
    model = XGBClassifier(
        n_estimators=100,
        max_depth=5,
        learning_rate=0.1,
        objective='binary:logistic',
        eval_metric='logloss'
    )

    # Train the model
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred):.4f}")
    print(f"Recall: {recall_score(y_test, y_pred):.4f}")
    print(f"F1-score: {f1_score(y_test, y_pred):.4f}")

    # Save the trained model and vectorizer
    with open(model_file, "wb") as f:
        pickle.dump((model, vectorizer), f)  # Save both model and vectorizer

if __name__ == "__main__":
    train_model("data/preprocessed_data.pkl", "models/phishing_detector_xgboost.pkl")
