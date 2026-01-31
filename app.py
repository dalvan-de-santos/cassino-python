from menu import menuOp
from cassanique import roleta
import os

pontuação_total = 10
while True:
    menuOp()
    choice = int(input('Digite o número da opção desejada: '))
    os.system('cls')

    #Roleta
    if choice == 1:
        while True:
         pontuação_total = roleta(pontuação_total)
         choice_roleta = input('Deseja jogar novamente? (S/n): ')
         if choice_roleta.lower() == 'n':
            os.system('cls')
            break
         
         elif pontuação_total < 5:
            print("Você não tem pontos suficientes para continuar jogando na roleta.")
            input("Pressione Enter para voltar ao menu principal.")
            os.system('cls')
            break
            
         