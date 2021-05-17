"""
    Módulo cliente -
    Classe Cliente - 
    Atributos:
        _id       - chave primária    - informado
        _nome     - nome do cliente   - informado
        _codigo   - codigo do cliente - informado
        _cnpjcpf  - cnpj ou cpf       - informado
        _tipo     - tipo do cliente   - informado
                    (Pessoa Fisica ou Juridica)
        
"""


class Cliente:
    def __init__(self, idclient, nome, codigo, cnpjcpf):
        self._id = idclient
        self._nome = nome
        self._codigo = codigo
        self._cnpjcpf = cnpjcpf

    @property
    def get_nome(self):
        return self._nome

    @property
    def get_cnpjcpf(self):
        return self._cnpjcpf

    @property
    def get_id(self):
        return self._id
