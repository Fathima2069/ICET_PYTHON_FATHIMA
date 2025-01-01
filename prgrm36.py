f1=open('file.txt','r')
f2=open('new.txt','w')
cont=f1.readlines()
for i in range(0,len(cont)):
     if(i%2==0):
  f2.write(cont[i])
     else:
        passf2.
      close()

File - file.txt
india is my country
hello how are you
have a nice day
good morning

