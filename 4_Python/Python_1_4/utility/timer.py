def cronometro(fun):
    def wrapper(*args):
        import time
        start:float = time.time()
        fun(*args)
        print(time.time() - start)
    
    return wrapper