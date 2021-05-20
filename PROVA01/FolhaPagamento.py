from Colaborador import *

COLABORADORES = set()


class FolhaPagamento:
    def __init__(self, mes, tot_descontos, tot_proventos, ano):
        self._mes = int(mes)
        self._total_descontos = float(tot_descontos)
        self._total_proventos = float(tot_proventos)
        self._ano = int(ano)
        self._movimentos = []

    def calcular_folha(self):
        linha = 120 * "-" + "\n"
        totsalarios = self._dados_folha()
        totpagar = self._total_proventos - self._total_descontos
        string = f"FOLHA DE PAGAMENTO {self._mes}/{ self._ano}"\
                 f"\n{linha}\nTotal de Salários Atual = {totsalarios} \nTotal de Proventos= {self._total_proventos}"\
                 + f"\nTotal de Descontos = {self._total_descontos}\nTotal a Pagar = {totpagar}\n{linha}"

        return "\033[01m\033[40m\033[97m{}".format(string)

    def inserir_movimento(self, move):
        if isinstance(move, MovimentoFolha):
            self._movimentos.append(move)
            self.adicionar_colaboradores(move.get_idcolaborador)

    @staticmethod
    def adicionar_colaboradores(idcolab):
        COLABORADORES.add(idcolab)

    def _dados_folha(self):
        tot_salarios = 0
        for colaborador in COLABORADORES:
            prov, desc, salar = self.dados_colaborador(colaborador)
            self._total_proventos += prov
            self._total_descontos += desc
            tot_salarios += salar
        return tot_salarios

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
