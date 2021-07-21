import sys

word = list(map(str, sys.stdin.readline().strip().upper()))

temp = list(set(word))
manyUse = [temp[0]]

if len(temp) == 1:
    print(manyUse[0])
else:
    for i in range(1, len(temp)):
        if word.count(temp[i]) > word.count(manyUse[0]):
            manyUse.clear()
            manyUse.append(temp[i])
        elif word.count(temp[i]) == word.count(manyUse[0]):
            manyUse.append(temp[i])
        else: continue

    if len(manyUse) > 1: print("?")
    else: print(manyUse[0])