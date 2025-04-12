# app/calculadora.py
"""
Calculator module that provides basic mathematical operations.

This module implements the core mathematical operations used by the calculator web application.
All functions accept two numeric parameters and return the result of the operation.

Functions:
    sumar(a, b): Returns the sum of two numbers
    restar(a, b): Returns the difference between two numbers
    multiplicar(a, b): Returns the product of two numbers
    dividir(a, b): Returns the quotient of two numbers
"""

def sumar(a, b):
    """
    Add two numbers together.

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        float: The sum of a and b
    """
    return a + b


def restar(a, b):
    """
    Subtract the second number from the first.

    Args:
        a (float): Number to subtract from
        b (float): Number to subtract

    Returns:
        float: The difference between a and b
    """
    return a - b


def multiplicar(a, b):
    """
    Multiply two numbers together.

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        float: The product of a and b
    """
    return a * b


def dividir(a, b):
    """
    Divide the first number by the second.

    Args:
        a (float): Numerator
        b (float): Denominator

    Returns:
        float: The quotient of a divided by b

    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
