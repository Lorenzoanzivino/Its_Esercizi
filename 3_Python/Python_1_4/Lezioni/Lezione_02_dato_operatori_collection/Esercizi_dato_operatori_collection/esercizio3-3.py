''' 3-3
Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car,
and make a list that stores several examples. Use your list to print a series of statements about these items,
such as “I would like to own a Honda motorcycle.”'''

myfavoritelist:list = ["Motocicletta Honda", "Macchina Ducia Duster", "Macchina Ferrari", "Motocicletta Ducati", "Macchina Lamborghini"]

for items in myfavoritelist:
        print(f"Mi piacerebbe avere una", items)

print(f"Mi piacerebbe avere una {myfavoritelist[0]}")
print(f"Mi piacerebbe avere una {myfavoritelist[1]}")
print(f"Mi piacerebbe avere una {myfavoritelist[2]}")
print(f"Mi piacerebbe avere una {myfavoritelist[3]}")
print(f"Mi piacerebbe avere una {myfavoritelist[4]}")