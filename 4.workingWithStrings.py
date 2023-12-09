print("Khushi\n\"Kavya\"")
print("hello\bye")  # backslash can be printed anvi

#concatenation and some common functions that can be used with strings
name = "Khushi Kavya"
print(name + " is cool")
print(name.lower())
print(name.upper())
print(name.isupper())
print(name.islower())
print(name.upper().isupper())
print(len(name))
print(name[0])
print(name[3])
print(name.index("y"))
print(name.index("Kav"))
print(name.index("a"))  # first occurence of a
# print(name.index("r"))    # error as not present 
print(name.replace("Kavya", "Jassika"))