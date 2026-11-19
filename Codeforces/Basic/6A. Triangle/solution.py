a = list(map(int, input().split()))
a.sort()

triangle = False
segment = False

for i in range(4):
    for j in range(i + 1, 4):
        for k in range(j + 1, 4):
            if a[i] + a[j] > a[k]:
                triangle = True
            elif a[i] + a[j] == a[k]:
                segment = True

if triangle:
    print("TRIANGLE")
elif segment:
    print("SEGMENT")
else:
    print("IMPOSSIBLE")