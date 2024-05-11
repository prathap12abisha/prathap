##a=6
##print(type(a))
##a=6.9078
##print(type(a))
##a=6+4j
##print(type(a))
##a="Sheakin"
##print(type(a))
##a=10
##print(bin(a))


##a="Welcome to "
##print(a)
##print(a+" "+"Networkz System")
##print(a*2)
##print(a[7])
##print(a[3:])
##print(a[:3])
##print(a[3:8])


##a="Welcome to"
##print(a.capitalize())
##print(a.upper())
##print(a.lower())
##print(a.title())
##print(len(a))
##print(min(a))
##print(max(a))
##print("a". join(a))


##list=["hi",1,2,"hello","how","are",4,5]
##print(list)
##list1=["apple","mango",8]
##print(list+list1)
##print(list*2)
##print(list[3])
##print(list[3:])
##print(list[2:8])
##list[6]="you"
##print(list)
##del list1[1]
##print(list1)


##list=["hi",1,2,"hello","how","are",4,5]
##list1=[1,2,3,4,5]
##print(len(list))
##print(min(list))
##print(min(list1))
##print(max(list1))


##list1=[1,2,3,4,5,3]
##x=list1.count(3)
##print(x)
##list1.append("hello")
##print(list1)
##list1.extend([8,9,10])
##print(list1)
##print(list1.index(4))
##list1.remove(3)
##print(list1)
##list1.reverse()
##print(list1)


##tuple=("hi",1,2,"hello","how","are",4,5)
##print(tuple)
##tuple1=("apple","mango",8)
##print(tuple+tuple1)
##print(tuple*2)
##print(tuple[3])
##print(tuple[3:])
##print(tuple[2:8])


##tuple2=("hi",1,2,"hello","how","are",4,5)
##tuple1=("a","b","c")
##print(len(tuple2))
##print(max(tuple1))
##print(min(tuple1))


##set={"a","b","c"}
##print(set)


##thisdict=(
##    "brand":"Ford",
##    "model":"Mustang",
##    "year":1964
##)
##print(thisdict["brand"])


##thisdict=(
##    "brand":"Ford",
##    "model":"Mustang",
##    "model":"App",
##    "year":1964
##    "year":2020
##)
##print(thisdict)


##thisdict=(
##    "brand":"Ford",
##    "model":"Mustang",
##    "year":1964
##)
##thisdict["year"]=2018
##print(thisdict)


##thisdict=(
##    "brand":"Ford",
##    "model":"Mustang",
##    "year":1964
##)
##thisdict.update(("year":2020))
##print(thisdict)


##thisdict=(
##    "brand":"Ford"
##    "model":"Mustang"
##    "year":1964
##)
##thisdict["colour"]="red"
##print(thisdict)


##a=(input("Enter the first number :"))
##b=(input("Enter the second number :"))
##c=(input("Enter the third number :"))
##if (a>b)&(a>c):
##    print("a is greater")
##if (b>c)&(b>a):
##    print("b is greater")
##if(c>a)&(c>b):
##    print("c is greater")


##a=int(input("Enter the number:"))
##if a%2==0:
##    print("Enter the number is even")
##else:
##    print("Enter the number is odd")


##browser=input("Enter the browser:")
##if (browser=="chrome"):
##    print("Browser name is chrome")
##elif (browser=="safari"):
##    print("Browser name is safari")
##elif (browser=="edge"):
##    print("Browser name is edge")
##else:
##    print("Enter the browser, name is not here")


##a=int(input("Enter the number"))
##if(a>=0):
##    if(a==0):
##        print("Zero")
##    else:
##        print("positive number")
##else:
##    print("negative number")


##a=int(input("Enter the number"))
##i=0
##while(i<a):
##    print("The count is:",i)
##    i+=1
##print("end of program")


##numbers=[6,5,4,1,2,3,7,8,9]
##sum=0
##for val in numbers:
##    sum=sum+val
##print("the sum is",sum)


##sum=0
##for i in range(10):
##    sum=sum+i
##print(sum)


##for i in range (1,11):
##    mul=i*5
##    print(i,"*5=" mul)


##a="students"
##for i in a:
##    if i=="e":
##        continue
##    print(i)


##a="students"
##for i in a:
##    if i=="e":
##        break
##    print(i)


##print("how are you")
##val={'s','h','a','l','i','n','i'}
##for i in val:
##    pass


##print("how are you")
##val={'s','h','a','l','i','n','i'}
##for i in val:
##    print(i)
##print("terminated")


##i=1
##whilei<=10:
##    if(i==5):
##        pass
##    print(i)
##    i=i+1
##print("program terminated")


##n=int(input("enter the number:"))
##for i in range(1,n):
##    for j in range(1,i+1):
##        print("*",end=' ')
##    print()


##def averageNumber (a,b):
##    print ("Average of a and b is:",(a+b)/2)
##averageNumber(4,5)


##def addition(a,b):
##    return(a,b)
##print("Addition of a and b value is:",addition(3,4))

      
##def returnstmt(a):
##    return(4*a)
##print(returnstmt(2),",",returnstmt(5))


##n=int(input("Enter the number 1 to 4:"))
##def conversion(a):
##    if(a==1):
##        return"one"
##    if(a==2):
##        return"two"
##    if(a==3):
##        return"three"
##    if(a==4):
##        return"four"
##print(n,"In words",conversion(n))


##def vote(symbol="mango"):
##    print("winner"+" "+symbol)
##vote("lotus")
##vote("hand")
##vote()


##def sum(x,y=10):
##    return x+y
##print(sum(10))
##print(sum(5,8))


##a="welcome"
##def globalv():
##    print("Global variable value is:"a)
##globalv()
##print("Global variable value is:"a)


##def greeting():
##    message="Happy BirthDay"
##    print("Hi shalu,",message)
##greeting
##print("Hi shalu,",message)


##oldlist=[1,23,4,5,6]
##newlist=filter(lambda x:(x%2==0),oldlist)
##print(list(newlist))


##def even(x):
##    return(x%2==0)
##y=filter (even,range(1,11))
##print(list(y))


##oldlist=[1,2,3,4,5,6]
##newlist=filter(lambda x:(x*2),oldlist)
##print(list(newlist))


##def even(x):
##    return x*2
##y=map(even,range(1,11))
##print(list(y))


##list=[2,4,7,3]
##print(reduce(lambda x))


##def add (x,y):
##    return x+y
##r=reduce(add.range(1,11))
##print (r)


##print(sqrt(10))
##print(factorial(5))


##print(sqrt(10))
##print(factorial(5))
##print(pow(2,3))


##import calendar
##print("June Month 2024")
##print(calendar.Month(2024,6,6,4))


##def addseq(x):
##    if x==1:
##        return 1
##    else:
##        return x+addseq(x-1)
##print("The sum of first 10 sequence number is",addseq(10))

##class myclass:
##    x=5
##print(myclass)

##class Rectangle:
##    len=4
##    brd=5
##    def rectArea(self):
##        return Rectangle.len*Rectangle.brd
##obj=Rectangle()
##print("Area of Rectangle is:",obj.rectArea())

##class Rectangle:
##    def__init__(self):
##        self.len=4
##        self.brd=5
##    def rectArea(self):
##        return self.len*self.brd
##obj=Rectangle()
##print("Area of Rectangle is:",obj.rectArea())

##class Rectangle:
##    def __init__(self,length,breadth):
##        self.len=length
##        self.brd=breadth
##    def rectArea(self):
##        return self.len*self.brd
##obj=Rectangle(5,6)
##print("Area of Rectangle is:",obj.rectArea())

##class Rectangle:
##    def__init__(self,length,breadth):
##        self.len=length
##        self.brd=breadth
##    def__str__(self):
##        return"length is %d,breadth is %d"%(self.len,self.brd)
##    def rectArea(self):
##        return self.len*self.brd
##obj=Rectangle(5,6)
##print(obj)
##print("Area of Rectangle is:",obj.rectArea())


##class rect:
##    n=0
##    def __init__(self,x,y):
##        rect.n+=1
##        self.l=x
##        self.b=y
##    def __del__(self):
##        rect.n-=1
##        classname=self.__class__.__name__
##        print(classname,'destroyed')
##    def rectarea(self):
##        print("Area of rectangle is ",self.l*self.b)
##    def noOFobjects(self):
##        print("Number of objects are: ",rect.n)
##r=rect(3,5)
##r.rectarea()
##s=rect(5,8)
##s.rectarea()
##r.noOFobjects()
##del r
##s.noOFobjects()
##del s
##print("no of objects now:",rect.n)


##class Employee:
##    def __init__(self,name,age):
##        self.name=name
##        self.age=age
##    def empData (self):
##        print("Name is:",self.name)
##        print("Age is:",self.age)
##class Developer(Employee):
##    def __init__(self,name,age,exp):
##        Employee.__init__(self,name,age)
##        self.exp=exp
##    def devData(self):
##        Employee.empdata(self)
##        print("expriance is :",self.exp)
##print (".............employee shalini details........")
##obj1=Employee("shalini",31)
##obj1.empData()
##print (".............Developer abilash details........")
##obj=Developer("abilash",17,10)
##obj.devData()


##class TeamMember:
##    def __init__(self,name,id):
##        self.name=name
##        self.id=id
##class Worker:
##    def __init__(self,salary,position):
##        self.salary=salary
##        self.position=position
##class  TeamLeader(TeamMember,Worker):
##      def __init__(self,name,id,salary,position,experience):
##          self.experience=experience
##          TeamMember. __init__(self,name,id)
##          Worker. __init__(self,salary,position)
##          print("name is:",self.name,"\n","id is",self.id,"\n","salary is:",self.salary,"\n","position is",self.position,"\n","Experience is",self.experience)
##obj=TeamLeader("shalini","101","3000","developer","5")


##class rectangle:
##    def __init__(self,length,height):
##        self.length=length
##        self.height=height
##    def area(self):
##        return self.length*self.height
##class triangle:
##    def __init__(self,length,height):
##        rectangle.__init__(self,length,height)
##    def area(self):
##        return 1/2*self.length*self.height
##obj=triangle(4,5)
##obj1=rectangle(2,5)
##print("Area of rectangle is: ",obj1.area())
##print("Area of triangle is: ",obj.area())


##class rect:
##    def __init__(self,l,b):
##        self.l=l
##        self.b=b
##    def __str__(self):
##        return"Length is %d,Breadth is %d"%(self.l,self.b)
##    def __add__(self,c):
##        return rect (self.l+c.l,self.b+c.b)
##    def rectarea(self):
##        return self.l*self.b
##r1=rect(5,8)
##r2=rect(10,20)
##r3=r1+r2
##print(r3)
##print("Area of rectangle is ",r3.rectarea())


##class rect:
##    def __init__(self,x,y):
##        self.l=x
##        self.b=y
##    def rectarea(self):
##        return self.l*self.b
##r=rect(5,8)
##print("area of rectangle is ",r.rectarea())
##print("area of rectangle is ",r.l*r.b)


##class rect:
##    def __init__(self,x,y):
##        self.__l=x
##        self.__b=y
##    def rectarea(self):
##        return self.__l*self.__b
##r=rect(5,8)
##print("area of rectangle is ",r.rectarea())
##print("area of rectangle is ",r._rect__l*r._rect__b)


##import linecache
##line=linecache.getline("aboutpython.txt",1)
##print ("The content of the third line is:","line")


##str="Hello world"
##f=open ("filebinary.bin","w")
##line=f.write(str)
##f.close()
##f=open ("filebinary.bin","r")
##fcontent=f.read()
##print(fcontent)
##f.close()


##n=int(input("Enter the number:"))
##b=int(input("Enter the number:"))
##c=n/b
##print(c)


##n=int(input("Enter the number:"))
##b=int(input("Enter the number:"))
##try:
##    c=n/b
##    print(c)
##except Exception as e:
##    print(e)


##try:
##    a=int(input("Enter the number:"))
##    if a<4:
##        b=a/(a-3)
##        print("value of b=",b)
##except Exception as ex:
##    print("error occurred",ex)
##else:
##    print("End of the program")


##try:
##    n=int(input("enter a number"))
##    assert n%2==0
##except:
##    print("Not an even number")
##else:
##    reciprocal=1/n
##    print("Reciprocal of number is ",reciprocal)


##import sys
##n=input("enter a number:")
##if n.isdigit():
##    n=int(n)
##try:
##    m=15/n
##    print("The result is:",m)
##except Exception as ex:
##    print("You have not entered a numeric value:",ex)
##    sys.exit(1)


##import sys
##try:
##    f=open ("abc.txt","r")
##    try:
##        lines=f.read()
##        print(lines)
##    except IOError:
##        print("Input Output Error")
##except Exception as ex:
##    print("file abc.txt does not exist",ex)
##    sys.exit(1)
##finally:
##    print("file abc.txt exist as notexist")


##try:
##    age=int(input("please enter your age"))
##    if age<5:
##        raise ValueError("NOT ALLOWED! YOUR AGE IS LESS THAN5")
##    if age >20:
##        raise ValueError("NOT ALLOWED! YOUR AGE IS GREATER THAN 20")
##except ValueError as V:
##    print("VALUEERROR EXCEPTIONN THROWN",V)


##n=int(input("ENTER A POSITIVE VALUE:"))
##assert(n>=0),'ENTERED VALUE IS NOT A POSITIVE VALUE'


##from tkinter import *
##from tkinter import messagebox
##window=Tk()
##window.title("HAI")
##window.geometry("500x500")
##window.resizable(0,0)
##window.config(bg="blue")
##def click():
##    messagebox.showinfo("MESSAGE","HI AM MESSAGEBOX")
##btn=Button(window,text="CLICK ME !",bg="WHITE",font=("TIMES",25),command=click)
##btn.place(x=100,y=150)
##window.mainloop()


##from tkinter import*
##from PIL import Image,ImageTK
##w=Tk()
##w.title("ADDING IMAGE")
##w.geometry("500x500")
##w.resizable(height=0,width=0)
##img=Image.open("img 1.jpg")
##resiz=img.resize((500,500))
##render=imageTk.photoImage(resiz)
##lb=Label1(w,image=render)
##lb.place(x=10,y=10)
##lab=label(w,text="username").pack()
##w.mainloop()


##from tkinter import*
##window=Tk()
##scrollbar=Scrollbar(window)
##scrollbar.pack(side=RIGHT,fill=Y)
##mylist=Listbox(window,yscrollcommand=scrollbar.set)
##for line in range(100):
##    mylist.insert(END,"this is the line number"+str(line))
##mylist.pack(side=LEFT,fill=BOTH)
##scrollbar.config(command=mylist.yview)
##mainloop()


##from tkinter import*
##w=Tk()
##c=Canvas(w,bg="Blue",height=350,width=600)
##coord=(80,60,240,240)
##arc=c.create_arc(coord,start=0,extent=350,fill="red")
##c.pack()
##w.mainloop()


##from tkinter import*
##top=Tk()
##top.geometry("200x200")
##spin=Spinbox(top,from_=0,to=25)
##spin.pack()
##top.mainloop()


##import  sqlite3
##conn=sqlite3.connect('sheakin.db');
##print("OPENED DATABASE SUCCESSFULLY");


##conn.execute('''CREATE TABLE if not exists USER
##                    (ROLLNO INT NOT NULL,
##                      NAME TEXT NOT NULL,
##                      AGE INT NOT NULL,
##                      ADDRESS INT NOT NULL,
##                      SALARY REAL);''')
##print ("TABLE CREATED SUCCESSFULLY")


##conn.execute('''INSERT INTO USER(ROLLNO,NAME,AGE,ADDRESS,SALARY)
##             VALUES (1,'sheakin',17,'kk',30000.00)''')
##conn.commit()
##print("RECORDS CREATED SUCCESSFULLY");
##conn.close()


##conn.execute('''UPDATE user SET Name='matheesh'where ROLLNO=1''');
##conn.commit()
##print("UPDATED SUCCESSFULLY")


##conn.execute ('''DELETE from user where Name='matheesh' ''');
##conn.commit()
##print("DATA DELETED SUCCESSFULLY")
