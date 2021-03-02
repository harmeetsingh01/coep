#If Rashmi wieghs 24 kg and Rashi is 21 Kg,
#Radhika is 18 Kg and Ramola 15 kg., which two pairs will form an equation?
#a)...., b)...., c)...., d).... ( an such many examples)

from IndianNameGenerator import *
import random

n1=randomMarathi()
n2=randomMarathi()
n3=randomMarathi()
n4=randomMarathi()
n5=randomMarathi()

if n1==n2 or n1==n3 or n1==n4 or n1==n5 or n2==n3 or n3==n4 or n4==n5 or n1==n2==n3==n4==n5:
    n1=randomMarathi()
    n2=randomMarathi()
    n3=randomMarathi()
    n4=randomMarathi()
    n5=randomMarathi()

r1=random.randint(40, 49)
r2 = random.randint(25, 50)
r3 = random.randint(25, 50)
#weights should not be same
if r1==r2 or r1==r3 or r2==r3 or r1==r2==r3:
    r1=r1+5
    r2=r2+8
    r3=r3+1

r4=r3+r2-r1


r=random.randint(0,15)
if r>3 and r<7:
    r4,r3=r3,r4
    
elif r>7 and r<11:
    r4,r2=r2,r4

elif r>11 and r<15:
    r4,r1=r1,r4


if r1<25 or r2<25 or r3<25 or r4<25:
    r1=r1+20
    r2=r2+20
    r3=r3+20
    r4=r4+20



#Question
print("If",n1,"weighs",r1,"Kg and",n2,"weighs",r2,"Kg,",n3,"weighs",r3,"Kg and",n4,"weighs",r4,"Kg.\nWhich two pairs will form an equation?\n")

op=["","","",""]
sq=[0,1,2,3]
#options



if abs(r1-r2)==abs(r3-r4):
    o3=n1+''' and '''+n2+''' , '''+n3+''' and '''+n4
    o1=n1+''' and '''+n3+''' , '''+n2+''' and '''+n4
    o2=n1+''' and '''+n4+''' , '''+n2+''' and '''+n3
    o4=n1+''' and '''+n4+''' , '''+n2+''' and '''+n5
    
    

elif abs(r1-r3)==abs(r2-r4):
    o3=n1+''' and '''+n3+''' , '''+n2+''' and '''+n4
    o1=n1+''' and '''+n2+''' , '''+n3+''' and '''+n4
    o2=n1+''' and '''+n4+''' , '''+n2+''' and '''+n3
    o4=n1+''' and '''+n5+''' , '''+n2+''' and '''+n3
    
    
elif abs(r1-r4)==abs(r2-r3):
    o3=n1+''' and '''+n4+''' , '''+n2+''' and '''+n3
    o1=n1+''' and '''+n3+''' , '''+n2+''' and '''+n4
    o2=n1+''' and '''+n2+''' , '''+n3+''' and '''+n4
    o4=n1+''' and '''+n4+''' , '''+n5+''' and '''+n3
    
    
ra=random.randint(0,3)
op[ra]=o3
sq.remove(ra)
op[sq[0]]=o1
op[sq[1]]=o2
op[sq[2]]=o4
#PRINTING OPTIONS
for z in range(1,5):
        print("Option",z,":",op[z-1])
    
print("")
value = int(input("Enter the option number : "))

def sol():
    global r1
    global r2
    global r3
    global r4
    print("Since, it is given that the weights of",n1,",",n2,",",n3,"and",n4,"\nare",r1,",",r2,",",r3,"and",r4,"respectively")
    if abs(r1-r2)==abs(r3-r4):
        if r2>r1:
            r2,r1=r1,r2
        if r4>r3:
            r4,r3=r3,r4
            
        a=r1-r2
        b=r3-r4
        print("Now,",r1,"-",r2,"=",a)
        print("Also,",r3,"-",r4,"=",b)
        print("=>",r1,"-",r2,"=",r3,"-",r4)
        print("=> L.H.S = R.H.S")
        print("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")
        print("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n2+" , "+n3+" and "+n4)

    elif abs(r1-r3)==abs(r2-r4):
        if r3>r1:
            r3,r1=r1,r3
        if r4>r2:
            r4,r2=r2,r4
            
        a=r1-r3
        b=r2-r4
        print("Now,",r1,"-",r3,"=",a)
        print("Also,",r2,"-",r4,"=",b)
        print("=>",r1,"-",r3,"=",r2,"-",r4)
        print("=> L.H.S = R.H.S")
        print("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")
        print("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n3+" , "+n2+" and "+n4)
                    
    elif abs(r1-r4)==abs(r2-r3):
        if r4>r1:
            r2,r1=r1,r2
        if r4>r3:
            r4,r3=r3,r4
                    
        a=r1-r4
        b=r2-r3
        print("Now,",r1,"-",r4,"=",a)
        print("Also,",r2,"-",r3,"=",b)
        print("=>",r1,"-",r4,"=",r2,"-",r3)
        print("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")
        print("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n4+" , "+n2+" and "+n3)
        



if value==ra+1:
        print("\nYour answer is Correct!")
        print(">------------- SOLUTION -------------<")
        sol()
elif value!=ra+1 and value<5 and value>0:
        print("\nYour answer is incorrect!")
        print(">------------- SOLUTION --------------<")
        sol()
else :
        print("invalid choice")
