## 1. Code Cleanup
- [x] 1.1 Delete the `simple_linear_regression.py` file.
- [x] 1.2 Remove all linear regression logic from `app.py`.

## 2. Spam Classification UI
- [x] 2.1 In `app.py`, create a title for the Spam Classifier.
- [x] 2.2 Add a `st.text_area` for user input.
- [x] 2.3 Add a button to trigger the classification.
- [x] 2.4 Add a placeholder to display the result.

## 3. Machine Learning Backend
- [x] 3.1 Create a new file `spam_classifier.py`.
- [x] 3.2 In `spam_classifier.py`, implement a function to load a dataset (e.g., from a local CSV file).
- [x] 3.3 Implement a function for text preprocessing (e.g., using `TfidfVectorizer`).
- [x] 3.4 Implement a function to train a simple classification model (e.g., `MultinomialNB`).
- [x] 3.5 Create a main function that orchestrates the loading, preprocessing, and training, and returns a trained model/pipeline.

## 4. Integration
- [x] 4.1 In `app.py`, import the functions from `spam_classifier.py`.
- [x] 4.2 Load the trained model when the app starts.
- [x] 4.3 When the button is clicked, use the model to predict the class of the input text and display the result.

## 5. Documentation
- [x] 5.1 Update the `README.md` if necessary to reflect the new application structure.