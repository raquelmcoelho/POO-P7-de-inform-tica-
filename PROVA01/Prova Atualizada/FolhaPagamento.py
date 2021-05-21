from Colaborador import Colaborador
from MovimentoFolha import MovimentoFolha


class FolhaPagamento:
    def __init__(self, mes, tot_descontos, tot_proventos, ano):
        self._mes = int(mes)
        self._total_descontos = float(tot_descontos)
        self._total_proventos = float(tot_proventos)
        self._ano = int(ano)
        self._movimentos = []
        self._colaboradores = set()

    def calcular_folha(self):
        linha = 120 * "-"
        tot_salarios = self.dados_folha()
        tot_pagar = tot_salarios + self._total_proventos - self._total_descontos
        texto = f""" {linha}
        Total de Salários: {tot_salarios}
        Total de Proventos: {self._total_proventos}
        Total de Descontos: {self._total_descontos}
        Total a Pagar: {tot_pagar} \n {linha}
        """
        return "\033[01m\033[40m\033[97m{}".format(texto)

    def inserir_movimento(self, move):
        if isinstance(move, MovimentoFolha):
            self._movimentos.append(move)
            colab = move.get_colaborador
            self.inserir_colaborador(colab)
            colab.inserir_movimentos(move)

    def inserir_colaborador(self, colab):
        if isinstance(colab, Colaborador):
            self._colaboradores.add(colab)

    def dados_por_colaborador(self, colab):
        for colaborador in self._colaboradores:
            if colaborador.get_id == colab:
                tot_proventos = 0
                tot_descontos = 0
                salario = colaborador.get_salario

                movimentos = colaborador.get_movimentos
                for move in movimentos:
                    if move.get_tipomovimento == "Provento":
                        tot_proventos += move.get_valor
                    elif move.get_tipomovimento == "Desconto":
                        tot_descontos += move.get_valor

                return tot_proventos, tot_descontos, salario

    def dados_folha(self):
        tot_salarios = 0
        for colaborador in self._colaboradores:
            prov, desc, sal = self.dados_por_colaborador(colaborador.get_id)
            self._total_proventos += prov
            self._total_descontos += desc
            tot_salarios += sal

        return tot_salarios
