n=int(input())
k = int(input())
if k == n:
    print(0)
else:
    print(2*n*(n//k-1))
