class Carta():
    def __init__(self, naipe, rank, valor):
        self.naipe = naipe
        self.rank = rank
        self.valor = valor

    def __str__(self):
        # return self.rank + 'de' + self.naipe + '[' + str(self.valor) + "]"
        return f'{self.rank} de {self.naipe} [{self.valor}]'