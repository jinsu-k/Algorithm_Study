#두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
#두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
#첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

#python 소숫점 버릴때 사용하는 floor 함수 올림은 ceil
from math import floor
A,B = input().split()
def add(A,B):
    return int(A)+int(B)
def sub(A,B):
    return int(A)-int(B)
def mul(A,B):
    return int(A)*int(B)
def div(A,B):
    return floor(int(A)/int(B))
def re(A,B):
    return int(A)%int(B)
print(add(A,B))
print(sub(A,B))
print(mul(A,B))
print(div(A,B))
print(re(A,B))