from app.model.Cliente import *

clientes = [
    Cliente("Raquel Maciel", 100, 1),
    Cliente("Yuri Mateus", 200, 12),
    Cliente("Igor Martins", 300, 1234),
    Cliente("João da Silva", 400, 123456),
    Cliente("Ana Maria Braga", 500, 12345678),
]


def create_cliente(dados):
    clientes.append(Cliente(nome=dados['nome'],
                            codigo=dados['codigo'],
                            cnpjcpf=dados['cnpjcpf']))


def read_cliente(idcliente=None):
    if idcliente is None:
        strings = []

        for client in clientes:
            strings.append(client.__dict__())

        return strings

    else:
        for client in clientes:
            if str(client.id) == str(idcliente):
                return client.__dict__()


def update_cliente(dados):
    for client in clientes:
        if str(client.id) == str(dados["idcliente"]):
            client.nome = dados["nome"]
            client.codigo = dados["codigo"]
            client.cnpjcpf = dados["cnpjcpf"]


def delete_cliente(idcliente_inputado):
    for client in clientes:
        if str(client.id) == str(idcliente_inputado):
            clientes.remove(client)
