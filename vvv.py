
x=input()
l=len(x)
sum=0
for j in range(0,l):
     sum+=int(x[j])**l
if int(x)==sum:
    print('armstrong number')
else:
    print('not')
