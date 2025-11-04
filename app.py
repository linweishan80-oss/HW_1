import streamlit as st
import joblib
import os

# Define the path to the model
MODEL_PATH = 'spam_classifier_model.pkl'

@st.cache_resource
def load_model(model_path):
    """Loads the trained classifier model."""
    if not os.path.exists(model_path):
        return None
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return None

st.title('Spam Classifier')

# Load the model
model = load_model(MODEL_PATH)

if model is None:
    st.warning("**Model not found.** Please train the model first.")
    st.info("To train the model, run the following command in your terminal:\n\n"            "1. Make sure you have the `spam.csv` dataset in the root directory.\n"            "2. Run the script: `python spam_classifier.py`")
else:
    # Add a st.text_area for user input
    user_input = st.text_area('Enter a message to classify:')

    # Add a button to trigger the classification
    classify_button = st.button('Classify')

    # Add a placeholder to display the result
    if classify_button and user_input:
        # Use the model to predict
        prediction = model.predict([user_input])
        
        # Display the result
        st.subheader("Result")
        if prediction[0] == 'spam':
            st.error("This message is classified as SPAM.")
        else:
            st.success("This message is classified as NOT SPAM (Ham).")