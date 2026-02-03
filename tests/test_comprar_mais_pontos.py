from src.comprar import pontos_comprar
import pytest
from src.app import codigo_compra


def test_comprar_pontos_positivos(monkeypatch):
    inputs = iter(['20', 'XYZ123', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    
    pontos = pontos_comprar()
    assert pontos == 20


def test_comprar_pontos_zero(monkeypatch):
    inputs = iter(['0', 'XYZ123', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    
    pontos = pontos_comprar()
    assert pontos == 0

def test_comprar_pontos_negativos(monkeypatch):
    inputs = iter(['-10', 'XYZ123', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    
    pontos = pontos_comprar()
    assert pontos == 0