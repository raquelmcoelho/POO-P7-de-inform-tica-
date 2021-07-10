from flask import Response, request
import json
from __Avaliação07.aplicattion import app
from __Avaliação07.aplicattion.Model.CRUD import *


def gera_response(status, nome_conteudo, conteudo, mensagem=None):
    body = {nome_conteudo: conteudo}
    if mensagem:
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")


@app.route("/")
def index():
    return 'Página Index'


@app.route("/api/clientes", methods=["GET"])
def get_clientes():
    return gera_response(200, "Ler Clientes", read_cliente())


@app.route("/api/cliente/<int:idcliente>", methods=["GET"])
def get_cliente_id(idcliente):
    return gera_response(200, "Ler cliente", read_cliente(idcliente))


@app.route("/api/cliente", methods=["POST"])
def post_cliente():
    body = request.get_json()
    try:
        return gera_response(201, "Criar novo cliente", create_cliente(body), "Sucesso")

    except Exception:
        return gera_response(400, "Criar novo cliente", {}, "Erro")


@app.route("/api/cliente/<int:idcliente>", methods=["PUT"])
def put_cliente_id(idcliente):
    body = request.get_json()
    try:
        return gera_response(200, "Atualização do Cliente", update_cliente(idcliente, body), "Sucesso")

    except Exception:
        return gera_response(400, "Atualização do Cliente", {}, "Erro")


@app.route("/api/cliente/<int:idcliente>", methods=["DELETE"])
def delete_cliente_id(idcliente):
    try:
        return gera_response(200, "Delete do Cliente", delete_cliente(idcliente), "Deletado com sucesso")

    except Exception:
        return gera_response(200, "Delete do Cliente", {}, "Erro ao deletar")


"""
  PRODUTO ROUTES
  get    api/produtos       : Ler todos os produtos
  get    api/produto/{id}   : Ler um produto
  post   api/produto        : Cria um novo produto
  put    api/produto/{id}   : Atualiza um produto
  delete api/produto/{id}   : Exclui um produto
"""


@app.route("/api/produtos", methods=["GET"])
def get_produtos():
    return gera_response(200, "Ler todos os Produtos", read_produto())


@app.route("/api/produto/<int:idproduto>", methods=["GET"])
def get_produto_id(idproduto):
    return gera_response(200, "Ler produto", read_produto(idproduto))


@app.route("/api/produto", methods=["POST"])
def post_produto():
    body = request.get_json()
    try:
        return gera_response(201, "Criar novo produto", create_produto(body), "Sucesso")

    except Exception:
        return gera_response(400, "Criar novo produto", {}, "Erro")


@app.route("/api/produto/<int:idproduto>", methods=["PUT"])
def put_produto_id(idproduto):
    body = request.get_json()
    try:
        return gera_response(200, "Atualização do Produto", update_produto(idproduto, body), "Sucesso")

    except Exception:
        return gera_response(400, "Atualização do Produto", {}, "Erro")


@app.route("/api/produto/<int:idproduto>", methods=["DELETE"])
def delete_produto_id(idproduto):
    try:
        return gera_response(200, "Delete do Produto", delete_produto(idproduto), "Deletado com sucesso")

    except Exception:
        return gera_response(200, "Delete do Produto", {}, "Erro ao deletar")


"""
  NOTA FISCAL ROUTES

  get    api/notasfiscais     : ler todas as notas fiscais
  get    api/notafiscal/{id}  : Ler uma nota fiscal
  post   api/notafiscal       : Cria uma nota fiscal
  put    api/notafiscal/{id}  : Atualiza uma nota fiscal
  delete api/notafiscal/{id}  : Exclui uma nota fiscal
  get    api/calculanf/{id}   : Calcula o valor da nota fiscal
  get    api/imprimenf/{id}   : Imprime uma nota fiscal
"""


@app.route("/api/notasfiscais", methods=["GET"])
def get_notasfiscais():
    return gera_response(200, "Ler todos as Notas Finais", read_nota())


@app.route("/api/notafiscal/<int:idnota>", methods=["GET"])
def get_notafiscal_id(idnota):
    return gera_response(200, "Ler Nota", read_nota(idnota))


@app.route("/api/notafiscal", methods=["POST"])
def post_notafiscal():
    body = request.get_json()
    try:
        return gera_response(201, "Criar nova Nota Fiscal", create_nota(body), "Sucesso")

    except Exception:
        return gera_response(400, "Criar nova Nota Fiscal", {}, "Erro")


@app.route("/api/notafiscal/<int:idnota>", methods=["PUT"])
def put_notafiscal_id(idnota):
    body = request.get_json()
    try:
        return gera_response(200, "Atualização da Nota", update_nota(idnota, body), "Sucesso")

    except Exception:
        return gera_response(400, "Atualização da Nota", {}, "Erro")


@app.route("/api/notafiscal/<int:idnota>", methods=["DELETE"])
def delete_notafiscal_id(idnota):
    try:
        return gera_response(200, "Delete da Nota", delete_nota(idnota), "Deletado com sucesso")

    except Exception:
        return gera_response(200, "Delete da Nota", {}, "Erro ao deletar")


@app.route("/api/calculanf/<int:idnota>", methods=["GET"])
def get_calculanf_id(idnota):
    nota = NotaFiscal.query.filter_by(id=idnota).first()

    return gera_response(200, "Calcular Nota Fiscal", nota.calcula_nota())


@app.route("/api/imprimenf/<int:idnota>", methods=["GET"])
def get_imprimenf_id(idnota):
    nota = NotaFiscal.query.filter_by(id=idnota).first()
    return gera_response(200, "Imprimir Nota Fiscal", nota.imprime_nota())



"""
  ITEM NOTA FISCAL ROUTES

  get    api/itensnf/{id}    : Ler todos os itens de uma nota fiscal
  get    api/itemnf/{id}     : Ler um item de nota fiscal
  post   api/itemnf          : Cria um novo item de nota fiscal
  put    api/itemnf/{id}     : Atualiza um item de nota fiscal
  delete api/itemnf/{id}     : Exclui um item de nota fiscal
"""

@app.route("/api/itensnf/<int:idnota>", methods=["GET"])
def get_itensnf(idnota):
    return gera_response(200, "Ler todos os Itens da Nota Fiscal", read_nota(idnota)["Itens"])


@app.route("/api/itemnf/<int:iditem>", methods=["GET"])
def get_itemnf_id(iditem):
    return gera_response(200, "Ler Item", read_item(iditem))


@app.route("/api/itemnf", methods=["POST"])
def post_itemnf():
    body = request.get_json()
    try:
        return gera_response(201, "Criar novo Item", create_item(body), "Sucesso")

    except Exception:
        return gera_response(400, "Criar novo Item", {}, "Erro")


@app.route("/api/itemnf/<int:iditem>", methods=["PUT"])
def put_itemnf_id(iditem):
    body = request.get_json()
    try:
        return gera_response(200, "Atualização do Item", update_item(iditem, body), "Sucesso")

    except Exception:
        return gera_response(400, "Atualização do Item", {}, "Erro")


@app.route("/api/itemnf/<int:iditem>", methods=["DELETE"])
def delete_itemnf_id(iditem):
    try:
        return gera_response(200, "Delete do Item", delete_item(iditem), "Deletado com sucesso")

    except Exception:
        return gera_response(200, "Delete do Item", {}, "Erro ao deletar")
