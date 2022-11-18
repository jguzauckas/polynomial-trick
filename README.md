This project is to display an algebra trick with polynomials. The premise of the trick is that if you have a person create a polynomial of any degree with all positive integer coefficients (greater than or equal to 0), then by having them provide two particular values from the function, we can determine their original function.

The two values the user needs to provide about their function are f(1) and f(f(1) + 1).

Each file has the following purpose:

- polynomial-builder.py - a python file that allows you to construct a polynomial by providing the coefficients and then will calculate the value of the polynomial given inputs you request. This makes it easier to calculate the values of larger polynomials for use with the file that applies the trick. This file does not share any information with the other files, so the trick is done with the correctly limited information.
- polynomial-trick.py - a python file that performs the trick. It asks the user to enter the two values (and dynamically asks for the second value based on the first one entered). It then calculates and formats the coefficients of their polynomial and prints out the result. Will work with any degree polynomial/size of coefficients, only limited by memory.
- polynomial-trick-proof.pdf - a scan of an algebraic proof of this trick working for all polynomials with positive integer coefficients.

Enjoy!
