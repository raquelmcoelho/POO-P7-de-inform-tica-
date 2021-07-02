from app.model.NotaFiscal import NotaFiscal
from app.model.Clientes import clientes
from app.model.ItensNotaFiscal import itens

notas = [
    NotaFiscal(100, clientes[0]),
    NotaFiscal(200, clientes[1]),
    NotaFiscal(300, clientes[2]),
    NotaFiscal(400, clientes[3])
]

notas[0].adicionar_item(itens[0])

notas[1].adicionar_item(itens[0])
notas[1].adicionar_item(itens[1])

notas[2].adicionar_item(itens[0])
notas[2].adicionar_item(itens[1])
notas[2].adicionar_item(itens[2])

notas[3].adicionar_item(itens[0])
notas[3].adicionar_item(itens[1])
notas[3].adicionar_item(itens[2])
notas[3].adicionar_item(itens[3])


def create_nota(dados):
    notas.append(NotaFiscal(codigo=dados['codigo'],
                            cliente=clientes[int(dados['idcliente'])]))


def read_nota(idnota=None):
    if idnota is None:
        strings = []

        for nota in notas:
            strings.append(nota.__dict__())

        return strings

    else:
        for nota in notas:
            if str(nota.id) == str(idnota):
                return nota.__dict__()


def update_nota(dados):
    for nota in notas:
        if str(nota.id) == str(dados["idnota"]):
            nota.codigo = dados["codigo"]
            nota.cliente = clientes[int(dados["idcliente"])]


def delete_nota(idnota):
    for nota in notas:
        if str(nota.id) == str(idnota):
            notas.remove(nota)


def calcula(idnota):
    for nota in notas:
        if str(nota.id) == str(idnota):
            return nota.calcular_nota_fiscal()


def imprime(idnota):
    for nota in notas:
        if str(nota.id) == str(idnota):
            return nota.imprimir_nota_fiscal()
