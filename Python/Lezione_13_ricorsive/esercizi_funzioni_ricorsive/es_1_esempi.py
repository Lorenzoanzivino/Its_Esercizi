'''def recursive_countdown(n:int) -> None:

    # Step 1 "n is negative"
    if n < 0 :
        print("Error! Inserted number is negative!")

    # Step 2 "n = 0 si ferma la ricorsione"
    elif n == 0:
        print(0)

    # Se n > 0 stampa n incrementato finchè n non corrisponderà a uno dei due casi di blocco (n<0 oppure n==n)
    else:
        print(n)
        recursive_countdown(n-1)

recursive_countdown(5)'''

'''def sum(n:int) -> int:
    # n is negative
    if n < 0:
        print("\nError! Inserted number is negative!")
        return None
    # n is positive
    else:
        # define a sum
        sum:int = 0
        # compute sum until n >= 0
        while n:
            sum = sum + n
            n = n-1
    # return sum as int
    return int(sum)

# calling sum function for n = -5
print(sum(-5))
# calling sum function for n = 5
print(f"\n{sum(5)}")'''

# Esempio 1
'''def recursive_sum(n:int) -> int:
    # n is negative
    if n < 0:
        print("Error! Inserted number is negative!")
        return None

    # if n = 0 recursive process must be stopped
    elif n == 0:
        return 0
    
    # if n is positive, compute recursive sum
    else:
        return int(n + recursive_sum(n-1))
    
print(recursive_sum(5))'''

# Esempio 2
def recursiveSumInRange(a:int, b:int) -> int:
    # if a > b, swap values of a and b
    if a > b:
        # define a temporary variable called temp, containing value of a
        temp:int = a

        # swap values of a and b
        a = b
        b = temp # now b = a

    # if b = a, the recursive process must be stopped
    if b == a:
        return int(a)
    
    # otherwise, compute the sum recursively
    else:
        return int(b + recursiveSumInRange(a, b-1))
    
# calling sumInRange function for a=5, b=10
print(recursiveSumInRange(5,10))