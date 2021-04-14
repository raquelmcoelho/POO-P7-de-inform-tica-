"""
O código Morse é um esquema de
codificação que usa travessões e pontos para representar dígitos e letras.
Nesta atividade, você escreverá um programa que usa um dicionário para
armazenar o mapeamento desses símbolos para o código Morse. Use um ponto para
representar um ponto e um hífen para representar um travessão. O mapeamento de
caracteres para travessões e pontos é mostrado na Tabela definida no arquivo CodigoMorse-02.jpg.

Seu programa deve ler uma
mensagem do usuário. Em seguida, deve traduzir todas as letras e dígitos da
mensagem para o código Morse, deixando um espaço entre cada sequência de
travessões e pontos. Seu programa deve ignorar quaisquer caracteres que não
estejam listados na tabela anterior. O código Morse para Hello, World! é
mostrado abaixo no arquivo CodigoMorse-01.jpg:
"""
morse = {"a": ".-",
         "b": "-...",
         "c": "-.-.",
         "d": "-..",
         "e": ".",
         "f": ".._.",
         "g": "--.",
         "h": "....",
         "i": "..",
         "j": ".---",
         "k": "-.-",
         "l": ".-..",
         "m": "--",
         "n": "-.",
         "o": "---",
         "p": ".--.",
         "q": "--.-",
         "r": ".-.",
         "s": "...",
         "t": "-",
         "u": "..-",
         "v": "...-",
         "w": ".--",
         "x": "-..-",
         "y": "-.--",
         "z": "--..",
         "0": "-----",
         "1": ".----",
         "2": "..---",
         "3": "...--",
         "4": "....-",
         "5": ".....",
         "6": "-....",
         "7": "--...",
         "8": "---..",
         "9": "----.",
         " ": " "}


def codigomorse(mensagem):
    codigo = list(mensagem[::1])
    if set(codigo).issubset(morse):
        for i in codigo:
            print(morse[i], end=" ")
        return codigo
    else:
        return print("erro")


mens = input("mensagem:")
codigomorse(mens)
