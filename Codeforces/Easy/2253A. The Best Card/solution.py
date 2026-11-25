t = int(input())
 
for _ in range(t):
    n = int(input())
    big = n + 1
    ok = True
 
    for i in range(2, big):
        if big % i == 0:
            ok = False
            break
 
    if ok:
        print("YES")
    else:
        print("NO")