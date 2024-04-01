lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
friends.append("Creed")     # Added at the end of the list
friends.insert(1, "Kelly")  # Added at index 1
friends.remove("Jim")       # Removed Jim
print(friends)