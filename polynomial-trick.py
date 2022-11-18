# Print instructions
print(
    "\nChoose a polynomial of any degree and choose positive integer coefficients for each power."
)
print("Positive integer coefficients could be any integer greater than or equal to 0.")
print("When prompted, enter the calculated values for your polynomial.")
print("This program will determine what your original polynomial was.\n")

# Have user enter f(1)
f1 = int(input("Enter the calculated value of f(1): "))
base = f1 + 1

# Ask user to enter f(f(1) + 1)
total = ff1 = int(input(f"Enter the calculated value of f({base}): "))

# Cycle through powers of f(1) + 1 until > f(f(1) + 1)
degree = 0
while ff1 > (base ** (degree + 1)):
    degree += 1

# f(f(1) + 1) // (f(1) + 1) ** # - 1 -> coefficient
# f(f(1) + 1) -= int * (f(1) + 1) ** # - 1 -> remainder
equation = "f(x) = "
for deg in reversed(range(0, degree + 1)):
    coef = total // base**deg
    total -= coef * base**deg
    if deg > 1:
        equation += f"{coef}x^{deg} + "
    elif deg > 0:
        equation += f"{coef}x + "
    else:
        equation += f"{coef}"

# Print out results
print(f"\nYour polynomial was of degree {degree}.")
print(f"Your polynomial was {equation}.")
