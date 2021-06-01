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
from cliente import Cliente
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal:
    def __init__(self, id_nota, codigo, cliente):
        self._Id = id_nota
        self._codigo = codigo
        self._cliente = self.set_cliente(cliente)
        self._data = datetime.date.today()
        self._itens = []

    @staticmethod
    def set_cliente(cliente):
        if isinstance(cliente, Cliente):
            return cliente

    def adicionar_item(self, item):
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
        
    def calcular_nota_fiscal(self):
        valor = 0.0
        for item in self._itens:
            valor += item.get_valor_item
        return valor
     
    def imprimir_nota_fiscal(self):
        # declarando padrão de linha
        linha = 120 * "-"

        # string de cima da nota fiscal com os dados do cliente
        stringclient = ("\n%3s\n NOTA FISCAL%90sData:%s\n"
                        + " Cliente:%s%12sNome:%s\n"
                        + " CPF/CNPJ:%s\n%s\n ITENS\n%s\n"
                        + " Seq%23sDescrição%26sQTD%7sValor Unit%10sPreço\n%s\n") % (linha, "",
                                                                                     self._data.strftime("%d/%m/%Y"),
                                                                                     self._cliente.get_id, "",
                                                                                     self._cliente.get_nome,
                                                                                     self._cliente.get_cnpjcpf, linha,
                                                                                     linha, "", "", "", "", linha)

        # string do meio da nota fiscal onde mostra-se todos items e suas informações
        stringprodutos = ""
        for item in self._itens:
            produto = item.get_produto
            stringprodutos += " %3s%4s%30s%24s%d%12s%3.2f%13s%5.2f\n" % (item.get_sequencial, "",
                                                                         produto.get_descricao, "",
                                                                         item.get_qtd, "",
                                                                         produto.get_valor_unitario, "",
                                                                         item.get_valor_item)

        # string final da nota fiscal onde é revelado o valor concebido pelo método .calcular_nota_fiscal()
        stringfinal = f"""%s\n VALOR TOTAL:%s\n%s""" % (linha, self.calcular_nota_fiscal(), linha)

        # pondo cor foreground, background e estilo "bold" através do format na nota fiscal e mandando as strings unidas
        notafiscal = stringclient + stringprodutos + stringfinal

        # opção de ter uma nota fiscal colorida através do format, apenas um extra
        notafiscal_colorida = "\033[01m\033[40m\033[92m{}".format(notafiscal)

        # aqui retorna a normal e a colorida e a pessoa escolhe qual quer na hora de chamar
        return notafiscal, notafiscal_colorida
