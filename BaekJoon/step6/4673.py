def d(n):
    return (n + sum((list(map(int, str(n))))))

notSelf = []

for i in range(0, 10000):
    notSelf.append(d(i))
    if (i+1) not in notSelf:
        print(i+1)
