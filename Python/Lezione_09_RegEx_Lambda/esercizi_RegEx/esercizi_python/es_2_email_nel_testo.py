'''2. Trova tutte le email in un testo

Scrivi una funzione extract_emails(text) che prende un testo e restituisce tutte le email trovate.

Esempio:

text = "Contattaci a info@azienda.com oppure support@help.org"
extract_emails(text)  # ['info@azienda.com', 'support@help.org']'''

import re

def extract_emails(text:str) -> list[str]:

    pattern : str = r'\w\w+@\w[\w-]*\w?.\w+'

    found_email = re.findall(pattern, text)

    print(found_email)

extract_emails("Contattaci a info@azienda.com oppure support@help.org")