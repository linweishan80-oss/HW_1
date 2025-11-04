import streamlit as st
import joblib
import os
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Define the path to the model and data
MODEL_PATH = 'spam_classifier_model.pkl'
DATA_PATH = 'spam.csv'

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

@st.cache_data
def load_data(data_path):
    """Loads the spam dataset."""
    if not os.path.exists(data_path):
        return None
    try:
        df = pd.read_csv(data_path, encoding='latin-1')
        df = df[['v1', 'v2']]
        df.columns = ['label', 'message']
        return df
    except Exception as e:
        st.error(f"Error loading the dataset: {e}")
        return None

def show_wordclouds(df):
    """Generates and displays word clouds for ham and spam messages."""
    st.subheader("Most Common Words")

    # Separate ham and spam messages
    ham_text = " ".join(df[df['label'] == 'ham']['message'])
    spam_text = " ".join(df[df['label'] == 'spam']['message'])

    # Create two columns for side-by-side word clouds
    col1, col2 = st.columns(2)

    with col1:
        st.text("Ham (Not Spam)")
        wordcloud_ham = WordCloud(width=400, height=200, background_color='white').generate(ham_text)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud_ham, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)

    with col2:
        st.text("Spam")
        wordcloud_spam = WordCloud(width=400, height=200, background_color='white').generate(spam_text)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud_spam, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)


st.title('Spam Classifier')

# Load the model
model = load_model(MODEL_PATH)

if model is None:
    st.warning("**Model not found.** Please train the model first.")
    st.info("To train the model, run the following command in your terminal:\n\n"
            "1. Make sure you have the `spam.csv` dataset in the root directory.\n"
            "2. Run the script: `python spam_classifier.py`")
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

    st.markdown("---")
    # Add a checkbox for showing visualizations
    show_visuals = st.checkbox("Show Data Visualizations")

    if show_visuals:
        df = load_data(DATA_PATH)
        if df is not None:
            show_wordclouds(df)
        else:
            st.warning(f"**Dataset not found.** Please make sure `spam.csv` is in the root directory.")
