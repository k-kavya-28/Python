num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")
# result = num1 + num2
# print(result) # will see number as strings and not give correct result eg. 2+3 = 23

# result = int(num1) + int(num2)  # drawback is cant enter float values terminal gives ERROR
result = float(num1) + float(num2)  
print(result)