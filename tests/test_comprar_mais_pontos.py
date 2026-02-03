from src.comprar import pontos_comprar
import pytest




def test_comprar_pontos_positivos(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '20')
    pontos = pontos_comprar()
    assert pontos == 20


def test_comprar_pontos_zero(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '0')
    pontos = pontos_comprar()
    assert pontos == 0

def test_comprar_pontos_negativos(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '-10')
    pontos = pontos_comprar()
    assert pontos == 0