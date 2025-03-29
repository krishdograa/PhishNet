import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def combine_features(row):
    # Combine relevant text features for better context
    return f"{row['subject']} {row['body']} {row['urls']}"

def preprocess_data(input_file, output_file):
    # Load the CSV file
    data = pd.read_csv(input_file)

    # Ensure the necessary columns exist
    required_columns = ['subject', 'body', 'urls', 'label']
    for col in required_columns:
        if col not in data.columns:
            raise ValueError(f"Input CSV must have '{col}' column.")

    # Combine key features into a single text field
    data['combined_text'] = data.apply(combine_features, axis=1)

    # Vectorize the combined text using TF-IDF (sparse matrix format)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(data['combined_text'])

    # Extract labels
    y = data['label'].values

    # Save preprocessed data and vectorizer
    with open(output_file, "wb") as f:
        pickle.dump((X, y, vectorizer), f)

    print(f"Preprocessed data saved to {output_file}")

if __name__ == "__main__":
    preprocess_data("data/phishing_emails.csv", "data/preprocessed_data.pkl")
