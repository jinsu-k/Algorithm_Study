'''
문제:
    - 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
입력:
    - 입력은 여러 개의 테스트 케이스로 이루어져 있다.
    - 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
    - 입력의 마지막에는 0 두 개가 들어온다.
출력:
    - 각 테스트 케이스마다 A+B를 출력한다.
제한:
1 1
2 3
3 4
9 8
5 2
0 0
'''

import sys
C_list = []
i = 0
while True:
    A,B = sys.stdin.readline(10).rsplit()
    if(int(A) == 0 and int(B) == 0):
        break
    else:
        C_list.insert(i,(int(A)+int(B)))
        i = i + 1
j = 0
while j < len(C_list):
    print(C_list[j])
    j = j + 1
    
