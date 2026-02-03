from menu import menuOp
from cassanique import roleta
from comprar import pontos_comprar
from painel_jogador import painel
import os

codigo_compra = 'XYZ123'  # Código fixo para a compra de pontos
pontuação_total = 0
while True:
    menuOp()
    painel(pontuação_total)
    
    try:
      choice = int(input('Digite o número da opção desejada: '))
      os.system('cls')

      #Roleta
      if choice == 1:
         while True:

            if pontuação_total < 5:
                  print("Você não tem pontos suficientes para continuar jogando na roleta.")
                  input("Pressione Enter para voltar ao menu principal.")
                  os.system('cls')
                  break
            
            pontuação_total = roleta(pontuação_total)
            
            choice_roleta = input('Deseja jogar novamente? (S/n): ')
            if choice_roleta.lower() == 'n':
                  os.system('cls')
                  break
            
            
      elif choice == 2:
          pontuação_total += pontos_comprar()
          os.system('cls')
    except ValueError:
          print("Por favor, insira um número válido.")
         
      
            
      
