# OpenSpec Project Overview

This project is a machine learning application for spam email classification, based on the work from "Hands-On Artificial Intelligence for Cybersecurity" by Packt Publishing. The goal is to expand upon the original project's preprocessing steps and add richer visualizations and a Streamlit-based interactive demo.

## Technology Stack
- Language: Python
- Core Libraries:
  - scikit-learn: For machine learning algorithms.
  - pandas: For data manipulation and analysis.
  - numpy: For numerical operations.
- Visualization:
  - matplotlib: For creating static, animated, and interactive visualizations.
- Web Framework:
  - streamlit: For building and sharing the interactive web app.

## Project Structure
```
├── app.py                          # Main Streamlit application
├── simple_linear_regression.py     # Script for command-line regression analysis
├── requirements.txt                # Python dependencies
├── OpenSpec/                       # OpenSpec files for project management
│   └── openspec/
│       ├── project.md              # This file
│       └── ...
└── ...
```

## Conventions
- The project follows the CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology.
- Code should be well-commented, especially the machine learning pipeline.
- Use f-strings for string formatting.
- Type hinting is encouraged for new functions.

## Error Handling
- For the Streamlit app, present errors and warnings to the user in a clear and informative way using `st.error` and `st.warning`.
- For scripts, use try-except blocks to catch exceptions and provide meaningful error messages.

## Logging
- For the Streamlit app, use `st.write` or `st.info` for logging information to the user.
- For scripts, use the `print` function for logging progress and results.

## Testing Strategy
- Manual testing of the Streamlit application by interacting with the UI.
- The command-line script `simple_linear_regression.py` can be used for testing the core regression logic.
- As the project grows, unit tests using `pytest` should be added for data processing and model training functions.

## Development Workflow
- Install dependencies from `requirements.txt` using `pip install -r requirements.txt`.
- Run the Streamlit app using `streamlit run app.py`.
- Run the command-line script using `python simple_linear_regression.py`.
- Follow the OpenSpec workflow for proposing and implementing changes.
