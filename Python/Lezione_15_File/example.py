# Funzione open()

# PATH: str = "example.txt"
# file = open(PATH, "r", encoding="utf-8")
# output: str = file.read()
# print(output)

file = open("example.txt", "a")
try :
    pass
except Exception as e:
    pass
finally :
    file.close()

# CONTESTO
# Uscendo dal print che è indentato il file si chiude automaticamente
with open("example.txt", "w") as file :
    print(file.read())