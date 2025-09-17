'''5-1.
Test condizionali: scrivi una serie di test condizionali. Stampa un'istruzione
che descriva ogni test e la tua previsione per i risultati di ogni test. Il tuo codice
dovrebbe assomigliare a questo:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Osserva attentamente i tuoi risultati e assicurati di capire perché ogni riga
viene valutata come True o False.
• Crea almeno 10 test. Fai in modo che almeno 5 test vengano valutati come True e altri
5 test vengano valutati come False.
'''

# Variabili da testare
macchina = "subaru"
anni = 25
nome = "Alice"
piove = True
colore_preferito = "blue"

# Test macchina 1
print("La macchina == 'subaru'? I predict True.")
print(macchina == 'subaru')

# Test macchina 2
print("\nLa macchina == 'audi'? I predict False.")
print(macchina == 'audi')

# Test anni 1
print("\nGli anni sono: > 18? I predict True.")
print(anni > 18)

# Test anni 2
print("\nGli anni sono: == 30? I predict False.")
print(anni == 30)

# Test nome 1
print("\nIl nome è: == 'Alice'? I predict True.")
print(nome == 'Alice')

# Test nome 2
print("\nIl nome è: == 'Bob'? I predict False.")
print(nome == 'Bob')

# Test piove
print("\nPiove? I predict True.")
print(piove)

# Test colore preferito 1
print("\nIl colore preferito è: == 'red'? I predict False.")
print(colore_preferito == 'red')

# Test colore preferito 2
print("\nIl colore preferito è: == 'blue'? I predict True.")
print(colore_preferito == 'blue')

# Test nome vuoto ''
print("\nIl nome è: != ''? I predict True.")
print(nome != '')
