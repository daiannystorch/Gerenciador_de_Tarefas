count = 0
for n1 in range(10):
    for n2 in range(10):
        if n2 == n1:
            continue
        for n3 in range(10):
            if n3 == n1 or n3 == n2:
                continue
            for n4 in range(10):
                if n4 == n1 or n4 == n2 or n4 == n3:
                    continue
                count += 1

print(count)

