first_number  = float(input("- Welcome to my python calculator! \n- It Will ask you for a number, an operator, and a second number. \n- Enter your first number to begin: "))
operator = input("Enter an operator (+, -, *, /): ")
second_number = float(input("Now, enter your second number: "))

if operator == "+":
    answer = first_number + second_number
elif operator == "-":
    answer = first_number - second_number
elif operator == "*":
    answer = first_number * second_number
elif operator == "/":
    answer = first_number / second_number

print(f"The answer is  + {round(answer, 5):,}")
