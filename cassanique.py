
def roleta(pontuação_total=0):
    import random
    pontos = pontuação_total
    verificaçao = 0
    simbolos = ['🍒', '🍋', '🍊', '🍉', '⭐', '7️⃣']

    resultado = [random.choice(simbolos) for _ in range(3)]


    if resultado[0] == '7️⃣' and resultado[1] == '7️⃣' and resultado[2] == '7️⃣':
        pontos += 50
    elif resultado[0] == resultado[1] and resultado[1] == resultado[2]:
        pontos += 10
    elif resultado[0] == resultado[1]:
        pontos += 5
    elif resultado[0] == resultado[2]:
        pontos += 5
    elif resultado[1] == resultado[2]:
        pontos += 5
    else:
        pontos -= 5
        
    print(f"================[Pontos: {pontos} ]=========================")   
    print(f"Resultado: {' | '.join(resultado)}")
    return pontos




