from FolhaPagamento import *

# folhas de pagamento
FP = FolhaPagamento(9, 0, 0, 2019)

# folhas colaboradores
CL01 = Colaborador("100", "Manoel Claudino", "Av 13 de Maio 2081", "88671020", "Benfica", "60020-060",
                   "124543556-89", 4500.00)
CL02 = Colaborador("200", "Carmelina da Silva", "Avenida dos Expedicionários 1200", "3035-1280", "Aeroporto",
                   "60530-020", "301789435-54", 2500.00)
CL03 = Colaborador("300", "Gurmelina Castro Saraiva", "Av João Pessoa 1020", "3235-1089", "Damas", "60330-090",
                   "350245632-76", 3000.00)
# movimentofolha
# ele já insere o movimento no colaborador automaticamente
MF01 = MovimentoFolha(CL01, "Gratificação", 4500.00, "P")
MF02 = MovimentoFolha(CL01, "Plano Saúde", 1000.00, "P")
MF03 = MovimentoFolha(CL01, "Pensão", 600.00, "D")
MF04 = MovimentoFolha(CL02, "Gratificação", 2500.00, "P")
MF05 = MovimentoFolha(CL02, "Plano Saúde", 1000.00, "P")
MF06 = MovimentoFolha(CL02, "Faltas", 600.00, "D")
MF07 = MovimentoFolha(CL03, "Gratificação", 4500.00, "P")
MF08 = MovimentoFolha(CL03, "Plano Saúde", 1000.00, "P")
MF09 = MovimentoFolha(CL03, "Pensão", 600.00, "D")

# inserindo movimentos
FP.inserir_movimento(MF01)
FP.inserir_movimento(MF02)
FP.inserir_movimento(MF03)
FP.inserir_movimento(MF04)
FP.inserir_movimento(MF05)
FP.inserir_movimento(MF06)
FP.inserir_movimento(MF07)
FP.inserir_movimento(MF08)
FP.inserir_movimento(MF09)


if __name__ == '__main__':
    print(CL01.calcular_salario(FP))
    print(CL02.calcular_salario(FP))
    print(CL03.calcular_salario(FP))

    print(FP.calcular_folha())
