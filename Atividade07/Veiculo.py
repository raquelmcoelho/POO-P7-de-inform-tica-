from Estado import *


class Veiculo:
    def __init__(self):
        # atributos da classe pai de visibilidade private
        self._estado = Estado.parado

        # atributos da classe pai de visibilidade pública, apenas para demonstração
        # km/hr
        self.velocidade = 0
        # x cartesiano
        self.posicao = 0

    # métodos privados
    def _andar(self, espaco):
        self.posicao += espaco

    @staticmethod
    def _checar_direcao(num):
        if num < 0:
            return -num, "pra trás"
        else:
            return num, "pra frente"

    # métodos públicos
    def checar(self):
        check_velocidade = self._checar_direcao(self.velocidade)
        check_posicao = self._checar_direcao(self.posicao)
        return f"Seu veículo está a {check_velocidade[0]} km por hr {check_velocidade[1]} e na posição" \
               f" {check_posicao[0]} {check_posicao[1]}"

    def parar(self):
        self._estado = Estado.parado
        self.velocidade = 0
        return self.checar()

    def acelerar(self, velocidade, tempo):
        self._estado = Estado.andando
        self.velocidade += velocidade
        espaco = velocidade * tempo
        self._andar(espaco)
        return self.checar()

    def frear(self, velocidade_re, tempo):
        self._estado = Estado.andando
        self.velocidade -= velocidade_re
        espaco = - (velocidade_re * tempo)
        self._andar(espaco)

        if self.velocidade == 0:
            self.parar()

        return self.checar()

    def estado(self):
        return self._estado.name


