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
    def __init__(self, id_produto, codigo, descricao, valor_unitario):
        self._id = id_produto
        self._codigo = codigo
        self._descricao = descricao
        self._valorUnitario = valor_unitario

    @property
    def get_descricao(self):
        return self._descricao

    @property
    def get_valor_unitario(self):
        return self._valorUnitario
