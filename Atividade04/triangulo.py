"""
O triângulo pode ser classificado com base no comprimento de
seus lados em equilátero, isósceles ou escaleno. Todos os três lados de um
triângulo equilátero têm o mesmo comprimento. Um triângulo isósceles tem dois
lados que são do mesmo comprimento e um terceiro lado que é diferente comprimento.
Se todos os lados tiverem comprimentos diferentes, o triângulo é escaleno.  Escreva um programa que leia os comprimentos
dos três lados de um triângulo do usuário. Em seguida, exiba uma mensagem que
declara o tipo do triângulo.
"""


def triangulo():
    l1, l2, l3 = (input("insira os três lados de um triângulo pondo espaço entre eles:\n").split(" "))
    l1, l2, l3 = float(l1), float(l2), float(l3),
    # equilátero
    if l1 == l2 and l2 == l3:
        print("esse triângulo é equilátero")
    # escaleno
    elif l1 != l2 and l2 != l3 and l3 != l1:
        print("esse triângulo é escaleno")
    # isósceles
    else:
        print("esse triângulo é isósceles")


triangulo()
