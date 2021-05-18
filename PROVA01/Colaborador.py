from MovimentoFolha import MovimentoFolha


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

    def inserir_movimentos(self, move):
        if isinstance(move, MovimentoFolha):
            self._movimentos.append(move)

    def separar_movimentos(self):
        proventos = {}
        descontos = {}
        for movimento in self._movimentos:
            if movimento.get_tipomovimento == "Provento":
                proventos[movimento.get_descricao] = movimento.get_valor

            elif movimento.get_tipomovimento == "Desconto":
                descontos[movimento.get_descricao] = movimento.get_valor

        return proventos, descontos

    def calcular_salario(self, folha_pagamento):
        linha = 120 * "-" + "\n"
        totproventos, totdescontos, salario = folha_pagamento.dados_colaborador(self._codigo)

        folha_pagamento_formatada = f"{linha}\nCódigo: {self._codigo}\nNome: {self._nome}" \
                                    + f"\nSalário Antigo: {self._salarioatual}\nSalário Atual: {salario}" \
                                    + f"\nTotal Proventos: {totproventos}\nTotal Descontos: {totdescontos}" \
                                    + f"\nValor Líquido a Receber: {totproventos - totdescontos}\n{linha}"

        proventos, descontos = self.separar_movimentos()
        folha_pagamento_formatada += "%s%8sDESCRIÇÃO%15sVALOR%15sTIPO\n%s" % (linha, "", "", "", linha)

        for provento in proventos:
            folha_pagamento_formatada += "%15s:%15s%7s%15s-PROVENTO\n" % (provento, "", proventos[provento], "")

        for desconto in descontos:
            folha_pagamento_formatada += "%15s:%15s%7s%15s-DESCONTO\n" % (desconto, "", descontos[desconto], "")

        return "\033[01m\033[107m\033[30m{}".format(folha_pagamento_formatada)