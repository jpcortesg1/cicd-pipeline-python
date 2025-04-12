"""
Main Flask application module that implements a web calculator.

This module provides a simple web interface for performing basic mathematical operations
such as addition, subtraction, multiplication, and division. It handles common errors
like division by zero and invalid inputs.

Functions:
    index(): Handles GET and POST requests for the main page.
"""
# app/app.py
from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Handles GET and POST requests for the calculator's main page.

    GET: Displays the calculator form.
    POST: Processes the selected mathematical operation with the provided numbers.

    Returns:
        str: Renders the index.html template with the operation result if it exists.
            In case of error, returns a descriptive error message.
    """
    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]

            if operacion == "sumar":
                resultado = sumar(num1, num2)
            elif operacion == "restar":
                resultado = restar(num1, num2)
            elif operacion == "multiplicar":
                resultado = multiplicar(num1, num2)
            elif operacion == "dividir":
                resultado = dividir(num1, num2)
            else:
                resultado = "Invalid operation"
        except ValueError:
            resultado = "Error: Please enter valid numbers"
        except ZeroDivisionError:
            resultado = "Error: Cannot divide by zero"

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":  # pragma: no cover
    app.run(
        debug=False, 
        port=5001, 
        host="0.0.0.0"
    )  # Remove debug=True for production
