from flask import Flask, request, render_template_string
import numpy as np
import matplotlib
matplotlib.use('Agg') # Use a non-interactive backend
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import io
import base64

app = Flask(__name__)

# HTML template for the form and results
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Linear Regression</title>
    <style>
        body { font-family: sans-serif; margin: 2em; }
        .container { max-width: 800px; margin: auto; }
        .form-group { margin-bottom: 1em; }
        label { display: block; margin-bottom: 0.5em; }
        input { width: 100%; padding: 0.5em; box-sizing: border-box; }
        button { padding: 0.7em 1.5em; background-color: #007bff; color: white; border: none; cursor: pointer; }
        .results { margin-top: 2em; }
        img { max-width: 100%; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Simple Linear Regression Analysis</h1>
        <form action="/run" method="post">
            <div class="form-group">
                <label for="a">True Slope (a)</label>
                <input type="number" step="any" id="a" name="a" value="{{ params.get('a', 2.5) }}">
            </div>
            <div class="form-group">
                <label for="noise">Noise Level</label>
                <input type="number" step="any" id="noise" name="noise" value="{{ params.get('noise', 15) }}">
            </div>
            <div class="form-group">
                <label for="num_points">Number of Points</label>
                <input type="number" id="num_points" name="num_points" value="{{ params.get('num_points', 100) }}">
            </div>
            <button type="submit">Run Analysis</button>
        </form>

        {% if results %}
        <div class="results">
            <h2>Results</h2>
            <p><strong>True Slope (a):</strong> {{ results.true_slope }}</p>
            <p><strong>Estimated Slope (a''):</strong> {{ "%.4f"|format(results.estimated_slope) }}</p>
            <p><strong>True Intercept (b):</strong> {{ results.true_intercept }}</p>
            <p><strong>Estimated Intercept (b''):</strong> {{ "%.4f"|format(results.estimated_intercept) }}</p>
            <p><strong>Mean Squared Error (MSE):</strong> {{ "%.4f"|format(results.mse) }}</p>
            <p><strong>R-squared:</strong> {{ "%.4f"|format(results.r2) }}</p>
            <img src="data:image/png;base64,{{ results.plot_url }}" alt="Regression Plot">
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    """Displays the initial form."""
    return render_template_string(HTML_TEMPLATE, params={})

@app.route('/run', methods=['POST'])
def run_analysis():
    """Runs the regression analysis based on form input and displays the results."""
    # --- Get Parameters from Form ---
    try:
        a = float(request.form.get('a', 2.5))
        noise = float(request.form.get('noise', 15))
        num_points = int(request.form.get('num_points', 100))
        b = 10  # Kept constant for simplicity
    except (ValueError, TypeError):
        return "Invalid input. Please provide valid numbers.", 400

    params = {'a': a, 'noise': noise, 'num_points': num_points}

    # --- Data Preparation ---
    np.random.seed(42)  # for reproducibility
    X = np.random.rand(num_points, 1) * 10
    true_y = a * X + b
    y = true_y + np.random.randn(num_points, 1) * noise

    # --- Modeling ---
    model = LinearRegression()
    model.fit(X, y)

    # --- Evaluation ---
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    results = {
        "true_slope": a,
        "estimated_slope": model.coef_[0][0],
        "true_intercept": b,
        "estimated_intercept": model.intercept_[0],
        "mse": mse,
        "r2": r2,
    }

    # --- Visualization ---
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, color='blue', label='Noisy Data Points')
    plt.plot(X, true_y, color='green', linewidth=2, label=f'True Line (y = {a}x + {b})')
    plt.plot(X, y_pred, color='red', linewidth=2, label=f'Fitted Line (y = {model.coef_[0][0]:.2f}x + {model.intercept_[0]:.2f})')
    plt.title('Simple Linear Regression')
    plt.xlabel('Independent variable (X)')
    plt.ylabel('Dependent variable (y)')
    plt.legend()
    plt.grid(True)

    # Save plot to a memory buffer
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()

    results["plot_url"] = plot_url

    return render_template_string(HTML_TEMPLATE, results=results, params=params)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
