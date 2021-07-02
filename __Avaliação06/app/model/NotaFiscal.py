"""
    Módulo notafiscal -
    Classe NotaFiscal -
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado.
"""
import datetime
from app.model.Cliente import Cliente
from app.model.ItemNotaFiscal import ItemNotaFiscal


class NotaFiscal:
    idnotas = 0

    def __init__(self, codigo, cliente):
        self._id = NotaFiscal.idnotas
        NotaFiscal.idnotas += 1
        self._codigo = codigo
        self._cliente = self.check_cliente(cliente)
        self._data = datetime.date.today()
        self._itens = []

    def __dict__(self):
        itens_str = []
        if len(self._itens) != 0:
            for item in self._itens:
                itens_str.append(item.descricao)

        dict_nota = {"ID Nota": self._id,
                     "Código": self._codigo,
                     "Cliente": self._cliente.nome,
                     "Data": str(self._data),
                     "Itens": itens_str}
        return dict_nota

    # getters
    @property
    def id(self):
        return self._id

    @property
    def codigo(self):
        return self._codigo

    @property
    def cliente(self):
        return self._cliente

    @property
    def data(self):
        return self._data

    @property
    def itens(self):
        return self._itens

    # setters
    @codigo.setter
    def codigo(self, novocodigo):
        self._codigo = novocodigo

    @cliente.setter
    def cliente(self, novocliente):
        self._cliente = self.check_cliente(novocliente)

    # class methods
    @staticmethod
    def check_cliente(cliente):
        if isinstance(cliente, Cliente):
            return cliente

    # another methods
    def adicionar_item(self, item):
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
            item.sequencial = len(self._itens)

    def calcular_nota_fiscal(self):
        valor = 0.0
        for item in self._itens:
            valor += item.valor_item
        return valor

    def imprimir_nota_fiscal(self):
        # declarando padrão de linha

        # string de cima da nota fiscal com os dados do cliente
        dict_nf = {"Data": self._data.strftime("%d/%m/%Y"),
                   "Cliente": self._cliente.id,
                   "Nome": self._cliente.nome,
                   "CPF/CNPJ": self._cliente.cnpjcpf}

        # string do meio da nota fiscal onde mostra-se todos items e suas informações
        for item in self._itens:
            dict_nf[item.descricao] = {"Seq": item.sequencial,
                                       "Descricao": item.descricao,
                                       "QTD": item.quantidade,
                                       "Valor Unit": item.produto.valorunitario,
                                       "Preco": item.valor_item}

        dict_nf["Valor Final"] = self.calcular_nota_fiscal()

        return dict_nf
