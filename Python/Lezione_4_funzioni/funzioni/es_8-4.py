'''8-4. Camicie grandi: Modifica la funzione make-shirt() in modo che le camicie siano grandi per impostazione predefinita con un messaggio che legge adoro Python. Crea una camicia grande e una camicia media con il messaggio predefinito e una camicia di qualsiasi dimensione con un messaggio diverso.'''


def make_shirt(taglia:str = "grande", testo:str = "Adoro Python"):
    print(f"La taglia è: {taglia}, il testo è: {testo.upper()}")

make_shirt()
make_shirt("medium")