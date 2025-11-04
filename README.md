# Spam Message Classifier

This project is a machine learning application that classifies SMS messages as either "Spam" or "Ham" (not spam). It uses a Streamlit web interface for interactive classification.

The project is built using Python, scikit-learn, and Streamlit, and follows the OpenSpec methodology for spec-driven development.

## Features
- Interactive web interface to classify messages.
- Trains a Naive Bayes classifier on the SMS Spam Collection dataset.
- Clear separation of UI (`app.py`) and machine learning logic (`spam_classifier.py`).
- Data visualization with word clouds to show the most common words in spam and ham messages.

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Setup and Run

1.  **Clone the repository (if you haven't already):**
    ```bash
    # git clone ...
    ```

2.  **Install dependencies:**
    Navigate to the project directory and install the required Python packages.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Download the Dataset:**
    This model is trained on the "SMS Spam Collection Data Set" from the UCI Machine Learning Repository.
    - Download the dataset from Kaggle: [https://www.kaggle.com/uciml/sms-spam-collection-dataset](https://www.kaggle.com/uciml/sms-spam-collection-dataset)
    - Unzip the file and place `spam.csv` in the root directory of this project.

4.  **Train the Model:**
    Run the training script to process the data and create the classifier model file (`spam_classifier_model.pkl`).
    ```bash
    python spam_classifier.py
    ```
    You should see an accuracy score printed to the console and confirmation that the model was saved.

5.  **Run the Streamlit App:**
    Launch the web application.
    ```bash
    streamlit run app.py
    ```
    Your browser should open with the application running. You can now enter messages to see their classification.
