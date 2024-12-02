#!/usr/bin/python3
import re
import sys


def format_equation(equation):
    """
    Takes a string representing an equation, removes unnecessary spaces,
    multiplication signs '*', and adds '+' signs before '-', except those that are part of exponents.
    """
    # Convert the equation to lowercase for uniformity
    equation = equation.lower()
    # Remove spaces
    equation = equation.replace(" ", "")
    # Remove multiplication signs '*'
    equation = equation.replace("*", "")
    # Replace '-' with '+-' only if '-' is not preceded by '^'
    equation = re.sub(r"(?<!\^)-", "+-", equation)
    return equation


def check_exponent(equation):
    """Checks if there are any invalid exponents in the equation."""
    exponents = re.findall(r"x\^([-]?\d+\.?\d*)", equation)
    for exp in exponents:
        if not exp.replace(".", "", 1).lstrip("-").isdigit():
            print(f"Error: Invalid exponent '{exp}' detected.")
            sys.exit(1)
        exp_value = float(exp)
        if not exp_value.is_integer():
            print(f"Error: Invalid floating-point exponent '{exp}' detected.")
            sys.exit(1)
        exp_value = int(exp_value)
        if exp_value < 0:
            print(f"Error: Negative exponent '{exp_value}' detected.")
            sys.exit(1)


def get_degree(polynomial):
    """Determines the degree of the polynomial."""
    exponents = re.findall(r"x\^(\d+)", polynomial)
    degrees = [int(exp) for exp in exponents]
    if degrees:
        return max(degrees)
    elif "x" in polynomial:
        return 1
    else:
        return 0


def get_values(polynomial, degree):
    """Extracts the coefficients of the polynomial as a list."""
    coefficients = [0] * (degree + 1)
    # Split the terms using the '+' sign
    terms = polynomial.split("+")
    for term in terms:
        if not term:
            continue
        # Determine the sign of the term
        sign = 1
        if term.startswith("-"):
            sign = -1
            term = term[1:]
        # Process terms with 'x'
        if "x" in term:
            if "^" in term:
                coef_part, exp_part = term.split("x^")
                exp = int(exp_part)
            else:
                coef_part = term.split("x")[0]
                exp = 1
            # Handle the coefficient
            if coef_part == "":
                coef = 1.0
            else:
                try:
                    coef = float(coef_part)
                except ValueError:
                    print(f"Error: Invalid coefficient '{coef_part}' in term '{term}'")
                    sys.exit(1)
            coef *= sign
            coefficients[exp] += coef
        else:
            # Process constant terms
            try:
                coef = float(term) * sign
                coefficients[0] += coef
            except ValueError:
                print(f"Error: Invalid constant term '{term}'")
                sys.exit(1)
    return coefficients


def list_sub(arr1, arr2):
    """Subtracts the coefficients of two polynomials."""
    max_len = max(len(arr1), len(arr2))
    arr1 += [0] * (max_len - len(arr1))
    arr2 += [0] * (max_len - len(arr2))
    result = [arr1[i] - arr2[i] for i in range(max_len)]
    # Remove unnecessary trailing zeros
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


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


def solve(eq, degree):
    """Solves the polynomial equation based on its degree."""
    print("Polynomial degree:", degree)  
    if degree > 2:
        print(
            "The polynomial degree is strictly greater than 2, I can't solve."
        )  
        return
    if degree == 0:
        if eq[0] == 0:
            print("All real numbers are solutions.")  
        else:
            print(
                "This equation has no solution."
            )  
        return
    if degree == 1:
        solution = -eq[0] / eq[1]  # Calculate the solution for a linear equation
        print("The solution is:", format_output(solution))  
        return
    if degree == 2:
        a = eq[2]  # Coefficient of x^2
        b = eq[1]  # Coefficient of x
        c = eq[0]  # Constant term
        discriminant = b**2 - 4 * a * c  # Compute the discriminant
        print("Discriminant:", format_output(discriminant)) 
        if discriminant > 0:
            print(
                "Discriminant is strictly positive, the two solutions are:"
            ) 
            root = discriminant**0.5  # Calculate the square root of the discriminant
            solution1 = (-b + root) / (2 * a)  # First solution
            solution2 = (-b - root) / (2 * a)  # Second solution
            print(format_output(solution1))  
            print(format_output(solution2))  
        elif discriminant == 0:
            solution = -b / (2 * a)  
            print(
                "Discriminant is zero, the solution is:"
            )  
            print(format_output(solution))  
        else:
            print(
                "Discriminant is strictly negative, the two complex solutions are:"
            ) 
            real_part = -b / (2 * a)  # Real part of the complex solutions
            imaginary_part = (-discriminant) ** 0.5 / (
                2 * a
            )  # Imaginary part of the complex solutions
            print(
                f"{format_output(real_part)} - i * {format_output(imaginary_part)}"
            )  
            print(
                f"{format_output(real_part)} + i * {format_output(imaginary_part)}"
            )
        return


def format_output(flt):
    """Format a floating-point number."""
    if flt - int(flt) == 0:
        flt = int(flt)
    else:
        flt = float("{0:.6f}".format(flt))
    return flt


def ComputorV1(equation):
    """Main function to solve the polynomial equation."""
    equation = format_equation(equation)
    check_exponent(equation)
    sides = equation.split("=")
    if len(sides) != 2:
        print(
            "Invalid equation format. Please use the format: '<polynomial> = <polynomial>'"
        )
        return
    degree = max(get_degree(sides[0]), get_degree(sides[1]))
    eq_left = get_values(sides[0], degree)
    eq_right = get_values(sides[1], degree)
    eq = list_sub(eq_left, eq_right)
    print("Reduced form:", format_polynom(eq))
    degree = len(eq) - 1
    solve(eq, degree)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python computorv1.py '<equation>'")
    else:
        ComputorV1(sys.argv[1])
