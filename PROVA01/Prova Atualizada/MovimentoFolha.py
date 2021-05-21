from Colaborador import Colaborador
from TipoMovimento import TipoMovimento

class MovimentoFolha:
    def __init__(self, colaborador, descricao, valor, tipomovimento):
        self._colaborador = self.set_colaborador(colaborador)
        self._descricao = str(descricao)
        self._valor = float(valor)
        self._tipomovimento = self.set_tipo_movimento(tipomovimento)

    @staticmethod
    def set_colaborador(colab):
        if isinstance(colab, Colaborador):
            return colab

    @staticmethod
    def set_tipo_movimento(tipo):
        if tipo == "D":
            return TipoMovimento.D.value
        elif tipo == "P":
            return TipoMovimento.P.value
        else:
            return "Desconhecido"

    @property
    def get_tipomovimento(self):
        return self._tipomovimento

    @property
    def get_valor(self):
        return self._valor

    @property
    def get_colaborador(self):
        return self._colaborador

    @property
    def get_descricao(self):
        return self._descricao
