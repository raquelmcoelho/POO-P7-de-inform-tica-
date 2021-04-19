"""
Se você tiver 3 canudos, possivelmente de comprimentos diferentes, pode ou não ser possível colocá-los de forma que
formem um triângulo quando suas pontas se tocam. Por exemplo, se todos os canudos têm um comprimento de 6 cm , então
pode-se facilmente construir um triângulo equilátero usando-os. No entanto, se um canudo tiver 15 centímetros de
comprimento, enquanto os outros dois têm apenas 5 centímetros de comprimento, então um triângulo não pode ser formado.
Mais geralmente, se qualquer comprimento for maior ou igual à soma dos outros dois, os comprimentos não podem ser usados
para formar um triângulo. Caso contrário, eles podem formar um triângulo.
Escreva uma função que determine se três comprimentos podem ou não formar um triângulo. A função terá 3 parâmetros e
retornará um resultado booleano. Se qualquer um dos comprimentos for menor ou igual a 0, sua função deve retornar False.
Caso contrário, deve determinar se os comprimentos podem ou não ser usados para formar um triângulo usando o
método descrito no parágrafo anterior e retornar o resultado apropriado.
Além disso, escreva um programa que leia 3 valores inteiros de tamanhos informados do usuário e demonstre o
comportamento de sua função.
"""


def triangulopossivel(l1, l2, l3):
    lista = [float(l1), float(l2), float(l3)]
    # checa se tem zero
    if lista.count(0.0) != 0:
        return 0, print("um é zero :(")
    # checa se um lado é maior ou igual a soma dos outros dois
    for i, j in enumerate(lista):
        if j >= sum(lista) - j:
            return 0, print(f"o lado {j} é maior que os outros 2 lados")
    # se não achar erros então é possível
    return 1, print("é possível sim")


lado1, lado2, lado3 = input("3 lados do triângulo:\n").split(" ")
triangulopossivel(lado1, lado2, lado3)
