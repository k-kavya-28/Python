empl_file = open("employees.txt", "r")

# print(empl_file.readable())
# print(empl_file.read())
# print(empl_file.readline())
# print(empl_file.readline())
# print(empl_file.readlines())

# print(empl_file.readlines()[1])

for employee in empl_file.readlines():
    print(employee)
empl_file.close()

# r = read
# w = write
# a = append
# r+ = read and write
# w+ = write and read
# a+ = append and read
# rb = read binary
# wb = write binary
# ab = append binary
# rb+ = read and write binary
# wb+ = write and read binary
# ab+ = append and read binary