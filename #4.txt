n = int(input())
l = int(input())
a = [1] + [0]*(n-1)
for i in range(n):
    x = int(input())
    if a[i] ==1:
        for j in range(i, i+x // l + 1):
            a[j] =1
for i in range(n-1, -1, -1):
    if a[i] ==1:
        print(i+1)
        break

