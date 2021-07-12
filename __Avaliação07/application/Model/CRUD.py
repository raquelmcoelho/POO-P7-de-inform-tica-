from __Avaliação07.application.Model.Models import *

########################################################################################################################


def create_cliente(dados):
    nome, cnpjcpf, codigo = None, None, None
    if "nome" in dados:
        nome = dados["nome"]
    if "cnpjcpf" in dados:
        cnpjcpf = int(dados["cnpjcpf"])
    if "codigo" in dados:
        codigo = int(dados["codigo"])

    db.session.add(Cliente(nome, cnpjcpf, codigo))
    db.session.commit()
    return "Cliente criado"


def read_cliente(idcliente=None):
    if idcliente is not None:
        cliente = Cliente.query.filter_by(id=int(idcliente)).first()
        if cliente:
            return cliente.dict()
        else:
            return "Não encontrado ou existente"
    else:
        return [cliente.dict() for cliente in Cliente.query.all()]


def update_cliente(idcliente, dados):
    cliente = Cliente.query.filter_by(id=int(idcliente)).first()
    if cliente:
        if "nome" in dados:
            cliente.nome = dados["nome"]
        if "cnjcpf" in dados:
            cliente.cnpjcpf = int(dados["cnpjcpf"])
        if "codigo" in dados:
            cliente.codigo = int(dados["codigo"])

        db.session.add(cliente)
        db.session.commit()
        return "Cliente atualizado"

    else:
        return "Não encontrado ou existente"


def delete_cliente(idcliente):
    cliente = Cliente.query.filter_by(id=int(idcliente)).first()
    if cliente:
        db.session.delete(cliente)
        db.session.commit()
        return "Cliente deletado"
    else:
        return "Não encontrado ou existente"

########################################################################################################################


def create_produto(dados):
    codigo, descricao, valor_unitario = None, None, None
    if "codigo" in dados:
        codigo = int(dados["codigo"])
    if "descricao" in dados:
        descricao = dados["descricao"]
    if "valor_unitario" in dados:
        valor_unitario = float(dados["valor_unitario"])

    db.session.add(Produto(codigo, descricao, valor_unitario))
    db.session.commit()
    return "Produto criado"


def read_produto(idproduto=None):
    if idproduto is not None:
        produto = Produto.query.filter_by(id=int(idproduto)).first()
        if produto:
            return produto.dict()
        else:
            return "Não encontrado ou existente"
    else:
        return [produto.dict() for produto in Produto.query.all()]


def update_produto(idproduto, dados):
    produto = Produto.query.filter_by(id=int(idproduto)).first()
    if produto:
        if "codigo" in dados:
            produto.codigo = int(dados["codigo"])
        if "descricao" in dados:
            produto.descricao = dados["descricao"]
        if "valor_unitario" in dados:
            produto.valor_unitario = float(dados["valor_unitario"])

        db.session.add(produto)
        db.session.commit()
        return "Produto atualizado"

    else:
        return "Não encontrado ou existente"


def delete_produto(idproduto):
    produto = Produto.query.filter_by(id=int(idproduto)).first()
    if produto:
        db.session.delete(produto)
        db.session.commit()
        return "Produto deletado"
    else:
        return "Não encontrado ou existente"

########################################################################################################################


def create_nota(dados):
    codigo, cliente_id, data = None, None, None
    print(dados)
    if "codigo" in dados:
        codigo = int(dados["codigo"])
    if "cliente_id" in dados:
        cliente_id = int(dados["cliente_id"])
    if "data" in dados:
        data = dados["data"]

    db.session.add(NotaFiscal(codigo, cliente_id, data))
    db.session.commit()
    return "Nota criada"


def read_nota(idnota=None):
    if idnota:
        nota = NotaFiscal.query.filter_by(id=int(idnota)).first()
        if nota:
            return nota.dict()
        else:
            return "Não encontrado ou existente"
    else:
        return [nota.dict() for nota in NotaFiscal.query.all()]


def update_nota(idnota, dados):
    nota = NotaFiscal.query.filter_by(id=int(idnota)).first()
    if nota:
        if "codigo" in dados:
            nota.codigo = int(dados["codigo"])
        if "cliente_id" in dados:
            nota.cliente_id = int(dados["cliente_id"])
        if "data" in dados:
            nota.data = float(dados["data"])

        db.session.add(nota)
        db.session.commit()
        return "Nota atualizada"
    else:
        return "Não encontrado ou existente"


def delete_nota(idproduto):
    nota = NotaFiscal.query.filter_by(id=int(idproduto)).first()
    if nota:
        db.session.delete(nota)
        db.session.commit()
        return "Nota Fiscal deletada"
    else:
        return "Não encontrado ou existente"


########################################################################################################################


def create_item(dados):
    quantidade, produto_id, nota_id = None, None, None
    if "quantidade" in dados:
        quantidade = int(dados["quantidade"])
    if "produto_id" in dados:
        produto_id = dados["produto_id"]
    if "nota_id" in dados:
        nota_id = float(dados["nota_id"])

    db.session.add(ItemNotaFiscal(quantidade, produto_id, nota_id))
    db.session.commit()
    return "Item criado"


def read_item(iditem=None):
    if iditem:
        item = ItemNotaFiscal.query.filter_by(id=int(iditem)).first()
        if item:
            return item.dict()
        else:
            return "Não encontrado ou existente"
    else:
        return [item.dict() for item in ItemNotaFiscal.query.all()]


def update_item(iditem, dados):
    item = ItemNotaFiscal.query.filter_by(id=int(iditem)).first()
    if item:
        if "quantidade" in dados:
            item.quantidade = int(dados["quantidade"])
        if "produto_id" in dados:
            item.produto_id = int(dados["produto_id"])
        if "nota_id" in dados:
            item.nota_id = float(dados["nota_id"])

        db.session.add(item)
        db.session.commit()
        return "Item atualizado"

    else:
        return "Não encontrado ou existente"


def delete_item(iditem):
    item = ItemNotaFiscal.query.filter_by(id=int(iditem)).first()
    if item:
        db.session.delete(item)
        db.session.commit()
        return "Item deletado"
    else:
        return "Não encontrado ou existente"
