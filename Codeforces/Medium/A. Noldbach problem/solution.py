n, k = map(int, input().split())

primes = []

for x in range(2, n + 1):
    ok = True

    for i in range(2, x):
        if x % i == 0:
            ok = False
            break

    if ok:
        primes.append(x)

count = 0

for i in range(len(primes) - 1):
    x = primes[i] + primes[i + 1] + 1

    if x in primes:
        count += 1

if count >= k:
    print("YES")
else:
    print("NO")