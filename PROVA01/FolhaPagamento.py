from Colaborador import *


class FolhaPagamento:
    def __init__(self, mes, tot_descontos, tot_proventos, ano):
        self._mes = int(mes)
        self._total_descontos = float(tot_descontos)
        self._total_proventos = float(tot_proventos)
        self._ano = int(ano)
        self._movimentos = []

    def calcular_folha(self):
        totproventos, totdescontos, totsalariospadrao, totsalarios = self._dados_folha()
        totpagar = totproventos + totsalarios - totdescontos
        string = f"""
         Total de Salários Antes = {totsalariospadrao}
         Total de Salários Atual = {totsalarios} 
         Total de Proventos= {totproventos}
         Total de Descontos = {totdescontos}
         Total a Pagar = {totpagar}"""
        return string

    def inserir_movimento(self, move):
        if isinstance(move, MovimentoFolha):
            self._movimentos.append(move)

    def _dados_folha(self):
        tot_proventos = 0
        tot_descontos = 0
        tot_salarios = {0}
        tot_salariosatuais = 0
        for movimento in self._movimentos:
            if movimento.get_tipomovimento == "Provento":
                tot_proventos += movimento.get_valor

            elif movimento.get_tipomovimento == "Desconto":
                tot_descontos += movimento.get_valor

            if movimento.get_descricao == "Salario":
                tot_salariosatuais += movimento.get_valor

            tot_salarios.add(get_salario(movimento.get_idcolaborador))

        return tot_proventos, tot_descontos, sum(tot_salarios), tot_salariosatuais

    def dados_colaborador(self, idcolab):
        tot_proventos = 0
        tot_descontos = 0
        salarioatual = 0
        for movimento in self._movimentos:
            if movimento.get_idcolaborador == idcolab:

                if movimento.get_tipomovimento == "Provento":

                    tot_proventos += movimento.get_valor

                elif movimento.get_tipomovimento == "Desconto":
                    tot_descontos += movimento.get_valor

                if movimento.get_descricao == "Salario":
                    salarioatual = movimento.get_valor

        return tot_proventos, tot_descontos, salarioatual
