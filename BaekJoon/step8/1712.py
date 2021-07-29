import sys

A, B, C = map(int, sys.stdin.readline().split())

BEP = 0
 
if C <= B: BEP = -1
else: BEP = (A/(C-B))+1
       
print(int(BEP))