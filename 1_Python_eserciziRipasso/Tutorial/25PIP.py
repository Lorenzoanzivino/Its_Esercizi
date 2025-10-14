# Gestori di pacchetti da scaricare da terminale: funzionalità extra

# pip --version oppure pip -V
# python get-pip.py 

import camelcase

c = camelcase.CamelCase()    # tutte le parole iniziano con la lettera maiuscola

frase = "ciao sono lorenzo"
print(c.hump(frase))

frase2 = "ciao sono lorenzo"
print(frase2.title())