import time

class Stopwatch:
    def __init__(self):
        self.start_time = 0.0
        self.end_time = 0.0

    def __enter__(self):
        self.start_time = time.time()

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Elapsed time: {elapsed_time:.8f} seconds")

        if exc_type is not None:
            print(f"Exception type : {exc_type}")
            print(f"An error occured : {exc_value}")
            print(f"Traceback : {traceback}")

        return True

print("Inizio del programma")

with Stopwatch():

    print("Sono dentro il blocco with")

print("Fine del programma")

with Stopwatch():
    lista1 = [i for i in range(10000000)]
    lista2 = [i for i in range(10000000)]
    lista2[100000000000000]
    lista3= [i for i in range(10000000)]