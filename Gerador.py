import random
import string
from time import sleep

Continuar = "S"

while(Continuar == "S"):

    print(20*"=")
    print("Gerador de senhas".center(20))
    print(20*"=")

    Caracteres = ""
    Tamanho = 0

    Resposta_Numeros = input("Você deseja que sua senha tenha números? (s/n) ").upper()

    if len(Resposta_Numeros) == 1:
        if Resposta_Numeros == "S":
            Caracteres += string.digits
    else:
        print("Resposta Incorreta")
        continue

    Resposta_CarEspecial = input("Você deseja que sua senha tenha caracteres especiais? (s/n) ").upper()

    if len(Resposta_CarEspecial):
        if Resposta_CarEspecial == "S":
            Caracteres += "!@#$%^&*()_+=-.,"
    else:
        print("Resposta Incorreta")
        continue
    
    Resposta_Letras = input("Você deseja que sua senha tenha letras? (s/n) ").upper()

    if len(Resposta_Letras):
        if Resposta_Letras == "S":
            Caracteres += string.ascii_lowercase + string.ascii_uppercase
    else:
        print("Resposta Incorreta")
        continue

    QuantidadeDeCaracteres = 0

    for Caractere in Caracteres:
        QuantidadeDeCaracteres += 1

    
    Tamanho = int(input(f"Qual será o tamanho da sua senha?\nO tamanho não pode ser maior que {QuantidadeDeCaracteres}! ").upper())

    if Tamanho <= QuantidadeDeCaracteres:
        print("Gerando senha...")

        Senha = "".join(random.sample(Caracteres, Tamanho))

        sleep(1.5)

        print(f"Sua senha gerada foi: {Senha}")

        Continuar = input("Você deseja gerar outra senha? (s/n) ").upper()
    else:
        print("Você ecedeu o limite do tamanho da senha!")
        
        Continuar = input("Você deseja gerar outra senha? (s/n) ").upper()