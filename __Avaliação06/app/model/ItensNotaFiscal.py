from app.model.ItemNotaFiscal import ItemNotaFiscal
from app.model.Produtos import produtos

itens = [
    ItemNotaFiscal(5, produtos[0]),
    ItemNotaFiscal(5, produtos[1]),
    ItemNotaFiscal(5, produtos[2]),
    ItemNotaFiscal(5, produtos[3]),
]


def create_item(dados):
    itens.append(ItemNotaFiscal(quantidade=int(dados['quantidade']),
                                produto_object=produtos[dados['idproduto']]))


def read_item(iditem=None):
    if iditem is None:
        strings = []

        for item in itens:
            strings.append(item.__dict__())

        return strings

    else:
        for item in itens:
            if str(item.id) == str(iditem):
                return item.__dict__()


def update_item(dados):
    for item in itens:
        if str(item.id) == str(dados["iditem"]):
            item.quantidade = int(dados["quantidade"])
            item.produto = produtos[int(dados["idproduto"])]


def delete_item(iditem):
    for item in itens:
        if str(item.id) == str(iditem):
            itens.remove(item)
