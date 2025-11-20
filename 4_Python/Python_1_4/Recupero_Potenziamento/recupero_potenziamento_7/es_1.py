
v1 = [1, 2, 3, 2, 5, 2, 1]
v2 = [2, 0, -1, 4, 6, 3, -1]

# 1.A
def baricentro(v: list[int]) -> int|None:
    count = 0
    for i in range(len(v)):
        count += 2
        if sum(v[:i+1]) == sum(v[i+1:]):
            return i
    print(f"{count} baricentro")
    return None
print(baricentro(v1))
print(baricentro(v2))


# 1.B
def printResult(v:list[int]) -> None:
    if baricentro(v) != None:
        print(f"Il baricentro è all'indice: {baricentro(v)}")
    else:
        print("Non esiste il baricentro!")

printResult(v1)
printResult(v2)


# 1.C
def baricentroOttimizzato(v: list[int]) -> bool:
    count = 0
    somma = 0

    for i in v:
        somma += i

    for i in range(len(v)):
        count += 1
        if somma - sum(v[:i+1]) == somma//2:
            return True
    print(f"{count} baricentro ottimizzato")
    return False

print(baricentroOttimizzato(v1))
print(baricentroOttimizzato(v2))