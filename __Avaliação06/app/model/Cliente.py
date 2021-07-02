"""
    Módulo cliente -
    Classe Cliente -
    Atributos:
        _id       - chave primária    - informado
        _nome     - nome do cliente   - informado
        _codigo   - codigo do cliente - informado
        _cnpjcpf  - cnpj ou cpf       - informado

"""


class Cliente:
    idcliente_atual = 0

    def __init__(self, nome, cnpjcpf, codigo):
        self._id = Cliente.idcliente_atual
        Cliente.idcliente_atual += 1
        self._nome = nome
        self._cnpjcpf = cnpjcpf
        self._codigo = codigo

    def __dict__(self):
        dict_cliente = {"ID Cliente": self._id,
                        "Código": self._codigo,
                        "Nome=": self._nome,
                        "CNPJ / CPF=": self._cnpjcpf}

        return dict_cliente

    # getters
    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def codigo(self):
        return self._codigo

    @property
    def cnpjcpf(self):
        return self._cnpjcpf

    # setters
    @nome.setter
    def nome(self, string):
        self._nome = string

    @cnpjcpf.setter
    def cnpjcpf(self, num):
        self._cnpjcpf = num

    @codigo.setter
    def codigo(self, num):
        self._codigo = num
            
    # deleters
    @nome.deleter
    def nome(self):
        self._nome = ""

    @cnpjcpf.deleter
    def cnpjcpf(self):
        self._cnpjcpf = 0

    @codigo.deleter
    def codigo(self):
        self._codigo = 0
