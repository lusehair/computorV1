import sys


def get_degree(polynom):
    degree = int(polynom.strip().split(" ")[-1][-1])
    return degree


def get_values(polynom, degree):
    value = 0
    data = polynom.strip().split(" ")
    coeff = [0] * (degree + 1)
    for i, arg in enumerate(data):
        if arg[0].isdigit():
            if i >= 1 and data[i - 1] == "-":
                value = float(data[i]) * (-1)
            else:
                value = float(data[i])
            degree = (
                int(data[i + 2][-1])
                if ((i + 2) < len(data) and data[i + 2][0] == "X")
                else 0
            )
            coeff[degree] = value
    return coeff


def format_polynom(coeffs):
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


def is_greater_than_two(eq):
    if len(eq) > 3:
        for value in eq[3:]:
            if value != float(0):
                return 1
        eq = eq[:3]
    return 0


def get_discriminant(eq):
    discr = eq[1] * eq[1] - 4 * eq[0] * eq[2]
    return discr


def print_floats(flt):
    if flt - int(flt) == 0:
        flt = int(flt)
    else:
        flt = float("{0:.2f}".format(flt))
    return flt


def format_output(flt):
    if flt - int(flt) == 0:
        flt = int(flt)
    else:
        flt = float("{0:.6f}".format(flt))
    return flt


def list_sub(arr1, arr2):
    values = []
    for i, val in enumerate(arr1):
        if i < len(arr1) and i < len(arr2):
            values.append(print_floats(val - arr2[i]))
    return values


def reduce(eq):
    i = -1
    while len(eq) > 1:
        if eq[i] == 0:
            del eq[-1]
        else:
            break
    print("Reduced form:", format_polynom(eq))
    return len(eq) - 1


def solve(eq, degree):
    if is_greater_than_two(eq):
        print("The polynomial degree is stricly greater than 2, I can't solve.")
        return 1
    print("Polynomial degree: ", degree)
    if degree == 0:
        if eq[0] == 0:
            print("All real numbers are solutions")
            return 0
        else:
            print("This equation has no solution")
            return 1
    elif degree == 1:
        print("The solution is:\n", format_output(-eq[0] / eq[1]))
        return 0
    discr = get_discriminant(eq)
    if discr >= 0:
        sqrt = discr**0.5
    else:
        sqrt = ((-1) * discr) ** 0.5
    if discr > 0:
        print("Discriminant is strictly positive, the two solutions are:")
        print(format_output((-eq[1] - sqrt) / (2 * eq[2])))
        print(format_output((-eq[1] + sqrt) / (2 * eq[2])))
    elif discr == 0:
        print("The solution is:")
        print((-eq[1] / (2 * eq[2])))
    else:
        print("Discriminant is strictly negative, the two solutions are:")
        eq[1] = -eq[1] / (2 * eq[2])
        sqrt = sqrt / (2 * eq[2])
        b = str(format_output(eq[1]))
        sol = " i * " + str(format_output(sqrt))
        if eq[1] != 0:
            sol1 = b + " -" + sol
            sol2 = b + " +" + sol
        else:
            sol1 = " -" + sol
            sol2 = sol
        print(sol1)
        print(sol2)


def ComputorV1():
    if len(sys.argv) != 2:
        return 1
    equation = sys.argv[1]
    sides = equation.strip().split("=")
    degree = max(get_degree(sides[0]), get_degree(sides[1]))
    eq = get_values(sides[0], degree)
    if sides[1].strip() != str(0):
        eq = list_sub(get_values(sides[0], degree), get_values(sides[1], degree))
    degree = reduce(eq)
    solve(eq, degree)


if __name__ == "__main__":
    ComputorV1()
