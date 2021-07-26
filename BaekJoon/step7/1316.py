N = int(input())
count = 0

for i in range(0, N):
    word = input()
    temp = []
    for i in range(0, len(word)):
        if word[i:i+1] in temp:
            count += 1
            break
        elif word[i:i+1] != word[i+1:i+2]: temp.append(word[i])

print(N-count)

