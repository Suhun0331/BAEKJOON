import sys
input= sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

dp = [[0]*n for _ in range(n)]

for i in range(n):
    for start in range(n-i):
        end = start + i
        if start == end:
            dp[start][end] = 1
        elif start == end-1:
            if arr[start] == arr[end]:
                dp[start][end] = 1

        else:
            if arr[start] == arr[end] and dp[start+1][end-1] == 1:
                dp[start][end] = 1

for _ in range(m):
    a, b = map(int, input().split())
    print(dp[a-1][b-1])
