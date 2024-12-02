# ComputorV1

## Overview

`computorv1` is a Python program designed to solve polynomial equations of degree 0, 1, and 2. This program analyzes the input equation, simplifies it, and provides the solution(s) based on the polynomial's degree.

It implements mathematical and algorithmic principles to parse, process, and solve equations efficiently, handling various edge cases like invalid inputs, complex numbers, and trivial solutions.

---

## Features

- **Polynomial Parsing**: Supports input equations with polynomial terms, constants, and operations.
- **Equation Simplification**: Reduces the equation into its canonical form for easy computation.
- **Solution Calculation**:
  - **Degree 0**: Checks for valid equality.
  - **Degree 1**: Solves using the linear equation formula.
  - **Degree 2**: Implements the quadratic formula to calculate roots.
- **Complex Roots**: Handles and displays solutions involving complex numbers when the discriminant is negative.
- **Error Handling**: Provides meaningful error messages for invalid inputs or unsupported cases.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/lusehair/computorv1.git
   cd computorv1

   ```

2. Ensure you have Python 3.8+ installed.

## Usage

Run the program directly from the terminal:

## How It Works

### 1. **Input Parsing**

The program takes an input equation and breaks it into terms. Each term is analyzed for its coefficient and degree.

**Example**:
Input: `5 * X^2 + 3 * X - 2 = 0`
Parsed Form: `5X^2 + 3X - 2 = 0`

### 2. **Canonical Form**

The left-hand side of the equation is rearranged and simplified to:
\[ $ax^2$ + $bx$ + $c=0$ \]
Where \( a, b, c \) are constants.

**Example**:
Input: `5 * X^2 + 3 * X - 2 = 0`
Canonical Form: \( $5X^2$ + $3X$ - $2$ = $0$ \)

### 3. **Solution Computation**

The program computes solutions based on the polynomial's degree:

- **Degree 0**: Validates the equality (e.g., \( 3 = 3 \)).
- **Degree 1**: Solves using:
  \[
  X = $-\frac{c}{b}$
  \]
- **Degree 2**: Solves using the quadratic formula:

  <img src="https://latex.codecogs.com/svg.latex?\Large&space;\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}" title="\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" />
  
  - The **discriminant** (\( $\Delta$ = $b^2$ - $4 ac$ \)) determines the nature of roots:
    - \( $\Delta$ > 0 \): Two real solutions.
    - \( $\Delta$ = 0 \): One real solution.
    - \( $\Delta$ < 0 \): Two complex solutions.

### Example: Degree 2 Solution

For the equation \( 5X^2 + 3X - 2 = 0 \):

1. \( a = 5, b = 3, c = -2 \)
2. \( $\Delta$ = $b^2$ - $4ac$ = $9$ + $40$ = $49$ \)
3. Roots: 
    <img src="https://latex.codecogs.com/svg.latex?\Large&space; X_1 \frac{-3 + \sqrt{49}}{10}, \quad X_2  = \frac{-3 - \sqrt{49}}{10}" title="\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" />

4. Result : 
  $X_1 = 0.4, \quad X_2 = -1$



## Testing

To verify the correctness of `computorv1`, a comprehensive test suite is provided in `test.py`. This script includes a variety of test cases that cover different polynomial equations and edge cases.

### Running the Tests

Execute the test suite using the following command:

```bash
python3 test.py
```

By default, all tests will run. You can also specify which tests to run:

```bash
python3 test.py subject      # Runs subject tests
python3 test.py correction   # Runs correction tests
python3 test.py additional   # Runs additional tests
```

### Test Categories

- **Subject Tests**: Tests who comes from subject of this project. 
- **Correction Tests**: Tests asked during the correction. 
- **Additional Tests**: Extended tests including more complex and edge case scenarios.

### Features Tested

- **Degree 0 Equations**: Checks for equations with no variables.
- **Degree 1 Equations**: Solves linear equations.
- **Degree 2 Equations**: Handles quadratic equations with:
  - Positive discriminant (two real solutions)
  - Zero discriminant (one real solution)
  - Negative discriminant (two complex solutions)
- **Syntax Handling**: Detects and reports syntax errors.
- **Unsupported Degrees**: Ensures proper error messages for equations of degree higher than 2.

---

