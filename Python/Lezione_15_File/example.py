# Funzione open()

PATH: str = "example.txt"

file = open(PATH, "r", encoding="utf-8")

output: str = file.read()

print(output)

file.close()