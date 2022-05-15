l=['network','math','programming','physics','music']
x=[]
for i in l:
    if i[0]=='p':
        x.append(i)
y=len(x)
print("the words start with 'p' are: "+star(x))
