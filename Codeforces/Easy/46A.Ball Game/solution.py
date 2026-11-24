n = int(input())

now = 1
ans = []

for i in range(1, n):
    now = now + i

    if now > n:
        now = now - n

    ans.append(now)

print(*ans)