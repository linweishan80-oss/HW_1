import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

st.title('Simple Linear Regression Analysis')

# --- Parameters in Sidebar ---
st.sidebar.header('Model Parameters')
a = st.sidebar.number_input('True Slope (a)', value=2.5, step=0.1)
noise = st.sidebar.number_input('Noise Level', value=15.0, step=1.0)
num_points = st.sidebar.number_input('Number of Points', value=100, min_value=10, max_value=1000, step=10)
b = 10  # The intercept of the true line (kept constant for simplicity)

st.sidebar.markdown("---")
run_button = st.sidebar.button('Run Analysis')

# --- Main panel ---
st.write("Adjust the parameters in the sidebar and click 'Run Analysis' to generate a new regression model.")

if run_button:
    # --- 1. Business Understanding ---
    st.header("CRISP-DM: 1. Business Understanding")
    st.markdown("""
    - **Goal:** To understand the relationship between an independent variable (X) and a dependent variable (y).
    - **Objective:** Interactively build a simple linear regression model (y = ax + b) and evaluate its performance based on user-defined parameters.
    - **Success Criteria:** The model should accurately estimate the underlying relationship from noisy data.
    """)

    # --- 2. Data Understanding & 3. Data Preparation ---
    st.header("CRISP-DM: 2. Data Understanding & 3. Data Preparation")
    st.markdown("Generating synthetic data based on the parameters you provided in the sidebar.")
    np.random.seed(42) # for reproducibility
    X = np.random.rand(num_points, 1) * 10
    true_y = a * X + b
    y = true_y + np.random.randn(num_points, 1) * noise
    
    st.subheader("Generated Data Sample")
    df_sample = pd.DataFrame({'X': X.flatten(), 'Generated Y (with noise)': y.flatten()})
    st.dataframe(df_sample.head())


    # --- 4. Modeling ---
    st.header("CRISP-DM: 4. Modeling")
    st.markdown("Training a simple linear regression model using the generated data.")
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    # --- 5. Evaluation ---
    st.header("CRISP-DM: 5. Evaluation")
    st.markdown("Evaluating the model's performance by comparing the predicted values against the actual values.")
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    st.subheader("Evaluation Metrics")
    col1, col2 = st.columns(2)
    col1.metric("Mean Squared Error (MSE)", f"{mse:.4f}")
    col2.metric("R-squared", f"{r2:.4f}")

    st.subheader("Model Coefficients")
    col1, col2 = st.columns(2)
    col1.metric("Estimated Slope (a')", f"{model.coef_[0][0]:.4f}", f"{model.coef_[0][0] - a:.4f}")
    col2.metric("Estimated Intercept (b')", f"{model.intercept_[0]:.4f}", f"{model.intercept_[0] - b:.4f}")


    # --- 6. Deployment (Visualization) ---
    st.header("CRISP-DM: 6. Deployment")
    st.markdown("Visualizing the results, including the original noisy data, the true underlying relationship, and the fitted regression line.")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(X, y, color='blue', label='Noisy Data Points')
    ax.plot(X, true_y, color='green', linewidth=2, label=f'True Line (y = {a}x + {b})')
    ax.plot(X, y_pred, color='red', linewidth=2, label=f'Fitted Line (y = {model.coef_[0][0]:.2f}x + {model.intercept_[0]:.2f})')
    ax.set_title('Simple Linear Regression')
    ax.set_xlabel('Independent variable (X)')
    ax.set_ylabel('Dependent variable (y)')
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)