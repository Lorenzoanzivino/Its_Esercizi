from classeArtista import Artista
from classeBrano import Brano
from classeGestionale import Gestionale
from classePlaylist import Playlist
import json, os

if __name__ == "__main__":
    # ------------------- GESTIONALE -------------------
    gestionale = Gestionale()

    # Creo artisti
    artista1 = Artista("Lorenzo", "Anzivino", "Lorenzo")
    artista2 = Artista("Maria", "Rossi", "Maria")
    artista3 = Artista("Stefano", "Reali", "BrokenQ")
    
    gestionale.aggiungi_artista(artista1)
    gestionale.aggiungi_artista(artista2)
    gestionale.aggiungi_artista(artista3)

    # Creo brani
    brano1 = Brano("Prigioniero", "03:45")
    brano2 = Brano("A.K.U.M.A", "04:12")
    brano3 = Brano("Solito concetto", "03:34")
    brano4 = Brano("Framework", "05:31")
    brano5 = Brano("Black Tar", "03:28")
    brano6 = Brano("Fight Against", "04:28")
    brano7 = Brano("Degenerate", "05:10")

    # Assegno brani agli artisti
    gestionale.aggiungi_brano_a_artista(artista1, brano1)
    gestionale.aggiungi_brano_a_artista(artista1, brano2)
    gestionale.aggiungi_brano_a_artista(artista1, brano3)
    gestionale.aggiungi_brano_a_artista(artista3, brano4)
    gestionale.aggiungi_brano_a_artista(artista3, brano5)
    gestionale.aggiungi_brano_a_artista(artista3, brano6)
    gestionale.aggiungi_brano_a_artista(artista3, brano7)

    # Mostra artisti e brani
    print("\n=== ARTISTI E LORO BRANI ===")
    gestionale.lista_artisti()

    # ------------------- PLAYLIST -------------------
    playlist = Playlist("La mia Playlist: ")

    # Aggiungo brani alla playlist
    playlist.aggiungiBrano(brano1, gestionale)
    playlist.aggiungiBrano(brano3, gestionale)
    playlist.aggiungiBrano(brano4, gestionale)
    playlist.aggiungiBrano(brano4, gestionale)  # test duplicato
    playlist.aggiungiBrano(Brano("NonEsistente", "03:00"), gestionale)  # test brano non presente

    # Stampa playlist
    print("\n=== PLAYLIST ===")
    print(playlist.__str__())

    # Rimuovo un brano dalla playlist
    playlist.rimuoviBrano(brano3)
    print("\n=== PLAYLIST DOPO RIMOZIONE ===")
    print(playlist.__str__())

    # ------------------- SALVATAGGIO JSON -------------------
    percorsoFile = '/home/its/vscode_projects/Esercizi_ITS/0_Python_Youtube/esercizi_chatGPT/classi/3_medio/playlistMusicale/artisti.json'
    os.makedirs(os.path.dirname(percorsoFile), exist_ok=True)

    list_dict = gestionale.to_dict()
    with open(percorsoFile, "w", encoding='utf-8') as file:
        json.dump(list_dict, file, ensure_ascii=False, indent=4)

    print(f"\n{len(gestionale._rubrica)} artisti salvati correttamente in {percorsoFile}")
