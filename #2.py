X = int(input())
Y = int(input())
N = int(input())
if (N % (X + Y)) == 0:
   print(int((N / (X + Y))*2))
else:
   if (N % (X + Y)) <= Y:
       print(int(((N//(X + Y))*2)+1))
   else:
       print(int(((N//(X + Y))*2)+2))
