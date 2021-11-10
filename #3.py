s=int(input())
e=int(input())
n=int(input())
port=[]
for i in range(0,n):
    x=int(input())
    port.append(x)
a=1000000000
for i in range(0,n):
    if (abs(port[i] - s)) < a:
        a = abs(port[i] - s)
b=1000000000
for i in range(0,n):
    if (abs(port[i] - e)) < b:
        b = abs(port[i] - e)
if abs(s - e) < (a+b+1):
    print(abs(s - e))
else:
    print(a+b+1)
