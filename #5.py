x = int(input())
y = int(input())
if x == y:
    print(-1)
elif y >= (x*2-1):
    print(x)
else:
    print(x *(2 + (x*2-y)//(y-x+1) - int((x*2-y) == (y-x+1))))
