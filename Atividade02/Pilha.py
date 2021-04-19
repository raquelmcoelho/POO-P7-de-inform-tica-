#Pilha - LIFO(last in first out)

pilha = []
n = int(input("quantos elementos vai ter na sua pilha? "))

#adicionar na head
while len(pilha) < n:
    a = input("adicione um elemento a pilha: ")
    pilha.insert(0, a)

print("sua pilha está nesta ordem:\n")
[print(x) for x in pilha]

#retirar na head
n1= input("\nqual elemento você quer acessar? ")
excluir = 0

for i in range(len(pilha)):
    if pilha[i] != n1:
        print("retirando item:", pilha[i])
        excluir +=1
    else:
        print("viva! conseguimos acessar seu elemento:", pilha[i])
        break


[pilha.pop(0) for x in range(0,excluir)]
print("\nagora a pilha está assim:\n")
[print(x) for x in pilha]


#só consegue acessar o que está no final se ir tirando todos os do topo