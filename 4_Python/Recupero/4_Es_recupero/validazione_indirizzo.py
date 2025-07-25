'''Validazione di un Indirizzo IPv4
Scrivi una funzione is_valid_ipv4(address: str) -> bool che determina se una
stringa è un indirizzo IPv4 valido. Un indirizzo IPv4 è composto da quattro numeri decimali
(ciascuno da 0 a 255) separati da punti (.). Gli zeri iniziali sono consentiti (ad esempio
192.168.001.001 è valido), ma ciascuna delle quattro parti deve essere compresa tra 0 e
255 e non deve contenere caratteri o spazi aggiuntivi.
Requisiti:
● Se non ci sono esattamente tre punti o non ci sono quattro parti numeriche,
restituisci False.
● Ciascuna parte deve contenere solo cifre (isdigit()) e, convertita in intero, deve
essere nel range [0,255][0,255][0,255].
Esempi:
is_valid_ipv4("192.168.0.1") # True
is_valid_ipv4("255.255.255.255") # True
is_valid_ipv4("256.100.10.1") # False (256 è fuori range)
is_valid_ipv4("192.168.1") # False (solo 3 parti)
is_valid_ipv4("192.168.1.a") # False (parte non numerica)'''

def is_valid_ipv4(address: str) -> bool:
    blocchi:list[str] = address.split(".")
    if len(blocchi) != 4:
        return False

    for blocco in blocchi:
        if not blocco.isdigit():
            return False
        valore = int(blocco)
        if valore < 0 or valore > 255:
            return False

    return True


# Soluzione Professore

# 1) valori compresi tra 0 e 255
# 2) solo numeri
# 3) 4 gruppi di numeri

def check(ip: str) -> bool:

    ip:list[str] = ip.split(".")

    if len(ip) != 4:
        return False
    
    for component in ip:
        # verifica che siano solo numeri o che sia compreso
        if not component.isdigit() or not (0 < int(component) <= 255):
            return False
    
    return True