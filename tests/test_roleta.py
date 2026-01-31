
def test_roleta():
    pontos = 0

    resultado_point = ['7️⃣', '7️⃣', '7️⃣']
    if resultado_point[0] == '7️⃣' and resultado_point[1] == '7️⃣' and resultado_point[2] == '7️⃣':
        pontos += 50
    assert pontos == 50
    pontos = 0

    resultado_tres_iguais = ['🍒', '🍒', '🍒']

    if resultado_tres_iguais[0] == resultado_tres_iguais[1] and resultado_tres_iguais[1] == resultado_tres_iguais[2]:
        pontos += 10
    assert pontos == 10

    pontos = 0
    resultado_primeiro_segundo_iguais = ['🍋', '🍋', '🍊']
    if resultado_primeiro_segundo_iguais[0] == resultado_primeiro_segundo_iguais[1]:
        pontos += 5
    assert pontos == 5
    
    pontos = 0
    resultado_primeiro_ultimo_iguais = ['🍉', '🍊', '🍉']
    if resultado_primeiro_ultimo_iguais[0] == resultado_primeiro_ultimo_iguais[2]:
        pontos += 5
    assert pontos == 5
    
    pontos = 0
    resultado_segundo_ultimo_iguais = ['🍒','⭐', '⭐']
    if resultado_segundo_ultimo_iguais[1] == resultado_segundo_ultimo_iguais[2]:
        pontos += 5
    assert pontos == 5
    