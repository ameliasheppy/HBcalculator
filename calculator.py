"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide,
                        square, cube, power, mod, )


# Replace this with your code
# we need to tokenize the list of info we get such as ['pow', '3', '5']
# tokenizing is just breaking it up into smaller chunks.
# if the first token is 'pow':
# call the power function with the other two tokens

# start the function off by the ability for the user to use the calculator forever if they want.

while True:
    user_input = input("Enter your equation > ")
    tokens = user_input.split(" ")

    if "q" in tokens:
        print("Exit")
        break
    # break with exit the while loop since the user is done

    elif len(tokens) < 2:
        print("That is not enough information")
        continue
        # contintue will go back to the input prompt
# the tokens are the user input, that is split into 3 tokens. The first token is the operator for the equation. tokens[0] = theperator because of zero indexing. so, if a user types "pow", that is token[0]/ then we split on the space between the operator and the numbers the user enters, so token[1]= num1, token[2] = num2.

    operator = tokens[0]
    num1 = int(tokens[1])

    if len(tokens) <= 2:
        num2 = None

    else:
        num2 = int(tokens[2])

    result = None

    # if num1.isalpha() or num2.isalpha():
    #     print("Those are letters, we need numbers for math! :)")
    #     continue

# + - * / square cube power mod
    if operator == "+":
        result = add(float(num1), float(num2))

    elif operator == "-":
        result = subtract(float(num1), float(num2))

    elif operator == "*":
        result = multiply(float(num1), float(num2))

    elif operator == "/":
        result = divide(float(num1), float(num2))

    elif operator == "square":
        result = square(float(num1))

    elif operator == "cube":
        result = cube(float(num1))

    elif operator == "power":
        result = power(float(num1), float(num2))

    elif operator == "mod":
        result = mod(float(num1), float(num2))
    else:
        result = "Please enter correct inputs"

    print(result)
