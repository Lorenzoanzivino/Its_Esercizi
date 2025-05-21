class Specie:
    def __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float):
        self.nome = nome
        self.popolazione = popolazione_iniziale
        self.tasso_crescita = tasso_crescita

    def cresci(self) -> int:
        self.popolazione = int(self.popolazione * (1 + self.tasso_crescita / 100))
        return self.popolazione

    def anni_per_superare(self, altra_specie: 'Specie') -> int:
        anni = 0
        # Creiamo copie delle popolazioni per non modificare gli oggetti originali durante la simulazione
        popolazione_self = self.popolazione
        popolazione_altra = altra_specie.popolazione
        
        # Continua a simulare finché la popolazione di questa specie non supera l'altra
        # o finché non si raggiunge il limite di 1000 anni per evitare loop infiniti
        while popolazione_self <= popolazione_altra and anni < 1000:
            popolazione_self = int(popolazione_self * (1 + self.tasso_crescita / 100))
            popolazione_altra = int(popolazione_altra * (1 + altra_specie.tasso_crescita / 100))
            anni += 1
        
        # Se il limite di 1000 anni è stato raggiunto e la condizione non è stata soddisfatta,
        # significa che non si supererà l'altra specie in un tempo ragionevole.
        if anni == 1000:
            return -1 # O un altro valore per indicare che non è stato raggiunto
        else:
            return anni

    def getDensita(self, area_kmq: float) -> int:
        anni = 0
        # Creiamo una copia della popolazione per non modificare l'oggetto originale
        popolazione_corrente = self.popolazione
        
        # Continua a simulare finché la densità non raggiunge 1 individuo per km²
        # o finché non si raggiunge il limite di 1000 anni
        while (popolazione_corrente / area_kmq) < 1 and anni < 1000:
            popolazione_corrente = int(popolazione_corrente * (1 + self.tasso_crescita / 100))
            anni += 1
        
        # Se il limite di 1000 anni è stato raggiunto e la condizione non è stata soddisfatta,
        # significa che la densità non sarà raggiunta in un tempo ragionevole.
        if anni == 1000:
            return -1 # O un altro valore per indicare che non è stato raggiunto
        else:
            return anni


class BufaloKlingon(Specie):
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__("Bufalo Klingon", popolazione_iniziale, tasso_crescita)


class Elefante(Specie):
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__("Elefante", popolazione_iniziale, tasso_crescita)