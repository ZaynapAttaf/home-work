a=int(input('enter a decimal number'))
b=[]
while a!=0:
    c=a%2
    b.aappend(c)
    a=a//2
b.reverse()
for i in range(0,len(b)):
    b[i]=int(b[i])
    print(b[i],end="")
