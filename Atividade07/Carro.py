from Veiculo import *
from Roda import *


class Carro(Veiculo):
    def __init__(self, cor, marca, ano):
        super().__init__()
        # atributos da classe filho
        self.cor = cor
        self.marca = marca
        self.ano = ano
        self.rodas = []
        [self.rodas.append(Roda(0.30, "borracha")) for _ in range(4)]

    def __str__(self):
        return f"\n\nCarro da cor {self.cor}\nmarca {self.marca}\ne ano {self.ano}\n{self.rodas[0]}\n\n"

    @staticmethod
    def buzinar():
        return "fom fom!"

    @staticmethod
    def ligar_seta():
        return "seta ligada"

    def ligar(self):
        return "Seu " + self.marca + " foi ligado"

    def desligar(self):
        self.parar()
        return "Seu " + self.marca + " foi desligado"

    def estacionar(self):
        # chamar classe do pai com argumento padrão
        return self.frear(10, 0.1)


if __name__ == '__main__':

    fusca = Carro("vermelho", "sedan", 2021)
    print("\033[035m\n\nMétodos e atributos da classe filho(Carro)")
    print("\033[097m\nFunção __str__:  ", fusca)
    print("Função buzinar: ", fusca.buzinar())
    print("Função ligar seta: ", fusca.ligar_seta())
    print("Função ligar: ", fusca.ligar())
    print("Função desligar: ", fusca.desligar())
    print("Função estacionar: ", fusca.estacionar())

    print("\033[035m\n\nMétodos e atributos da classe pai (Veículo)")
    print("\033[97m\nAtributo Velocidade: ", fusca.velocidade)
    print("Atributo Posição: ", fusca.posicao)
    print("Função parar: ", fusca.parar())
    print("Função acelerar: ", fusca.acelerar(50, 0.5))
    print("Função frear: ", fusca.frear(20, 0.2))
    print("Função estado: ", fusca.estado())
    print("Função checar: ", fusca.checar())
