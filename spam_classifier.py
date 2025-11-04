import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib # For saving the model

def load_data(file_path):
    """
    Loads the spam dataset from a CSV file.
    The CSV should have two columns: 'v1' for the label (ham/spam)
    and 'v2' for the message text.
    """
    df = pd.read_csv(file_path, encoding='latin-1')
    # Keep only the necessary columns
    df = df[['v1', 'v2']]
    df.columns = ['label', 'message']
    return df

def train_and_save_model(df, model_path='spam_classifier_model.pkl'):
    """
    Trains a spam classification model and saves it to a file.
    """
    X = df['message']
    y = df['label']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a pipeline that first creates TF-IDF features and then trains a Naive Bayes classifier
    model_pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english')),
        ('classifier', MultinomialNB())
    ])

    # Train the model
    model_pipeline.fit(X_train, y_train)

    # Evaluate the model (optional, good for logging)
    accuracy = model_pipeline.score(X_test, y_test)
    print(f"Model trained with accuracy: {accuracy:.4f}")

    # Save the trained model pipeline
    joblib.dump(model_pipeline, model_path)
    print(f"Model saved to {model_path}")

    return model_pipeline

if __name__ == '__main__':
    # This block runs when the script is executed directly
    # It will train the model and save it.
    # You need to have a 'spam.csv' file in the same directory.
    try:
        dataframe = load_data('spam.csv')
        train_and_save_model(dataframe)
    except FileNotFoundError:
        print("Error: 'spam.csv' not found.")
        print("Please download the SMS Spam Collection dataset and save it as 'spam.csv'.")
        print("You can find it here: https://www.kaggle.com/uciml/sms-spam-collection-dataset")
