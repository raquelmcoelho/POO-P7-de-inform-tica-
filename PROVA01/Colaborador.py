from MovimentoFolha import MovimentoFolha

COLABORADORES = {}


def get_salario(idcolab):
    for colaborador in COLABORADORES:
        if colaborador == idcolab:
            return COLABORADORES[colaborador]
    else:
        return "colaborador não existente"


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
        self.adicionarcolaborador()

    def adicionarcolaborador(self):
        COLABORADORES[self._codigo] = self._salarioatual

    def calcular_salario(self, folha_pagamento):
        totproventos, totdescontos, salario= folha_pagamento.dados_colaborador(self._codigo)
        folha_pagamento_formatada = f"""
        Código: {self._codigo}  Nome: {self._nome}
        Salário Antigo:{self._salarioatual}  Salário Atual : {salario}
        Total Proventos: {totproventos}
        Total Descontos: {totdescontos} Valor Líquido a Receber: {totproventos - totdescontos}"""
        return str(folha_pagamento_formatada)

    def inserir_movimentos(self, move):
        if isinstance(move, MovimentoFolha):
            self._movimentos.append(move)
