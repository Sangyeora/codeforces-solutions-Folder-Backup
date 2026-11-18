n, d = map(int, input().split())
a = list(map(int, input().split()))

ans = 0

for i in range(1, n):
    if a[i] <= a[i - 1]:
        times = (a[i - 1] - a[i]) // d + 1
        a[i] = a[i] + times * d
        ans = ans + times

print(ans)