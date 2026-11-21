n, p1, p2, p3, t1, t2 = map(int, input().split())
ans = 0
last = 0

for i in range(n):
    l, r = map(int, input().split())

    ans += (r - l) * p1

    #2开始中间休息
    if i > 0:
        rest = l - last

        for j in range(rest):
            if j < t1:
                ans += p1
            elif j < t1 + t2:
                ans += p2
            else:
                ans += p3

    last = r

print(ans)