import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort()
    scores.reverse()
    result = sum(scores[:k])
    print(f'#{tc} {result}')