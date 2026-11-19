y, w = map(int, input().split())
 
big = max(y, w)
 
if big == 1:
    print("1/1")
elif big == 2:
    print("5/6")
elif big == 3:
    print("2/3")
elif big == 4:
    print("1/2")
elif big == 5:
    print("1/3")
else:
    print("1/6")