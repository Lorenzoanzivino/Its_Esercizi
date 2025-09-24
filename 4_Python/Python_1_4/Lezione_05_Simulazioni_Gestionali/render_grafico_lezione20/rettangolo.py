'''Definire la classe Rettangolo che estende la classe Forma e aggiunge specifiche circa la lunghezza della sua base e della sua altezza.
Il costruttore della classe deve ricevere come argomento solo la base e l'altezza del rettangolo, ed impostare il nome della forma su "Rettangolo".
Il metodo getArea() deve calcolare l'area del rettangolo.
Il metodo render() deve stampare su schermo un rettangolo avente base ed altezza pari ai valori passati nel costruttore. Il rettangolo da stampare deve essere un rettangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)'''

from forma import Forma

class Rettangolo(Forma):
    def __init__(self, base:int, altezza:int):
        super().__init__("Rettangolo")

        self.base = base
        self.altezza = altezza

    def getArea(self) -> int:
        return self.base * self.altezza
    
    def render(self):
        for i in range(self.altezza):
            if i == 0 or i == self.altezza - 1:
                # prima e ultima riga: tutte stelle
                print("* " * self.base)
            else:
                # righe interne: stella, spazi, stella
                print("* " + "  " * (self.base - 2) + "*")


if __name__ == "__main__":
    r = Rettangolo(8, 4)
    print("Nome:", r.nome)
    print("Area:", r.getArea())
    print("Render del rettangolo: ")
    r.render()