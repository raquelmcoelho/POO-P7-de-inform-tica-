from TipoMovimento import TipoMovimento


class MovimentoFolha:
    def __init__(self, idcolaborador, descricao, valor, tipomovimento):
        self._idcolaborador = idcolaborador
        self._descricao = str(descricao)
        self._valor = float(valor)
        self._tipomovimento = self.set_tipo_movimento(tipomovimento)

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
    def get_idcolaborador(self):
        return self._idcolaborador

    @property
    def get_descricao(self):
        return self._descricao
