coefficients = []
input_coef = int(input("Enter a coefficient: "))
while input_coef >= 0:
    coefficients.append(input_coef)
    input_coef = int(input("Enter a coefficient: "))

print(f"Your coefficients are {coefficients}")
degree = len(coefficients) - 1
print(f"You have a polynomial of degree {degree}")


def function_value(x: int) -> int:
    sum = 0
    for n in range(0, degree + 1):
        sum += coefficients[degree - n] * x**n
    return sum


input_input = int(input("Enter a number to input into your function: "))
while input_input >= 0:
    print(f"f({input_input}) = {function_value(input_input)}")
    input_input = int(input("Enter a number to input into your function: "))
