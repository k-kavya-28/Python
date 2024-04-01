number = int(input("Enter a number: "))
try:
    print(10/number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid input")