is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a male")
elif is_male and not(is_tall):
    print("You are male and not tall")
elif not(is_male) and is_tall:
    print("You are tall and not male")
else:
    print("You are neither male nor tall")