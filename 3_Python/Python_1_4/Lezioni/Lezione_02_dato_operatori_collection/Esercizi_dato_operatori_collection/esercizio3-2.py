'''3-2
Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them.
The text of each message should be the same, but each message should be personalized with the person’s name.'''

myfriendslist:list = ["Stefano", "Peppe", "Francesco", "Patrick"]

for name in myfriendslist:
    print(f"Ciao, {name}, come stai?")

print(f"Ciao {myfriendslist[0]}, come stai?")
print(f"Ciao {myfriendslist[1]}, come stai?")
print(f"Ciao {myfriendslist[2]}, come stai?")
print(f"Ciao {myfriendslist[3]}, come stai?")