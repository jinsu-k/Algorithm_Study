'''
문제:
    - 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
입력:
    - 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
    - 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
출력:
    - 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
제한:
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
'''

import sys

C = int(sys.stdin.readline())
s_Avg = [0]*C

for i in range(0, C):
    avg = 0
    count = 0
    over_avg = []
    N = sys.stdin.readline().strip().split()
    N = list(map(int, N))

    avg = ((sum(N)-N[0])/N[0])

    over_avg = list(filter(lambda x: x > avg, N))
    count = len(over_avg)
    s_Avg[i] = ((count/N[0])*100) 

for score in s_Avg:
    print('%.3f%' % round(score,3))


    # import sys

# C = int(sys.stdin.readline())
# avg_Score = [0]*C
# temp_List = []

# for i in range(0,C):
#     avg = 0
#     N = sys.stdin.readline().strip().split()
#     N = list(map(int, N))
    
#     avg = ((sum(N)-N[0])/N[0])
#     temp_List = [i for i in N if ((i!=N[0]) and (i>avg))]
#     avg_Score[i] = (((len(temp_List)/N[0])*100)+1e-15)

# for score in avg_Score:
#     print('%.3f%' %round(score,3))