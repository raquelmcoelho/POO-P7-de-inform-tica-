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


def codigomorse():
    morse = {97: ".-", 98: "-...", 99: "-.-.", 100: "-..", 101: ".", 102: ".._.",  103: "--.",  104: "....",
             105: "..", 106: ".---", 107: "-.-", 108: ".-..", 109: "--", 110: "-.", 111: "---", 112: ".--.",
             113: "--.-", 114: ".-.", 115: "...", 116: "-", 117: "..-", 118: "...-", 119: ".--", 120: "-..-",
             121: "-.--", 122: "--..", 48: "-----", 49: ".----", 50: "..---", 51: "...--", 52: "....-",
             53: ".....", 54: "-....", 55: "--...", 56: "---..", 57: "----.", 255: "/"}
    codigo = " ".join(input("Escreva uma mensagem e eu a traduzirei para o código morse:\n").lower())
    print(codigo.translate(morse))


codigomorse()
