# datetime: import, .now(), formattazione, parametri di formattazione

'''
📅 Codici per data

%a → Nome del giorno abbreviato (es. lun, Tue)

%A → Nome completo del giorno (es. lunedì, Tuesday)

%w → Giorno della settimana come numero (0=dom, 6=sab)

%d → Giorno del mese (01–31)

%-d → Giorno del mese senza zero iniziale (Linux/Unix, non su Windows)

%b → Nome del mese abbreviato (es. gen, Jan)

%B → Nome completo del mese (es. gennaio, January)

%m → Mese come numero (01–12)

%-m → Mese senza zero iniziale (Unix/Linux)

%y → Anno con due cifre (00–99)

%Y → Anno con quattro cifre (es. 2025)

%j → Giorno dell’anno (001–366)

%U → Numero della settimana dell’anno (domenica = primo giorno della settimana)

%W → Numero della settimana dell’anno (lunedì = primo giorno della settimana)

⏰ Codici per ora

%H → Ora (00–23)

%I → Ora (01–12)

%p → AM / PM (dipende dalla locale, es. AM/PM o m./p.)

%M → Minuti (00–59)

%S → Secondi (00–59)

%f → Microsecondi (000000–999999)

%z → Offset del fuso orario in formato +HHMM o -HHMM

%Z → Nome del fuso orario (es. CET, UTC)

📌 Codici combinati / utilità

%c → Data e ora completa secondo la locale (es. lun 25 ago 2025 09:33:20)

%x → Solo data secondo la locale

%X → Solo ora secondo la locale

🌀 Caratteri di escape

%% → Il simbolo % letterale
'''

import datetime

# data e ora attuali
x:datetime = datetime.datetime.now()
print(x)

# data impostata senza orario
y = datetime.datetime(2012, 6, 13)
print(y)

# cambiare formato data
z = datetime.datetime.now()
print(z.strftime("%B"))

# data formattata
data_formattata = datetime.datetime.now()
print(data_formattata.strftime("%d/%m/%Y"))    # classica data dd/mm/yy
print(data_formattata.strftime("%A %d %b %Y"))    # formattazione Giorno numero Mese anno