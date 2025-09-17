from abc import ABC, abstractmethod

class Volo(ABC):

    def __init__(self, codiceVolo:str, capacita_posti:int) -> None:
        self.set_codiceVolo(codiceVolo)        
        self.set_capacita_posti(capacita_posti)
        self.set_prenotazioni(0)

    def get_codiceVolo(self) -> str:
        return self._codiceVolo

    def set_codiceVolo(self, valore) -> None:
        self._codiceVolo = valore

    def get_capacita_posti(self) -> str:
        return self._capacita_posti

    def set_capacita_posti(self, valore) -> None:
        if valore < 0:
            raise ValueError("La capacità non può essere negativa.")
        self._capacita_posti = valore

    def get_prenotazioni(self) -> str:
        return self._prenotazioni

    def set_prenotazioni(self, valore) -> None:
        if not isinstance(valore, int) or valore < 0 or valore > self._capacita_posti:
            raise ValueError("Numero di prenotazioni non valido.")
        self._prenotazioni = valore

    @abstractmethod
    def prenota_posto(self) -> str:
        pass

    @abstractmethod
    def posti_disponibili(self) -> str:
        pass


class VoloCommerciale(Volo):

    def __init__(self, codiceVolo, capacita_posti) -> None:
        super().__init__(codiceVolo, capacita_posti)
        
        self.posti_economica = int(capacita_posti * 0.7)
        self.posti_business = int(capacita_posti * 0.2)
        self.posti_prima = capacita_posti - (self.posti_economica + self.posti_business)

        self.prenotazioni_economica:int = 0
        self.prenotazioni_business:int = 0
        self.prenotazioni_prima:int = 0
    
    def posti_disponibili(self) -> dict[str, int]:

        economica_disp = self.posti_economica - self.prenotazioni_economica
        business_disp = self.posti_business - self.prenotazioni_business
        prima_disp = self.posti_prima - self.prenotazioni_prima

        # Se i posti disponibili sia sul volo, sia su una specifica classe di servizio sono esauriti, il valore da associare alla corrispondete chiave è 0.

        tot_disp = economica_disp + business_disp + prima_disp

        if tot_disp < 0:
            tot_disp = 0
        if economica_disp < 0:
            economica_disp = 0
        if business_disp < 0:
            business_disp = 0
        if prima_disp < 0:
            prima_disp = 0

        posti_reali:dict[str, int] = {}

        posti_reali['posti disponibili'] = tot_disp
        posti_reali['classe economica'] = economica_disp
        posti_reali['classe business'] = business_disp
        posti_reali['prima classe'] = prima_disp

        return posti_reali

    def prenota_posto(self, posti: int, classe_servizio: str) -> str:
        prenotazioni_economica_aggiuntive = 0
        prenotazioni_business_aggiuntive = 0
        prenotazioni_prima_aggiuntive = 0

        posti_totali_disponibili = self.get_capacita_posti() - self.get_prenotazioni()

        if posti_totali_disponibili <= 0:
            return f"Il volo {self.get_codiceVolo()} è al completo."

        if posti > posti_totali_disponibili:
            return f"Non ci sono abbastanza posti totali disponibili sul volo {self.get_codiceVolo()}."

        if classe_servizio == 'economica':
            posti_disponibili_classe = self.posti_economica - self.prenotazioni_economica
            if posti_disponibili_classe >= posti:
                prenotazioni_economica_aggiuntive = posti
            else:
                return "Non ci sono abbastanza posti disponibili in classe economica."

        elif classe_servizio == 'business':
            posti_disponibili_classe = self.posti_business - self.prenotazioni_business
            if posti_disponibili_classe >= posti:
                prenotazioni_business_aggiuntive = posti
            else:
                return "Non ci sono abbastanza posti disponibili in classe business."

        elif classe_servizio == 'prima':
            posti_disponibili_classe = self.posti_prima - self.prenotazioni_prima
            if posti_disponibili_classe >= posti:
                prenotazioni_prima_aggiuntive = posti
            else:
                return "Non ci sono abbastanza posti disponibili in prima classe."

        else:
            return "Classe richiesta non valida."

        self.prenotazioni_economica += prenotazioni_economica_aggiuntive
        self.prenotazioni_business += prenotazioni_business_aggiuntive
        self.prenotazioni_prima += prenotazioni_prima_aggiuntive

        nuove_prenotazioni_totali = (
            prenotazioni_economica_aggiuntive +
            prenotazioni_business_aggiuntive +
            prenotazioni_prima_aggiuntive
        )
        self.set_prenotazioni(self.get_prenotazioni() + nuove_prenotazioni_totali)

        return f"Hai prenotato {posti} posti in classe {classe_servizio} sul volo {self.get_codiceVolo()}."


class VoloCharter(Volo):
    def __init__(self, codiceVolo, capacita_posti, costo_volo:float):
        super().__init__(codiceVolo, capacita_posti)

        self.set_costo_volo(costo_volo)
    
    def get_costo_volo(self) -> float:
        return self._costo_volo
    
    def set_costo_volo(self, costo_volo:float) -> None:
        self.costo_volo = costo_volo

    def prenota_posto(self):
        if self.get_prenotazioni() == self.get_capacita_posti():
            return f"Il volo {self.get_codiceVolo()} è stato prenotato al costo di {self.get_costo_volo()}€"
        else:
            return f"Non tutti i posti sono liberi, il volo {self.get_codiceVolo()} non può essere prenotato"

    def posti_disponibili(self):
        return self.get_capacita_posti() - self.get_prenotazioni()
        

class CompagniaAerea:
    def __init__(self, nome: str, prezzoBiglietto: float) -> None:
        self.nome: str = nome
        self.prezzoBiglietto: float = prezzoBiglietto
        self.flotta: list = []

    def aggiungi_volo(self, volo_commerciale) -> None:
        if volo_commerciale not in self.flotta:
            self.flotta.append(volo_commerciale)

    def rimuovi_volo(self, volo_commerciale) -> None:
        if volo_commerciale in self.flotta:
            self.flotta.remove(volo_commerciale)

    def mostra_flotta(self) -> None:
        if not self.flotta:
            print("Nessun volo presente nella flotta.")
        else:
            for volo in self.flotta:
                print(f"Codice volo: {volo.get_codiceVolo()}")

    def guadagno(self) -> float:
        totale = 0.0
        for volo in self.flotta:
            if isinstance(volo, VoloCommerciale):
                totale += (
                    volo.prenotazioni_economica * self.prezzoBiglietto +
                    volo.prenotazioni_business * self.prezzoBiglietto * 2 +
                    volo.prenotazioni_prima * self.prezzoBiglietto * 3
                )
            elif isinstance(volo, VoloCharter):
                if volo.get_prenotazioni() == volo.get_capacita_posti():
                    totale += volo.get_costo_volo()
        return round(totale, 2)
    

if __name__=="__main__":

    lista:list = []

    # CREAZIONE VOLO COMMERCIALE
    volo_com = VoloCommerciale("COM123", 100)
    print("Posti disponibili sul volo commerciale COM123:")
    print(volo_com.posti_disponibili())
    lista.append(str(volo_com.posti_disponibili()))

    # Prenotazioni
    volo_com.prenota_posto(70, "economica")
    print(volo_com.posti_disponibili())
    lista.append(str(volo_com.posti_disponibili()))

    volo_com.prenota_posto(20, "business")
    print(volo_com.posti_disponibili())
    lista.append(str(volo_com.posti_disponibili()))

    volo_com.prenota_posto(70, "prima")  # Errore
    print(volo_com.posti_disponibili())
    lista.append(str(volo_com.posti_disponibili()))

    volo_com.prenota_posto(10, "prima")
    print(volo_com.posti_disponibili())
    lista.append(str(volo_com.posti_disponibili()))

    volo_com.prenota_posto(1, "economica")  # Volo completo
    print(volo_com.posti_disponibili())
    lista.append(str(volo_com.posti_disponibili()))

    # CREAZIONE VOLO CHARTER
    volo_charter = VoloCharter("CHA456", 50, 5000.00)
    lista.append(str(f"Posti disponibili sul volo charter {volo_charter.get_codiceVolo()}: {volo_charter.posti_disponibili()}"))
    volo_charter.prenota_posto()
    volo_charter.prenota_posto()

    # SECONDO VOLO COMMERCIALE
    volo_com2 = VoloCommerciale("COM789", 50)
    volo_com2.prenota_posto(20, "economica")

    # COMPAGNIA AEREA
    compagnia = CompagniaAerea("SkyFly", 100.0)
    compagnia.aggiungi_volo(volo_com)
    compagnia.aggiungi_volo(volo_com2)

    compagnia.mostra_flotta()
    print(f"Guadagno della compagnia aerea: {compagnia.guadagno()}€")
    lista.append(str(f"Guadagno della compagnia aerea: {compagnia.guadagno()}€"))

    with open("./4_Python/Lezione_22_esercizio/report.txt", "w", encoding="utf-8") as file:
        for output in lista:
            file.write(output + "\n")