# filtra e Somma Numeri Pari — PUNTI 1
# Scrivi una funzione:
# filter_and_sum_even(nums: list[int], min_val: int) -> int
# che prende una lista di interi e un valore minimo, e restituisce la somma di tutti i numeri pari maggiori di min_val.
# Se nessun numero soddisfa la condizione, restituisci 0.
# 📘 Esempio:
# filter_and_sum_even([3, 6, 9, 10, 12], 5)  # → 28 (6 + 10 + 12)

def filter_and_sum_even(nums:list[int], min_val: int) -> int:
    somma = 0
    for num in nums:
        if num > min_val and num % 2 == 0:
            somma += num
        return somma
print(filter_and_sum_even([1, 3, 5], 10))   # → 0 (nessun numero > 10 e pari)
print(filter_and_sum_even([2, 4, 6], 10))   # → 0 (tutti < 10)
print(filter_and_sum_even([12, 14], 10))    # → 26 (12+14)



# Calcola Media Ponderata — PUNTI 1
# Scrivi una funzione:
# weighted_average(values: list[float], weights: list[float]) -> float
# che calcola la media ponderata dei valori.
# Se le liste sono vuote o di lunghezza diversa, solleva un ValueError con messaggio "Liste non valide.".
# 📘 Esempio:
# weighted_average([8, 6, 9], [0.5, 0.3, 0.2])  # → 7.7

def weighted_average(values: list[float], weights: list[float]) -> float:
    if not values or not weights or len(values) != len(weights):
        raise ValueError("Liste non valide")
    weighted_sum = 0
    total_weight = 0
    for i in range(len(values)):
        weighted_sum += values[i] * weights[i]
        total_weight += weights[i]
    media = weighted_sum / total_weight
    return media
# Esempio
print(weighted_average([8, 6, 9], [0.5, 0.3, 0.2]))  # → 7.7
    


# Controllo Accesso — PUNTI 1
# Scrivi una funzione:
# check_access(card_valid: bool, pin_correct: bool, admin_override: bool) -> str
# L’accesso è consentito solo se:
# la carta è valida (card_valid == True)
# e (il PIN è corretto o è attivo l’override admin)
# La funzione deve restituire "Accesso consentito" o "Accesso negato".
# 📘 Esempio:
# check_access(True, False, True)  # → "Accesso consentito"

def check_access(card_valid: bool, pin_correct: bool, admin_override: bool) -> str:
    if card_valid == True and (pin_correct == True or admin_override == True):
        return "Accesso consentito"
    else:
        return "Accesso Negato"
print(check_access(True, False, False))
print(check_access(True, False, True))
print(check_access(False, False, True))



# 1. Somma Numeri Dispari Maggiori — PUNTI 1
# Scrivi una funzione:
# sum_odd_greater(nums: list[int], min_val: int) -> int
# Restituisce la somma di tutti i numeri dispari maggiori di min_val.
# Se nessuno soddisfa la condizione, restituisce 0.
# 📘 Esempio:
# sum_odd_greater([1, 3, 5, 8], 3)  # → 5 (solo 5 > 3)

def sum_odd_greater(nums:list[int], min_val:int) -> int:
    somma = 0
    for num in nums:
        if num > min_val and num % 2 == 1:
            somma += num
    return somma
    
print(sum_odd_greater([1, 3, 5, 8], 3))



# 2. Trova Massimo Condizionale — PUNTI 1
# Scrivi una funzione:
# conditional_max(nums: list[int], threshold: int) -> int | str
# Restituisce il massimo numero nella lista maggiore di threshold.
# Se nessuno soddisfa la condizione, restituisce "Nessun numero valido".
# 📘 Esempio:
# conditional_max([2, 7, 4, 9], 5)  # → 9

def conditional_max(nums1:list[int], threshold:int) -> int:
    for num1 in nums1:
        if num1 > threshold:
            massimo = num1
    return massimo
print(conditional_max([2, 7, 4, 9], 5))



# 3. Verifica Login Multiplo — PUNTI 1
# Scrivi una funzione:
# check_login(user_active: bool, password_correct: bool, otp_verified: bool) -> str
# L’accesso è consentito solo se:
# - l’utente è attivo
# - e la password è corretta
# - e l’OTP è verificato
# Restituisce "Login consentito" o "Login negato".
# 📘 Esempio:
# check_login(True, True, False)  # → "Login negato"

def check_login(user_active:bool, password_correct:bool, otp_verified:bool) -> str:
    if user_active==True and password_correct==True and otp_verified==True:
        return "Login Consentito"
    return "Login negato"
print(check_login(True, True, False))