#Fila - FIFO(first in first out)

fila = []
n = int(input("quantos elementos terá sua fila? "))

#adicionar no tail
while len(fila) < n:
    elemento = input("adicione o elemento: ")
    fila.append(elemento)

print("sua fila agora está assim:")
[print(x) for x in fila]

#retirar na head
n1 = int(input("quantos elementos você deseja retirar?"))
for x in range(0, n1):
     print("estamos retirando o elemento: ", fila[0])
     fila.pop(0)

print("\nagora sua fila está assim")
[print(x) for x in fila]