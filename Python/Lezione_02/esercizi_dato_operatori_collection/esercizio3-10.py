'''3-10
Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.'''

mylist:list[str]= ["Japan", "Alpi","London", "English", "AsRoma","Orange", "Sicily"]
print(mylist)
mylist2= sorted(mylist)
print(mylist2)

mylist2=sorted(mylist, reverse=True)
print(mylist2)

mylist.pop(1)
print(mylist)

mylist.insert(1,"Jamaica")
print(mylist)

mylist.append("Black")
print(mylist)

mylist.pop(3)
print(mylist)

print(f"I would like to visit {mylist[0]} as soon as possible")

print(len(mylist))
