f1=open("e//zz.txt","r")
f2=open("e//aa.txt","w")
q=f1.readlines()
a=0
for i in range(0,20):
    s=input("the answer is")
    q=f1.readlines()
    if s==q:
        a+=1
name=input('enter your name')
print(name,'answer  on',a,'from 20')
f2.write(name+'/t'+str(a))
f1.close()
f2.close()
