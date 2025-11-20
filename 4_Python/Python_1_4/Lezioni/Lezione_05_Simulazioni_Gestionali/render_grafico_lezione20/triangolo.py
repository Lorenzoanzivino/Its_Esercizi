'''Definire la classe Triangolo che estende la classe Forma e aggiunge specifiche circa la dimensione di un lato del triangolo (per semplicità, si suppone che il triangolo in questione sia un triangolo rettangolo).
Il costruttore della classe deve ricevere come argomento solo il lato del triangolo, ed impostare il nome della forma su "Triangolo".
Il metodo getArea() deve calcolare l'area del triangolo.
Il metodo render() deve stampare su schermo un triangolo rettangolo avente i due cateti di lunghezza pari ai valori passati nel costruttore. Il triangolo da stampare deve essere un triangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)'''

from forma import Forma

class Triangolo(Forma):
    def __init__(self, lato:int):
        super().__init__("Triangolo")

        self.lato = lato

    def getArea(self) -> int:
        return (self.lato * self.lato) // 2
    
    def render(self):
        for i in range(self.lato):
            if i == 0:  # prima riga
                print("*")
            elif i == self.lato - 1:  # ultima riga
                print("* " * self.lato)
            else:  # righe intermedie
                print("* " + "  " * (i - 1) + "*")


if __name__ == "__main__":
    t = Triangolo(4)
    print("Nome:", t.nome)
    print("Area:", t.getArea())
    print("Render del Triangolo: ")
    t.render()