"""
    Módulo produto
    Classe Produto
    Atributos :
        id            - informado
        codigo        - informado
        descricao     - informado
        valorUnitario - informado.
"""


class Produto:
    id_produtos = 0

    def __init__(self,  codigo, descricao, valor_unitario):
        self._id = Produto.id_produtos
        Produto.id_produtos += 1
        self._codigo = codigo
        self._descricao = descricao
        self._valorunitario = valor_unitario

    def __dict__(self):
        dict_produto = {"Id Produto": self._id,
                        "Código": self._codigo,
                        "Descrição": self._descricao,
                        "Valor Unitário": self._valorunitario}

        return dict_produto

    # getters
    @property
    def id(self):
        return self._id

    @property
    def codigo(self):
        return self._codigo

    @property
    def descricao(self):
        return self._descricao

    @property
    def valorunitario(self):
        return self._valorunitario

    # setters
    @codigo.setter
    def codigo(self, codigonovo):
        self._codigo = codigonovo

    @descricao.setter
    def descricao(self, descricaonovo):
        self._descricao = descricaonovo

    @valorunitario.setter
    def valorunitario(self, valorunitarionovo):
        self._valorunitario = valorunitarionovo
