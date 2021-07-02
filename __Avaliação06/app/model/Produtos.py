from app.model.Produto import Produto


produtos = [
    Produto(100, "Arroz Namorado", 8.50),
    Produto(200, "Feijão", 5.50),
    Produto(300, "Farinha Dona Benta", 5.60),
    Produto(400, "Sabão Ypê", 11.00)
]


def create_produto(dados):
    produtos.append(Produto(codigo=dados['codigo'],
                            descricao=dados['descricao'],
                            valor_unitario=dados['valorunitario']))


def read_produto(idproduto=None):
    if idproduto is None:
        strings = []

        for produto in produtos:
            strings.append(produto.__dict__())

        return strings

    else:
        for produto in produtos:
            if str(produto.id) == str(idproduto):
                return produto.__dict__()


def update_produto(dados):
    for produto in produtos:
        if str(produto.id) == str(dados["idproduto"]):
            produto.codigo = dados["codigo"]
            produto.descricao = dados["descricao"]
            produto.valorunitario = dados["valorunitario"]


def delete_produto(idproduto):
    for produto in produtos:
        if str(produto.id) == str(idproduto):
            produtos.remove(produto)
