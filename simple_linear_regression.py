import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def run_regression_analysis():
    """
    Runs a simple linear regression analysis based on user-defined parameters,
    following the CRISP-DM methodology.
    """

    # --- Parameters to Modify ---
    # You can change these values to see how they affect the regression.
    a = 2.5          # The slope of the true line
    noise = 15       # The amount of noise to add
    num_points = 100 # The number of data points
    b = 10           # The intercept of the true line (kept constant for simplicity)
    # --------------------------

    # 1. Business Understanding
    print("--- CRISP-DM Step 1: Business Understanding ---")
    print("Goal: To understand the relationship between an independent variable (x) and a dependent variable (y).")
    print("Objective: Build a simple linear regression model (y = ax + b) and evaluate its performance.")
    print("Success Criteria: The model should accurately estimate the underlying relationship from noisy data.\n")


    print("\nParameters:")
    print(f"  - True slope (a): {a}")
    print(f"  - True intercept (b): {b}")
    print(f"  - Noise level: {noise}")
    print(f"  - Number of points: {num_points}\n")


    # 2. Data Understanding
    print("--- CRISP-DM Step 2: Data Understanding ---")
    print("We will generate synthetic data based on your parameters.")
    print("The data will follow the model: y = ax + b + noise.\n")

    # 3. Data Preparation
    print("--- CRISP-DM Step 3: Data Preparation ---")
    print("Generating the dataset...\n")
    np.random.seed(42) # for reproducibility
    X = np.random.rand(num_points, 1) * 10
    true_y = a * X + b
    y = true_y + np.random.randn(num_points, 1) * noise

    # 4. Modeling
    print("--- CRISP-DM Step 4: Modeling ---")
    print("Training a simple linear regression model...\n")
    model = LinearRegression()
    model.fit(X, y)

    # 5. Evaluation
    print("--- CRISP-DM Step 5: Evaluation ---")
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    print("Model Evaluation Results:")
    print(f"  - True slope (a): {a}")
    print(f"  - Estimated slope (a'): {model.coef_[0][0]:.4f}")
    print(f"  - True intercept (b): {b}")
    print(f"  - Estimated intercept (b'): {model.intercept_[0]:.4f}")
    print(f"  - Mean Squared Error (MSE): {mse:.4f}")
    print(f"  - R-squared: {r2:.4f}\n")

    # 6. Deployment (Visualization)
    print("--- CRISP-DM Step 6: Deployment (Visualization) ---")
    print("Displaying the results visually.")

    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, color='blue', label='Noisy Data Points')
    plt.plot(X, true_y, color='green', linewidth=2, label=f'True Line (y = {a}x + {b})')
    plt.plot(X, y_pred, color='red', linewidth=2, label=f'Fitted Line (y = {model.coef_[0][0]:.2f}x + {model.intercept_[0]:.2f})')
    plt.title('Simple Linear Regression')
    plt.xlabel('Independent variable (X)')
    plt.ylabel('Dependent variable (y)')
    plt.legend()
    plt.grid(True)
    plt.savefig('linear_regression_plot.png')
    print("Plot saved to linear_regression_plot.png")


if __name__ == '__main__':
    run_regression_analysis()
