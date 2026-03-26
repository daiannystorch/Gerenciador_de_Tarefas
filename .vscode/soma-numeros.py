soma = 0
n = 1
# while n <= 10: 
#     soma = soma + n 
#     n = n + 1
#     print (f"Soma: {soma}")
#     print (f"n: {n}")
# print( f"A soma dos números de 1 a 10 é: {soma}")

for index in range(1, 11):
    soma += index
    
# soma = sum([i for i in range(1, 11)]) aqui será o diferente em array, ou seja, a soma de 1 a 10 usando uma lista de compreensão
print( f'A soma dos números de 1 a 10 é: {soma}')