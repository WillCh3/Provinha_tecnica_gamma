
"""4. Crie duas funções:
○ A primeira função receberá dois parâmetros e retornará como resultado uma
concatenação de texto colocando uma vírgula entre os dois parâmetros ao
uní-los.
○ A segunda função não receberá parâmetros; será feito a leitura de duas
entradas que o usuário digitar; irá chamar a primeira função passando como
argumento os dois textos lidos; por fim esta segunda função irá imprimir para
o usuário informando qual foi o resultado que se obteve na chamada à
primeira função.
○ Exemplo da primeira entrada: “Olá”. Exemplo da segunda entrada: “Mundo”.
Exemplo da saída do sistema: “Olá,Mundo”."""

def unir_texto(text1, text2):
    print(f'"{text1}, {text2}"')


def entradas_texto():
    text1 = input("Digite o Primeiro texto: ")
    text2 = input("Digite o Segundo texto: ")
    unir_texto(text1, text2)

entradas_texto()