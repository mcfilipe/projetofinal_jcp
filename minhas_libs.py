"""
Aqui iremos colocar as bibliotecas que iremos utilizar no projeto.
"""

def ler_ficheiro(nome_do_ficheiro):
    """
    método par abrir um ficheiro em modo leitura e imprimir o conteúdo do ficheiro
    para: nome_do_ficheiro.txt
    """
    meu_ficheiro = open(nome_do_ficheiro, "r", encoding="utf-8")
    for line in meu_ficheiro:
        print(line.strip()) 
        meu_ficheiro.close()
    meu_ficheiro.close()