from formaGenerica import FormaGenerica

class Rettangolo(FormaGenerica):

    # Inizializzare un oggetto della Classe Rettangolo
    def __init__(self):
        super().__init__()

        self.setShape('rettangolo')


    def draw(self) -> None:
            
            print(f"\n{self.getShape()}\n")

            '''
            per il lato A: i = 0 and j < 10
            per il lato B: i < 5 and j = 0
            per il lato C: i < 5 and j = 10 -1
            per il lato D: i = 5-1 and j < 10

            '''

            # ciclo for i = lato verticale
            for i in range(5):
                #ciclo for j = lato orizzontale
                for j in range(5*2):
                     
                    # il lato A e lato D del rettangolo
                    if i == 0 or i == 5-1:
                        print("*", end = " ")
                    
                    # il lato B e lato C
                    elif j == 0 or j == 5*2-1:
                        print("*", end = " ")

                    # spazi bianchi
                    else:
                        print(" ", end = " ")  
            
                print("\n", end = "")
