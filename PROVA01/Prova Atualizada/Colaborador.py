

class Colaborador:
    def __init__(self, codigo, nome, endereco, telefone, bairro, cep, cpf, salario_atual):
        self._codigo = int(codigo)
        self._nome = str(nome)
        self._endereco = str(endereco)
        self._telefone = str(telefone)
        self._bairro = str(bairro)
        self._cep = str(cep)
        self._cpf = str(cpf)
        self._salarioatual = float(salario_atual)
        self._movimentos = []

    def calcular_salario(self, folhapagamento):
        linha = 120 * "-"
        totprov, totdesc, salario = folhapagamento.dados_por_colaborador(self._codigo)
        texto = f"""
        COLABORADOR : {self._nome}
        código: {self._codigo} 
        salário: {salario}
        total proventos: {totprov} 
        total descontos: {totdesc} 
        valor líquido a receber: {salario + totprov - totdesc}\n"""

        texto += "\033[01m\033[94m\033[107m{}".format(f""" {linha}
        DESCRIÇÃO            VALOR       TIPO\n {linha} \n""")
        for move in self._movimentos:
            texto += "%20s: %13s   -%9s\n" % (move.get_descricao, move.get_valor, move.get_tipomovimento)

        return "\033[01m\033[30m\033[107m{}".format(texto + linha)

    def inserir_movimentos(self, move):
        self._movimentos.append(move)

    @property
    def get_movimentos(self):
        return self._movimentos

    @property
    def get_id(self):
        return self._codigo

    @property
    def get_salario(self):
        return self._salarioatual
