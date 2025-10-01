'''Flusso dei Frammenti
Ti intrufoli nella Cittadella Velata: sacche di numeri sono rovesciate ovunque. Ricomponi il bottino in un'unica borsa usando `sum_list(nums)`, che somma tutti gli interi in `nums`; se `nums` è vuota, torna `0`. Mantieni la firma esatta e supera ogni test come fossero grate che si alzano.'''
def sum_list(nums: list[int]) -> int:
    somma = 0
    if nums == []:
        return 0
    else:
        for numeri in nums:
            somma += numeri
        return somma
    

'''Picco della Lista

Nella sala del tributo devi individuare la gemma più preziosa tra mucchi disordinati: usa `max_or_none(nums)` per ottenere il valore più alto, oppure `None` se il sacco è vuoto. Mantieni la firma e non far scattare i test-trappola.'''
def max_or_none(nums: list[int]) -> int | None:
    if nums == []:
        return None
    valoreMassimo:int = nums[0]
    for numeri in nums:
        if numeri > valoreMassimo:
            valoreMassimo = numeri
    return valoreMassimo


'''Eco delle Tracce

Nel corridoio successivo le trappole scattano sui duplicati: lascia passare solo le prime impronte usando `dedup_stable(nums)`, che restituisce una nuova lista con la prima comparsa di ogni valore in ordine. Mantieni la firma e scivola oltre i test.'''
def dedup_stable(nums: list[int]) -> list[int]:
    if nums == []:
        return nums
    nums2:list[int] = [nums[0]]

    for numeri in nums:
        if numeri != nums2[-1]:
            nums2.append(numeri)
    return nums2


'''Segmenti Rituali
La camera delle scorte vuole sacche di dimensione fissa. Organizza i pacchi con `chunk(lst, size)`, che divide `lst` in blocchi di `size` (l'ultimo può essere più corto). Mantieni la firma e non allarmare i test.'''
def chunk(lst: list[int], size: int) -> list[list[int]]:
    if lst == []:
        return lst
    
    risultato: list[list[int]] = []
    blocco: list[int] = []   
    for num in lst:
        blocco.append(num)          
        if len(blocco) == size:    
            risultato.append(blocco) 
            blocco = []             
    if blocco:                    
        risultato.append(blocco)
    return risultato
print(chunk([1,2,3,4,5,6,7,8,9,10], 4))


'''Trama Lineare
Prima di fuggire dal magazzino riversa ogni bottino in una singola pila pronta al trasferimento. Fallo con `flatten_once(nested)`, appiattendo di un livello una lista di liste. Mantieni la firma e supera i test come un'uscita pulita.'''
def flatten_once(nested: list[list[int]]) -> list[int]:
    if nested == []:
        return nested
    
    lista_nuova:list[int] = []
    for liste in nested:
        for num in liste:
            lista_nuova.append(num)
    return lista_nuova
print(flatten_once([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]))


'''Sigillo Cercato
Al mercato nero ottieni sempre ciò che cerchi: se il banco è vuoto, usa il ricambio. Fallo con `get_or_default(d, k, default)`, che torna il valore se c'è, altrimenti `default`, senza toccare `d`. Mantieni la firma e sfila tra i test.'''
def get_or_default(d: dict, k, default=None):
    if k in d:
        return d[k]
    return default
    

'''Atlante Fuso
Due mappe del palazzo vanno fuse: per ogni stanza tieni il tracciato più aggiornato. Usa `merge_overwrite(a, b)` per creare un nuovo dizionario con `b` che prevale su `a`. Mantieni la firma e scardina i test.'''
def merge_overwrite(a: dict, b: dict) -> dict:
    for k in b:
        a[k] = b[k]

    return a


'''Alleanze Invertite
Per passare inosservato usi codici invertiti: nessun simbolo deve andare perduto. Attua `invert_unique(d)` per scambiare chiavi e valori (valori univoci). Mantieni la firma e svanisci tra i test.'''
def invert_unique(d: dict) -> dict:
    nuovo_d:dict = {}
    for key, value in d.items():
        nuovo_d[value] = key
    return nuovo_d


'''Pioggia di Lettere
Lettere segrete cadono sul mantello: conta solo i messaggi reali, ignora i sigilli rotti. Usa `letter_count(text)` per mappare frequenze delle sole lettere minuscole, scartando il resto. Mantieni la firma e scavalca i test.'''
def letter_count(text: str) -> dict[str, int]:
    solo_minuscole: list[str] = []
    for char in text:
        if char.isalpha():
            solo_minuscole.append(char.lower())

    dizionario: dict[str, int] = {}
    for char in solo_minuscole:
        if char in dizionario:
            dizionario[char] += 1
        else:
            dizionario[char] = 1

    return dizionario