# Esercizio numero 2
"""Cra un programma per calcolare la moltiplicazione e la somma di due numeri"""


def mol(a,b):
    return a * b


def som(a,b):
    return a + b


num1 = float(input('Inserisci il primo numero = '))
num2 = float(input('Inserisci il secondo numero = '))

print(f'Il prodotto di {num1} e {num2} è ', mol(num1, num2))
print(f'La somma di {num1} e {num2} è ', som(num1, num2))
