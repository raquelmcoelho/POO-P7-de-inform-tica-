from app.model.Cliente import *

clientes = [
    Cliente("Raquel Maciel", 100, 1),
    Cliente("Yuri Mateus", 200, 12),
    Cliente("Igor Martins", 300, 1234),
    Cliente("João da Silva", 400, 123456),
    Cliente("Ana Maria Braga", 500, 12345678),
]


def create_crud(dados):
    clientes.append(Cliente(nome=dados['nome'],
                            codigo=dados['codigo'],
                            cnpjcpf=dados['cnpjcpf']))


def read_crud():
    strings = []

    for client in clientes:
        strings.append(client.lista())

    return strings


def update_crud(dados):
    print(dados)
    for client in clientes:
        print(client.lista())
        if str(client.idcliente) == str(dados["idcliente"]):
            client.nome = dados["nome"]
            client.codigo = dados["codigo"]
            client.cnpjcpf = dados["cnpjcpf"]


def delete_crud(idcliente_inputado):
    for client in clientes:
        if str(client.idcliente) == str(idcliente_inputado):
            clientes.remove(client)
