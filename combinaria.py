# Quantos números de 4 dígitos eu posso formar com números de 0 a 9?

count = 0
for n1 in range(10):
    for n2 in range(10):
        for n3 in range(10):
            for n4 in range(10):
                count += 1 #cada vez que conta, vai pra próxima (mais 1)

print(count)

