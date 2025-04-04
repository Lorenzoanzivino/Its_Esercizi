'''Esercizio 8-8. Album degli utenti: Parti dal programma dell'Esercizio 8-7. Scrivi un ciclo while che permetta agli utenti di inserire l'artista e il titolo di un album. Una volta ottenute queste informazioni, chiama la funzione make_album() con i dati inseriti dall'utente e stampa il dizionario che viene creato. Assicurati di includere un valore di uscita nel ciclo while.'''


def make_album(artist:str, title:str, num_song:int = None) -> dict:
    if num_song is None:
        num_song = "Unknown"
    # Restituisce un dizionario con l'artista, il titolo dell'album e numero di canzoni.
    album:dict = {"artista": artist, "titolo": title, "numero canzoni": num_song}
    return album

# Ciclo while che permette all'utente di inserire artista e titolo
while True:
    print("\nInserisci i dettagli dell'album o digita 'esci' per uscire.")
    artist:str = str(input("Artista: "))
    if artist == "esci":
        break
    
    title:str = str(input("Titolo dell'album: "))
    if title == "esci":
        break

    num_song:str = input("Inserisci il numero di brani: ")
    if num_song == "esci":
        break
    
    # Se il numero di brani è vuoto: "Unknown"
    if not num_song: # stringa vuota = falso - ma Not = true.
        album = make_album(artist, title)
    else:
        album = make_album(artist, title, num_song)  #Converti a int se non vuoto

    print(f"Album creato: Artista: {album['artista']}, Titolo: {album['titolo']}, Numero di canzoni: {album['numero canzoni']}")

