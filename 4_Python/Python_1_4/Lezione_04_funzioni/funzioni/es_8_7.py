'''8-7. Album: scrivi una funzione chiamata make-album() che costruisce un dizionario che descrive un album musicale. La funzione dovrebbe assumere un nome d'artista e un titolo dell'album, e dovrebbe restituire un dizionario contenente queste due informazioni. Usa la funzione per creare tre dizionari che rappresentano diversi album. Stampare ogni valore di ritorno per mostrare che i dizionari memorizzano correttamente le informazioni dell'album. Usare Nessuno per aggiungere un parametro opzionale per make-album() che consente di memorizzare il numero di brani su un album. Se la riga di chiamata include un valore per il numero di brani, aggiungere tale valore al dizionario dell'album. Effettua almeno una nuova chiamata di funzione che include il numero di canzoni su un album.'''


def make_album(name:str, album:str, songs_number:int = None) -> dict:  # Definire il TIPO di una funzione quando ho un ritorno "-> NONE" quando non restituisce niente
    # sostituisco None con str "Unknow"
    if songs_number is None:
        songs_number = "Unknown"
    # Restituisce il dizionario contenente le informazioni sull'album
    return {"name": name, "album": album, "songs_number": songs_number}


# Lista di album
albums = [
    make_album("Evanescence", "Fallen", 11),
    make_album("I Prevail", "Lifelines", 15),
    make_album("I Prevail", "Trauma")
]

# Stampa tutte le informazioni degli album in un formato ordinato
for album in albums:
    print("\n"f"Artist: {album['name']}, Album: {album['album']}, Songs: {album['songs_number']}")
