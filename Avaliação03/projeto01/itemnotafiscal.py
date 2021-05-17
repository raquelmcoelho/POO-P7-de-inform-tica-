"""
    Módulo itemnotafiscal 
    Classe ItemNotaFiscal 
    Atributos :
        id         - informado
        sequencial - informado
        quantidade - informado
        produto    - informado
        valor      - calculado.            
"""
from produto import Produto


class ItemNotaFiscal:
    def __init__(self, id_item, sequencial, quantidade, produto_object):
        self._id = id_item
        self._sequencial = sequencial
        self._quantidade = quantidade
        self._produto = self.set_produto_item(produto_object)
        self._descricao = self._produto.get_descricao
        self._valorUnitario = self._produto.get_valor_unitario
        self._valorItem = (self._quantidade * self._valorUnitario)

    @staticmethod
    def set_produto_item(product):
        if isinstance(product, Produto):
            return product

    @property
    def get_sequencial(self):
        return self._sequencial

    @property
    def get_qtd(self):
        return self._quantidade

    @property
    def get_produto(self):
        return self._produto

    @property
    def get_valor_item(self):
        return self._valorItem
