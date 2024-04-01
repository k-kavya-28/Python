lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim","Jim", "Oscar", "Toby"]
#friends.extend(lucky_numbers)
#friends.append("Creed")     # Added at the end of the list
#friends.insert(1, "Kelly")  # Added at index 1
#friends.remove("Jim")       # Removed Jim
#friends.clear()             # Removed all elements
# friends.pop()               # Removed the last element
print(friends)
#print(friends.index("Kevin"))  # Gives the index of Kevin
# print(friends.count("Jim"))    # Gives the count of Jim
# friends.sort()                 # Sorts the list
# print(friends)
lucky_numbers.sort()
# print(lucky_numbers)
lucky_numbers.reverse()
# print(lucky_numbers)
friends2 = friends.copy()
print(friends2)
