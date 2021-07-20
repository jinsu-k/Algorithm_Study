import sys

def oneNumber(N):
    numList = list(map(int, str(N)))
    d = numList[0] - numList[1]
    for i in range(1, (len(numList)-1)):
        if((numList[i]-d)==numList[i+1]): return True
        else: return False 

N = sys.stdin.readline()
count = 99        

if(int(N) <= 1000):
    if(int(N) < 100):
        print(N)
    else:
        for i in range(100, (int(N)+1)):
            if(oneNumber(i) == True): count += 1
        print(count)
