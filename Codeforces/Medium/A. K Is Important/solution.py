t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    left = k - 1
    right = n - k
    score = 0

    if left <= right:
        for i in range(left, right + 1):
            score += a[i]


        i = left - 1
        j = right + 1
    else:

        i = right
        j = left

    while i >= 0:
        score += max(a[i], a[j])
        i -= 1
        j += 1

    print(score)