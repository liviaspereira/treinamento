"""Crie uma função com dois argumentos que retornará uma matriz dos primeiros (n) múltiplos de (x).

Suponha que tanto o número dado quanto o número de vezes a contar serão números positivos maiores que 0.

Retorne os resultados como um array (ou lista em Python, Haskell ou Elixir)."""

def count_by(x, n):
    lista = []
    for i in range(x, (n * x) + 1, x):
        lista.append(i)
    return lista

print(count_by(100, 5))
