## OTHERS TESTS SOURCES ##
# https://github.com/jeremie-gauthier/ComputorV1/blob/master/computor/tests/results.json

# # Equation de 0 degree (any solution)
# "5 * X^0 = 5 * X^0"

# # Equation de 0 degree (no solution)
# "4 * X^0 = 8 * X^0"

# # Equation de 1 degree (one solution)
# "5 * X^0 = 4 * X^0 + 7 * X^1"

# # Equation de 2 degree :

# "5 * X^0 + 13 * X^1 + 3 * X^2 = 1 * X^0 + 1 * X^1"

# # Equation de 2 degree avec discriminant de 0
# "6 * X^0 + 11 * X^1 + 5 * X^2 = 1 * X^0 + 1 * X^1"

# # Equation de 2 degree avec discriminant strictement negatif


# "5 * X^0 + 3 * X^1 + 3 * X^2 = 1 * X^0 + 0 * X^1"

# #### SUBJECT TESTS ####


# # Degree 2, discriminant > 0, deux solutions
# "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"

# # Degre 1, une solution
# "5 * X^0 + 4 * X^1 = 4 * X^0"

# # Degre 3 (non gere), retourne une erreur
# "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"


from computorv1 import ComputorV1
import sys


def subject_test():
    print("***************************")
    print("***RUNNING SUBJECT TESTS***")
    print("***************************")
    print("\n\nTEST 00 : Degree 2, discriminant > 0, two solutions")
    ComputorV1("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
    print("\n\nTEST 01: Degree 1, one solution")
    ComputorV1("5 * X^0 + 4 * X^1 = 4 * X^0")
    print("\n\nTEST 02: Degree 3 (not handled), should return an error")
    ComputorV1("8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0")
    print("\n\n")


def correction_test():
    print("******************************")
    print("***RUNNING CORRECTION TESTS***")
    print("******************************")
    print("TEST 00 : Degree 0, any solution")
    ComputorV1("5 * X^0 = 5 * X^0")
    print("\n\nTEST 01 : Degree 0, no solution")
    ComputorV1("4 * X^0 = 8 * X^0")
    print("\n\nTEST 02 : Degree 2, discriminant > 0, two solutions")
    ComputorV1("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
    print("\n\nTEST 03 : Degree 2, discriminant = 0, one solution")
    ComputorV1("6 * X^0 + 11 * X^1 + 5 * X^2 = 1 * X^0 + 1 * X^1")
    print("\n\nTEST 04 : Degree 2, discriminant < 0, two complex solutions")
    ComputorV1("5 * X^0 + 3 * X^1 + 3 * X^2 = 1 * X^0 + 0 * X^1")
    print("\n\n")


def additional_test():
    print("******************************")
    print("***RUNNING ADDITIONAL TESTS***")
    print("******************************")

    print("\n\nTEST 00 : Degree 2, discriminant > 0, two solutions")
    ComputorV1("1 * X^2 + 1 * X^1 - 2 * X^0 = 0 * X^0")
    print("\n\nTEST 01 : Degree 2, discriminant > 0, two solutions")
    ComputorV1("1 * X^2 + 3 * X^1 + 2 * X^0 = 0 * X^0")
    print("\n\nTEST 02 : Degree 2, discriminant > 0, two complex solutions")
    ComputorV1("1 * X^2 + 1 * X^1 + 1 * X^0 = 0 * X^0")
    print("\n\nTEST 03 : Degree 2, discriminant = 0, one solution")
    ComputorV1("4 * X^2 + 4 * X^1 + 1 * X^0 = 0 * X^0")
    print("\n\nTEST 04 : Degree 2, discriminant < 0, two complex solutions")
    ComputorV1("-1 * X^2 + 2 * X^1 - 3 * X^0 = 0 * X^0")
    print("\n\nTEST 05 : Degree 2, discriminant > 0, two solutions")
    ComputorV1("1 * X^2 + 4 * X^1 = 0 * X^0")
    print("\n\nTEST 06 : Degree 0, no solution")
    ComputorV1("0 = 1")
    print("\n\nTEST 07 : Degree 0, any solution")
    ComputorV1("42 = 42")
    print("\n\nTEST 07 : Degree 0, any solution")
    ComputorV1("5 = 5.0")
    print("\n\n")


def main():
    args = sys.argv[1:]
    if not args or "all" in args:
        subject_test()
        correction_test()
        additional_test()
    else:
        if "subject" in args:
            subject_test()
        if "correction" in args:
            correction_test()
        if "additional" in args:
            additional_test()


if __name__ == "__main__":
    main()
