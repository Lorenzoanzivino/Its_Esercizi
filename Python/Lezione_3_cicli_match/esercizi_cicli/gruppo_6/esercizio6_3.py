'''- 6-3. Glossario: Un dizionario Python può essere usato per modellare un dizionario reale. Tuttavia, per evitare confusione, chiamiamolo un glossario.
Pensa a cinque parole di programmazione che hai imparato nei capitoli precedenti. Usa queste parole come i tasti nel tuo glossario e conserva i loro significati come valori.
Stampare ogni parola e il suo significato come output ben formattato. Potresti stampare la parola seguita da un colono e poi il suo significato, o stampare la parola su una riga e quindi stamparne il significato intarsiato su una seconda riga. Utilizzare il carattere newline (n) per inserire una linea vuota tra ogni coppia di parole-significante nell'output.'''

glossario:dict[str] = {
    "Variable": "A named location in memory used to store data",
    "Loop" : "A control structure used to repeat a block of code multiple times",
    "List": "A collection of ordered and mutable elements",
    "Dictionary:": "A collection of key-value pairs used to store and retrieve data efficiently",
    "Tuples":" A collection of unordered and immutable elements"}

for nome in glossario:
    print(f"{nome} : {glossario[nome]}")