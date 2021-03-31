"""
#Lista Encadeada - cada elemento é um registro que além de obter seu dado em si
também possui um ponteiro somente para o próximo elemento da lista.
"""

linkedlist = []
n = int(input("quantos elementos terá sua LinkedList? "))
for x in range(0,n):
    linkedlist.append("vazio")


#adicionar ou substituir na posição que quiser

resposta = "sim"
while resposta != "não":
    elemento = input("adicione o elemento: ")
    position = int(input("em que posição? ")) - 1
    linkedlist.pop(position)
    linkedlist.insert(position, elemento)
    resposta = input("\ndeseja adicionar/substituir mais um?(sim/não) ")

print("\nsua LinkedList ficou assim:\n")
[print(x) for x in linkedlist]

#deletar elemento desejado
resposta = input("\ndeseja excluir algum item?(sim/não) ")

while resposta!="não":
    elemento = input("qual elemento você deseja excluir? ")
    if linkedlist.count(elemento) > 0:
        linkedlist.remove(elemento)
        print(elemento,"está sendo removido\n")
    else:
        print("inexistente")
    resposta= input("deseja excluir mais algum item?(sim/não) ")


else:
    print("\nokay, sua lista encadeada ficou assim:\n", linkedlist)

