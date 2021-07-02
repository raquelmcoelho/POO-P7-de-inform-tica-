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
from app.model.Produto import Produto


class ItemNotaFiscal:
    id_itens = 0

    def __init__(self, quantidade, produto_object):
        self._id = ItemNotaFiscal.id_itens
        ItemNotaFiscal.id_itens += 1
        self._sequencial = None
        self._quantidade = quantidade
        self._produto = self.check_produto_item(produto_object)
        self._descricao = self._produto.descricao
        self._valor_item = self.calcular_valor_item()

    def __dict__(self):
        dict_item = {"Id Item": self._id,
                     "Sequencial": self.sequencial,
                     "Quantidade": self._quantidade,
                     "Descrição": self._descricao,
                     "Valor Item": self._valor_item}
        return dict_item

    # class methods
    @staticmethod
    def check_produto_item(product):
        if isinstance(product, Produto):
            return product

    # getters
    @property
    def id(self):
        return self._id

    @property
    def sequencial(self):
        return self._sequencial

    @property
    def quantidade(self):
        return self._quantidade

    @property
    def produto(self):
        return self._produto

    @property
    def descricao(self):
        return self._descricao

    @property
    def valor_item(self):
        return self._valor_item

    # setters
    @produto.setter
    def produto(self, novoproduto):
        self._produto = self.check_produto_item(novoproduto)
        self.calcular_valor_item()

    @quantidade.setter
    def quantidade(self, qtd):
        self._quantidade = qtd
        self.calcular_valor_item()

    @sequencial.setter
    def sequencial(self, sequencial_inputada):
        self._sequencial = sequencial_inputada

    # another methods
    def calcular_valor_item(self):
        return self._quantidade * self._produto.valorunitario
