#!/usr/bin/python3

# Ressources: https://www.methodemaths.fr/polynome_second_degre/

import sys
import re


def get_degree(polynom):
    """
    Extracts the degree of a polynomial from its string representation.

    Args:
        polynom (str): A string representation of the polynomial.

    Returns:
        int: The degree of the polynomial.
    """
    # Remove leading and trailing whitespace from the polynomial string
    cleaned_polynom = polynom.strip()
    # Split the polynomial string into individual terms based on spaces
    terms = cleaned_polynom.split(" ")
    # Initialize the degree of the polynomial to zero
    degree = 0
    # Iterate over each term in the polynomial
    for term in terms:
        # Check if the term contains a variable with an exponent (e.g., 'X^2')
        if "X^" in term:
            # Split the term to isolate the exponent part
            parts = term.split("X^")
            # Make sure the exponent part exists
            if len(parts) > 1:
                # Convert the exponent part to an integer
                term_degree = int(parts[1])
                # Update the degree if this term's degree is higher
                if term_degree > degree:
                    degree = term_degree
        # Check if the term is a linear term (e.g., 'X')
        elif "X" in term and "^" not in term:
            # The degree of a linear term is 1
            term_degree = 1
            if term_degree > degree:
                degree = term_degree
        # Else, the term is a constant term (degree 0), so no need to update
    # Return the highest degree found in the polynomial
    return degree


def get_values(polynom, degree):
    """
    Parses a polynomial string and extracts the coefficients for each term up to the given degree.

    Args:
        polynom (str): The polynomial string to parse. Terms should be separated by spaces.
                       Example: "3 X^2 - 4 X + 5"
        degree (int): The highest degree of the polynomial.

    Returns:
        list: A list of coefficients where the index represents the degree of the term.
              Example: For "3 X^2 - 4 X + 5", the return value would be [5, -4, 3]
              representing 5 (constant term), -4 (coefficient of X), and 3 (coefficient of X^2).
    """
    # Initialize a list of zeros where each index represents the degree of X
    coeffs = [0] * (degree + 1)
    # Split the polynomial string into tokens separated by spaces
    tokens = polynom.strip().split(" ")
    # Initialize the index to loop through tokens
    i = 0
    while i < len(tokens):
        token = tokens[i]
        # Check if the token is a numerical coefficient
        if token.replace(".", "", 1).isdigit():
            # Determine the sign of the coefficient
            sign = -1 if i > 0 and tokens[i - 1] == "-" else 1
            # Convert the token to a float and apply the sign
            value = float(token) * sign
            i += 1
            # Skip the '*' operator if present
            if i < len(tokens) and tokens[i] == "*":
                i += 1
            # Check if the next token represents a variable term
            if i < len(tokens) and tokens[i].startswith("X"):
                # Handle 'X^n' where n is the exponent
                if tokens[i].startswith("X^"):
                    exponent = int(tokens[i][2:])
                # Handle 'X' which implies an exponent of 1
                elif tokens[i] == "X":
                    exponent = 1
                else:
                    exponent = 0
                # Assign the coefficient to the corresponding exponent index
                coeffs[exponent] = value
                i += 1
            else:
                # If there's no variable, it's a constant term (exponent 0)
                coeffs[0] = value
        else:
            # Move to the next token if the current one isn't a digit
            i += 1
    # Return the list of coefficients
    return coeffs


def format_polynom(coeffs):
    """
    Formats a list of polynomial coefficients into a human-readable polynomial string.

    Args:
        coeffs (list of int or float): List of coefficients for the polynomial, where the index represents the power of X.

    Returns:
        str: A string representation of the polynomial in the form "a_n * X^n + ... + a_1 * X^1 + a_0 * X^0 = 0".
    """
    polynom = ""
    for i, val in enumerate(coeffs):
        if val < 0:
            polynom += " - "
            val *= -1
        elif val >= 0 and i > 0:
            polynom += " + "
            if val == 0:
                val = int(val)
        polynom += str(val) + " * X^" + str(i)
    return polynom + " = 0"


def print_floats(flt):
    """
    Formats a floating-point number to either an integer if it has no decimal part,
    or to a float with up to two decimal places if it does.

    Args:
        flt (float): The floating-point number to format.

    Returns:
        int or float: The formatted number, either as an integer or a float with up to two decimal places.
    """
    # Check if the float has no decimal part
    if flt % 1 == 0:
        # Return the integer part
        return int(flt)
    else:
        # Round the float to two decimal places
        return round(flt, 2)


def format_output(flt):
    """
    Formats a floating-point number to either an integer if it has no decimal part,
    or to a float with up to six decimal places if it does.

    Args:
        flt (float): The floating-point number to format.

    Returns:
        int or float: The formatted number, either as an integer or a float with up to six decimal places.
    """
    if flt - int(flt) == 0:
        flt = int(flt)
    else:
        flt = float("{0:.6f}".format(flt))
    return flt


def list_sub(arr1, arr2):
    """
    Subtracts corresponding elements of two lists and returns a new list with the results.

    Args:
        arr1 (list of float): The first list of floating-point numbers.
        arr2 (list of float): The second list of floating-point numbers.

    Returns:
        list of float: A list containing the differences between corresponding elements of arr1 and arr2.

    Note:
        The function assumes that both lists are of the same length. If arr2 is shorter than arr1,
        the function will only process up to the length of arr2.
    """
    values = []
    for i, val in enumerate(arr1):
        if i < len(arr1) and i < len(arr2):
            values.append(print_floats(val - arr2[i]))
    return values


def solve(eq, degree):
    """
    Solves a polynomial equation of degree 0, 1, or 2.

    Parameters:
    eq (list): Coefficients of the polynomial equation in ascending order of power.
    degree (int): The degree of the polynomial equation.

    Returns:
    int: 0 if the equation is solved, 1 if the degree is greater than 2 and cannot be solved.

    Prints:
    - The polynomial degree.
    - The solution(s) of the equation or a message if the equation has no solution or all real numbers are solutions.
    - If the degree is greater than 2, prints a message indicating it cannot solve the equation.
    """
    # Print the degree of the polynomial
    print("Polynomial degree:", degree)
    # Check if the degree is greater than two
    if degree > 2:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
        return 1

    # Handle degree 0 equations
    if degree == 0:
        if eq[0] == 0:
            print("All real numbers are solutions")
        else:
            print("This equation has no solution")
        return 0

    # Handle degree 1 equations (linear equations)
    if degree == 1:
        solution = -eq[0] / eq[1]
        print("The solution is:", format_output(solution))
        return 0

    # Handle degree 2 equations (quadratic equations)
    # Calculate the discriminant
    a = eq[2]  # Coefficient of X^2
    b = eq[1]  # Coefficient of X^1
    c = eq[0]  # Constant term

    # Calculate the discriminant using the formula: discr = b^2 - 4ac
    discr = (b**2) - (4 * a * c)
    print("Discriminant:", format_output(discr))

    # Calculate the square root of the discriminant
    if discr >= 0:
        sqrt_discr = discr**0.5
    else:
        sqrt_discr = (-discr) ** 0.5

    # Find the solutions based on the discriminant
    if discr > 0:
        print("Discriminant is strictly positive, the two solutions are:")
        solution1 = (-eq[1] - sqrt_discr) / (2 * eq[2])
        solution2 = (-eq[1] + sqrt_discr) / (2 * eq[2])
        print(format_output(solution1))
        print(format_output(solution2))
    elif discr == 0:
        print("Discriminant is zero, the solution is:")
        solution = -eq[1] / (2 * eq[2])
        print(format_output(solution))
    else:
        print("Discriminant is strictly negative, the two complex solutions are:")
        real_part = -eq[1] / (2 * eq[2])
        imaginary_part = sqrt_discr / (2 * eq[2])
        print(f"{format_output(real_part)} - i * {format_output(imaginary_part)}")
        print(f"{format_output(real_part)} + i * {format_output(imaginary_part)}")


def format_equation(equation):
    """
    Takes an equation string, removes double spaces, and adds spaces between numbers and operators (+, -, *) if they are missing.

    Args:
        equation (str): The input equation as a string.

    Returns:
        str: The formatted equation string.
    """
    # Remove double spaces
    equation = " ".join(equation.strip().split())
    # Add spaces between numbers and operators if not present
    equation = re.sub(r"(\d)([+\-*])", r"\1 \2", equation)
    equation = re.sub(r"([+\-*])(\d)", r"\1 \2", equation)
    # Clean up any extra spaces
    equation = " ".join(equation.strip().split())
    return equation


def check_expontent(equation):
    """
    Checks if any exponents in the equation are greater than 2, less than 0,
    or if any exponents are floats.

    Args:
        equation (str): The polynomial equation as a string.

    Returns:
        None: Exits the program if an invalid exponent is found.
    """
    exponents = re.findall(r"X\^([-]?\d+\.?\d*)", equation)
    for exp in exponents:
        exp_value = float(exp)
        if not exp_value.is_integer():
            print(f"Invalid float exponent {exp} detected.")
            sys.exit(1)
        exp_value = int(exp_value)
        if exp_value < 0:
            print(f"Invalid exponent {exp_value} detected.")
            sys.exit(1)


def ComputorV1(equation):
    # check_expontent(equation)
    sides = equation.strip().split("=")

    if len(sides) != 2:
        print(
            "Invalid equation format. Please use the format: '<polynomial> = <polynomial>'"
        )
        return 1

    degree = max(get_degree(sides[0]), get_degree(sides[1]))
    eq_left = get_values(sides[0], degree)
    eq_right = get_values(sides[1], degree)
    print(eq_left)
    print(eq_right)
    eq = list_sub(eq_left, eq_right)
    # print(eq)
    i = -1
    while len(eq) > 1:
        if eq[i] == 0:
            del eq[-1]
        else:
            break
    print("Reduced form:", format_polynom(eq))
    degree = len(eq) - 1
    solve(eq, degree)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python computorv1.py '<equation>'")
    else:
        equation = format_equation(sys.argv[1])
        ComputorV1(equation)
