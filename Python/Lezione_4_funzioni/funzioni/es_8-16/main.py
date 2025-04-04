'''8-16. Importazioni: Utilizzando un programma che hai scritto che contiene una funzione, memorizza quella funzione in un file separato. Importa la funzione nel tuo file principale e chiama la funzione utilizzando ciascuno di questi approcci: importa nome_modulo da nome_modulo importa nome_funzione da nome_modulo importa nome_funzione come fn importa nome_modulo come mn da nome_modulo importa *'''

# 1. Importare l'intero modulo
import module_name
module_name.function_name("Mario")

# 2. Importare solo la funzione
from module_name import function_name
function_name("Luigi")

# 3. Importare la funzione con un alias
from module_name import function_name as fn
fn("Anna")

# 4. Importare l'intero modulo con un alias
import module_name as mn
mn.function_name("Giulia")

# 5. Importare tutte le funzioni dal modulo
from module_name import *
function_name("Marco")



# Imoportare la funzione e modulo con un ciclo
from module_name import show_messages
for nome in module_name.messages:
    print("Ciao")