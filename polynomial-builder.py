# Print instructions.
print("This tool is to help calculate values of a polynomial.")
print("First, we need to know the coefficients of your polynomial.")
print("For use with the trick in this repository, these should all")
print("be positive integer coefficients (that is, greater than or equal to 0).")
print("Start by entering your leading coefficient (with the highest power).")
print("Enter each consecutive coefficient moving to the right side of the")
print("equation until you have entered your constant. Then, you should")
print("enter the value '-1' to tell the program you are done entering")
print("coefficients, so that it can move forward.\n")

# Ask user for coefficients and save to list.
coefficients = []
input_coef = int(input("Enter a coefficient: "))
while input_coef >= 0:
    coefficients.append(input_coef)
    input_coef = int(input("Enter a coefficient: "))

# Build equation string.
equation = "f(x) = "
for n in reversed(range(0, len(coefficients))):
    i = len(coefficients) - n - 1
    if n > 1:
        equation += f"{coefficients[i]}x^{n} + "
    elif n > 0:
        equation += f"{coefficients[i]}x + "
    else:
        equation += f"{coefficients[i]}"

# Print out equation and degree to check with user.
print(f"\nYour equation is {equation}")
degree = len(coefficients) - 1
print(f"You have a polynomial of degree {degree}")

# Function to calculate value of function given input
def function_value(x: int) -> int:
    sum = 0
    for n in range(0, degree + 1):
        sum += coefficients[degree - n] * x**n
    return sum


# Ask user for values they want inputted and provide answers,
# until they stop.
print("Now you can enter numbers to input into the function. When you are")
print("done, you can enter '-1' to end the program.")
input_input = int(input("\nEnter a number to input into your function: "))
while input_input >= 0:
    print(f"f({input_input}) = {function_value(input_input)}")
    input_input = int(input("\nEnter a number to input into your function: "))
