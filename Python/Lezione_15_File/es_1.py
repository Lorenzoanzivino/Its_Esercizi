class FileManager:
    def __init__(self, file:str, mode:str, encoding="utf-8") :
        self.file = file
        self.wrapper = None
        self.mode = mode
        self.encoding = encoding

    def __enter__(self) :
        self.wrapper = open(self.file, self.mode)
        print("resource acquired")
        return self

    def __exit__(self, exc_type, exc_value, traceback) :
        print("resource acquired")
        self.wrapper.close()
        if exc_type is not None:
            print(f"An error occured: {exc_type}")
            print(f"An error occured: {exc_value}")
            print(f"An error occured: {traceback}")

        return True

with FileManager("example.txt", "r") as resource :
    print("Sono dentro il blocco with")

