#solve for x, 2x+5=11
import random
def substraction():
    #x - 3 = 5,solve for x
    def hard():
        r1=random.randint(2,12)
        if r1%2!= 0:
            r1=r1+1
        r2=random.randint(4,21)
        if r2%2!= 0:
            r2=r2+1
        r3=random.randint(21,35)
        if r3%2!= 0:
            r3=r3+1
        y=(r3+r2)
        x= y/r1

        print("Ques: Solve for x, ",r1,"x - ",r2," = ",r3)

        o1=(r3-r2)/r1
        o2=r2+r3-r1
        o3=x
        o4=(r3+r2)*r1

        print(" option 1 : ",float(o1),"\n","option 2 : ",float(o2),"\n","option 3 : ",float(o3),"\n","option 4 : ",float(o4),"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r1,"x - ",r2," = ",r3)
            print(r1,"x = ",r3," + ",r2)
            print(r1,"x = ",y)
            print("x = ",y,"/",r1)
            print("x = ",x)
            
        if value==1:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==2:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==3:
             print("\nright option")
             print(">--------------------------<")
             sol()
        elif value==4:
             print("\nwrong option")
             print(">--------------------------<")
             sol()
        else :
            print("\nInvalid Choice")

    def easy():
        r1=random.randint(2,12)
        if r1%2!= 0:
            r1=r1+1
        r2=random.randint(4,21)
        if r2%2!= 0:
            r2=r2+1
        r3=random.randint(21,35)
        if r3%2!= 0:
            r3=r3+1
        r1=2
        y=(r3+r2)
        x= y/r1

        print("Ques: Solve for x, ",r1,"x - ",r2," = ",r3)

        o1=(r3-r2)/r1
        o2=r2+r3-r1
        o3=x
        o4=(r3+r2)*r1

        print(" option 1 : ",o1,"\n","option 2 : ",o2,"\n","option 3 : ",o3,"\n","option 4 : ",o4,"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r1,"x + ",r2," = ",r3)
            print(r1,"x = ",r3," - ",r2)
            print(r1,"x = ",y)
            print("x = ",y,"/",r1)
            print("x = ",x)
            
        if value==1:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==2:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==3:
             print("\nright option")
             print(">--------------------------<")
             sol()
        elif value==4:
             print("\nwrong option")
             print(">--------------------------<")
             sol()
        else :
            print("\nInvalid Choice")

    print("1.easy")
    print("2.hard")
    ch=int(input("choose level:"))
    if ch==1:
        easy()
    elif ch==2:
        hard()
    else:
        print("invalid choice")
def addition():
    #solve for x, 2x+5=11
    def hard():
        r1=random.randint(2,12)
        if r1%2!= 0:
            r1=r1+1
        r2=random.randint(4,21)
        if r2%2!= 0:
            r2=r2+1
        r3=random.randint(21,35)
        if r3%2!= 0:
            r3=r3+1
        y=(r3-r2)
        x= y/r1

        print("Ques: Solve for x, ",r1,"x + ",r2," = ",r3)

        o1=(r3+r2)/r1
        o2=r1+r2+r3
        o3=x
        o4=(r3+r2)*r1

        print(" option 1 : ",float(o1),"\n","option 2 : ",float(o2),"\n","option 3 : ",float(o3),"\n","option 4 : ",float(o4),"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r1,"x + ",r2," = ",r3)
            print(r1,"x = ",r3," - ",r2)
            print(r1,"x = ",y)
            print("x = ",y,"/",r1)
            print("x = ",x)
            
        if value==1:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==2:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==3:
             print("\nright option")
             print(">--------------------------<")
             sol()
        elif value==4:
             print("\nwrong option")
             print(">--------------------------<")
             sol()
        else :
            print("\nInvalid Choice")

    def easy():
        r1=random.randint(2,12)
        if r1%2!= 0:
            r1=r1+1
        r2=random.randint(4,21)
        if r2%2!= 0:
            r2=r2+1
        r3=random.randint(21,35)
        if r3%2!= 0:
            r3=r3+1
        r1=2
        y=(r3-r2)
        x= y/r1

        print("Ques: Solve for x, ",r1,"x + ",r2," = ",r3)

        o1=(r3+r2)/r1
        o2=r1+r2+r3
        o3=x
        o4=(r3-r2)*r1

        print(" option 1 : ",o1,"\n","option 2 : ",o2,"\n","option 3 : ",o3,"\n","option 4 : ",o4,"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r1,"x + ",r2," = ",r3)
            print(r1,"x = ",r3," - ",r2)
            print(r1,"x = ",y)
            print("x = ",y,"/",r1)
            print("x = ",x)
            
        if value==1:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==2:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==3:
             print("\nright option")
             print(">--------------------------<")
             sol()
        elif value==4:
             print("\nwrong option")
             print(">--------------------------<")
             sol()
        else :
            print("\nInvalid Choice")

    print("1.easy")
    print("2.hard")
    ch=int(input("choose level:"))
    if ch==1:
        easy()
    elif ch==2:
        hard()
    else:
        print("invalid choice")
def multiplication():
    #solve for x, 10 = 2x
    def easy():
        r1=random.randint(2,21)
        r2=random.randint(1,10)
        r3=r1*r2
        x=r3/r1
        print("Ques: Solve for x, ",r1,"x = ",r3)

        o1=r3*r1
        o2=r3-r1
        o3=x
        o4=r3+r1

        print(" option 1 : ",float(o1),"\n","option 2 : ",float(o2),"\n","option 3 : ",float(o3),"\n","option 4 : ",float(o4),"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r1,"x = ",r3)
            print("x = ",r3,"/",r1)
            print("x = ",x)
            
        if value==1:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==2:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==3:
             print("\nright option")
             print(">--------------------------<")
             sol()
        elif value==4:
             print("\nwrong option")
             print(">--------------------------<")
             sol()
        else :
            print("\nInvalid Choice")

    def hard():
        r1=random.randint(2,12)
        if r1%2!= 0:
            r1=r1+1
        r3=random.randint(21,41)
        if r3%2!= 0:
            r3=r3+1
        x=r3/r1

        print("Ques: Solve for x, ",r1,"x = ",r3)


        o1=r3*r1
        o2=r3-r1
        o3=x
        o4=r1/r3

        print(" option 1 : ",o1,"\n","option 2 : ",o2,"\n","option 3 : ",o3,"\n","option 4 : ",o4,"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r1,"x = ",r3)
            print("x = ",r3,"/",r1)
            print("x = ",x)
            
        if value==1:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==2:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==3:
             print("\nright option")
             print(">--------------------------<")
             sol()
        elif value==4:
             print("\nwrong option")
             print(">--------------------------<")
             sol()
        else :
            print("\nInvalid Choice")

    print("1.easy")
    print("2.hard")
    ch=int(input("choose level:"))
    if ch==1:
        easy()
    elif ch==2:
        hard()
    else:
        print("invalid choice")
def division():
    #solve for x, 15/x = 3
    def easy():
        r1=random.randint(2,21)
        r2=random.randint(1,10)
        r3=r1*r2
        x=r3/r1
        print("Ques: Solve for x, ",r3,"/x = ",r1)

        o1=r3*r1
        o2=r3-r1
        o3=x
        o4=r1/r3

        print(" option 1 : ",float(o1),"\n","option 2 : ",float(o2),"\n","option 3 : ",float(o3),"\n","option 4 : ",float(o4),"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r3,"/x = ",r1)
            print("x = ",r3,"/",r1)
            print("x = ",x)
            
        if value==1:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==2:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==3:
             print("\nright option")
             print(">--------------------------<")
             sol()
        elif value==4:
             print("\nwrong option")
             print(">--------------------------<")
             sol()
        else :
            print("\nInvalid Choice")

    def hard():
        r1=random.randint(2,12)
        if r1%2!= 0:
            r1=r1+1
        r3=random.randint(21,41)
        if r3%2!= 0:
            r3=r3+1
        x=r3/r1

        print("Ques: Solve for x, ",r1,"x = ",r3)


        o1=r3*r1
        o2=r3-r1
        o3=x
        o4=r1/r3

        print(" option 1 : ",o1,"\n","option 2 : ",o2,"\n","option 3 : ",o3,"\n","option 4 : ",o4,"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r3,"/x = ",r1)
            print("x = ",r3,"/",r1)
            print("x = ",x)
            
        if value==1:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==2:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==3:
             print("\nright option")
             print(">--------------------------<")
             sol()
        elif value==4:
             print("\nwrong option")
             print(">--------------------------<")
             sol()
        else :
            print("\nInvalid Choice")

    print("1.easy")
    print("2.hard")
    ch=int(input("choose level:"))
    if ch==1:
        easy()
    elif ch==2:
        hard()
    else:
        print("invalid choice")
#----main-----
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
ch=int(input("choose the relation between constant and the variable term:"))
if ch==1:
    addition()
elif ch==2:
    substraction()
elif ch==3:
    multiplication()
elif ch==4:
    division()
else:
    print("invalid choice")
