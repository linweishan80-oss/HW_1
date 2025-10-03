import streamlit as st
import numpy as np
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
    # 1. Data Preparation
    st.header("1. Data and Model")
    np.random.seed(42) # for reproducibility
    X = np.random.rand(num_points, 1) * 10
    true_y = a * X + b
    y = true_y + np.random.randn(num_points, 1) * noise

    # 2. Modeling
    model = LinearRegression()
    model.fit(X, y)

    # 3. Evaluation
    y_pred = model.predict(X)
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


    # 4. Deployment (Visualization)
    st.header("2. Visualization")
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