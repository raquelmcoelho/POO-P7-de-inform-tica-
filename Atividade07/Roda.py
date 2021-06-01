class Roda:
    def __init__(self, d, m):
        self.diametro = d
        self.material = m

    def __str__(self):
        return f"Roda do diametro {self.diametro} e feita de {self.material}"
