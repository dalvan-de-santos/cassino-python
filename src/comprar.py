
def pontos_comprar():
    try:
        pontos = int(input("Quantos pontos você deseja comprar? "))
        if pontos > 0:
            print(f"Você comprou {pontos} pontos com sucesso!")
            input("Pressione Enter para voltar ao menu principal.")
            return pontos
        else:
            print("Por favor, insira um número positivo.")
            input("Pressione Enter para voltar ao menu principal.")
            return 0
        
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
        input("Pressione Enter para voltar ao menu principal.")
        return 0