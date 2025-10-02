# Deploying on Replit

This document provides instructions on how to deploy this simple linear regression project on Replit.

## Steps

1.  **Create a new Repl:**
    *   Go to [Replit](https://replit.com/).
    *   Click the "+" button to create a new Repl.
    *   Select the "Python" template.

2.  **Upload the files:**
    *   Upload the following files to your Repl:
        *   `simple_linear_regression.py`

3.  **Install Dependencies:**
    *   Replit's package manager should automatically detect the `import` statements and prompt you to install the required libraries (`matplotlib`, `scikit-learn`, `numpy`). If not, you can open the "Shell" tab and run:
    ```bash
    pip install matplotlib scikit-learn numpy
    ```

4.  **Run the Script:**
    *   Click the "Run" button at the top of the screen.
    *   This will execute the `simple_linear_regression.py` script.

5.  **View the Output:**
    *   The script will generate a file named `linear_regression_plot.png`.
    *   You can view this image directly in the Replit file explorer.

## Serving the Image (Optional)

If you want to share the output as a webpage, you can create a simple web server.

1.  **Create a `main.py` file:**
    *   If you don't have one, rename your `simple_linear_regression.py` to `main.py` or create a new `main.py`.

2.  **Add a web server:**
    *   Create a new file named `server.py` and add the following code:
    ```python
    from http.server import SimpleHTTPRequestHandler, HTTPServer

    def run_server():
        server_address = ('', 8080)
        httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
        print("Server started at localhost:8080")
        httpd.serve_forever()

    if __name__ == "__main__":
        run_server()
    ```

3.  **Modify `main.py`:**
    *   At the end of your `main.py` (or `simple_linear_regression.py`), add a call to run the web server after generating the plot. You'll need to import the `run_server` function.

This is a more advanced setup, but it allows you to share your results via a public URL that Replit provides for web-facing Repls.