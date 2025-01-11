#Importar a biblioteca necessária: Use a biblioteca random para selecionar caracteres aleatórios.

#Definir os conjuntos de caracteres:

#Letras minúsculas: abcdefghijklmnopqrstuvwxyz
#Letras maiúsculas: ABCDEFGHIJKLMNOPQRSTUVWXYZ
#Números: 0123456789
#Símbolos: !@#$%^&*()-_=+
#Obter as preferências do usuário:

#Perguntar o tamanho da senha.
#Confirmar os tipos de caracteres a serem incluídos.
#Gerar a senha:

#Combine os conjuntos escolhidos pelo usuário.
#Use random.choice() para selecionar caracteres aleatórios e formar a senha.
#Exibir a senha gerada.

import random

print("Bem Vindo ao keygeneratorD")

def gerador_senhas():

    letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
    letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros= "0123456789"
    simbolos = "!@#$%^&*()-_=+"

    comprimento = (input("Digite o comprimento da senha: "))

    if not comprimento.isdigit():
        print("Erro: Sem um número é impossível gerar uma senha")
        return  
      
    comprimento = int (comprimento)
    limite_maximo = 12
    
    if comprimento <= 0 or comprimento > limite_maximo:
        print("Erro: Digite um número INTEIRO válido com no maximo 12 caracteres")
        return

    adicionar_minusculas = input('Deseja adicionar letras minusculas?("s/n")\n').lower() == "s" 
    adicionar_maiusculas = input('Deseja adicionar letras maiusculas?("s/n")\n').lower() == "s"
    adicionar_numeros =input('Deseja adicionar numeros?("s/n") \n').lower() == "s"
    adicionar_simbolos = input('Deseja adicionar simbolos?("s/n") \n').lower() == "s"

    caracteres = ""
    if adicionar_minusculas:
        caracteres += letras_minusculas
    if adicionar_maiusculas:
        caracteres += letras_maiusculas
    if adicionar_numeros:
        caracteres += numeros
    if adicionar_simbolos:
        caracteres += simbolos

    if not caracteres:
        print("sem caracteres, sem senha palhaço")
        return

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    print(f"Senha gerada: {senha}")

gerador_senhas()

