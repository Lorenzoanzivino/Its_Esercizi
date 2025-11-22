'''
Definire la classe Quadrato che estende la classe Forma e aggiunge specifiche circa la lunghezza di un suo lato.
Il costruttore della classe deve ricevere come argomento solo il lato del quadrato, ed impostare il nome della forma su "Quadrato".
Il metodo getArea() deve calcolare l'area del quadrato.
Il metodo render() deve stampare su schermo un quadrato avente lato pari al valore passato nel costruttore. Il quadrato da stampare deve essere un quadrato vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)'''

from forma import Forma

class Quadrato(Forma):
    def __init__(self, lato:int):
        super().__init__("Quadrato")

        self.lato = lato

    def getArea(self) -> int:
        return self.lato ** 2
    
    def render(self):
        for i in range(self.lato):
            if i == 0 or i == self.lato - 1:
                # prima e ultima riga: tutte stelle
                print("* " * self.lato)
            else:
                # righe interne: stella, spazi, stella
                print("* " + "  " * (self.lato - 2) + "*")


if __name__ == "__main__":
    q = Quadrato(4)
    print("Nome:", q.nome)
    print("Area:", q.getArea())
    print("Render del quadrato: ")
    q.render()