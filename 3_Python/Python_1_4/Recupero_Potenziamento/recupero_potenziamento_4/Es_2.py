def proDict():

    dictionarytuple:dict[tuple,int] = {}

    for x in range(1,101,1):

        for y in range(2,89,2):

            dictionarytuple[(x,y)] = x*y

    return dictionarytuple

dict1:dict = proDict()

print(dict1[(13,88)])
print(dict1[(83,56)])
print(dict1[71,44])