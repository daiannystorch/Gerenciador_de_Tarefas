#Se eu jogar dois dados 1000x, quantas vezes dará a soma de 7?

import random

numero_de_vezes = 0

for _ in range (1000):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    if soma == 7:
        numero_de_vezes += 1
print(f"O número 7 apareceu {numero_de_vezes} vezes em 1000 lançamentos.")