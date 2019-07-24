f1=open('./Yeni Metin Belgesi (2).txt','r')
for i in range(2500):
    if i%50==0:
        print("],\n[",end='')
    
    if int(f1.read(1))==1:
        if i%50==0:
          print("0",end='')
        else:
            print(",0",end='')
    else:
        if i%50==0:
            print("255",end='')
        else:
            print(",255",end='')
