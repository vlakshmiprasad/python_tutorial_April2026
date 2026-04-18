#x=int(input("enter any number"))
#y=int(input("enter the number"))
#i=1
#while(i<6):
#    print(i)
#   i=i+1  
#for i in range(1,6):
#  print(i)
#i=int(input("enter the number"))
#if(i%2==0):
#    print("even")  
#else:
#    print("odd") 
#n=int(input("enter any number")) 
#while(n>0):
#    r=n%10
#    rev=(n*0)+r
#    print(rev,end="")
#    n=n//10
#def sub(a,b):
#    print(a+b)
#sub(10,20)
#def sub(name,msg):
#    print("hello",name,msg)
#sub("prasad","good morning")  
#def wish(name="guest"):
# print("hello",name,"goodmorning")
#wish("durga")
#a=10
#def f1():
#    print(a) 
#def f2():
#    print(a)  
#f1()
#f2()
#def f1():
#    a=10
#    print(a)
#def f2():
#    print(a)
#f1()
#f2() 
#s=lambda a,b:a+b  
#print(s(10,20))
#import math as m
#def distance2points(x1,y1,x2,y2):
#    distance=m.sqrt(((x2-x1)**2)+((y2-y1)**2))
#    print(distance)   
#distance2points(10,20,30,40)
#def fact(n):
#    if n==0:
#        return 1
#    else:
#        return(n*fact(n-1))
#    return result
#print(fact(4))
#s="apple"
#b=s.upper()
#print(b)
#str="hello hello hello"
#print(str.replace("he","fe"))
#str="python"
#print(max(str))
#str="1234"
#print(str.zfill(10))
#s=open("nagraj.py",mode='r')
#print(s.read())
#s.close()
#s1=open("nagraj.py",mode='r')
#print(s1.read())
#s1.close()
#s1=open("nagraj1.py","r")
#print(s1.read())
#s1.close()
#files
#a="true"
#b="false"
#print(a and b)
#print(a or b)
#print(not a)
#class text:
#    def __init__(self):
#        print("constructer execution")
#    def m(self):
#        print("method execution")
#t1=text()
#t2=text()
#t3=text()
#t1.m()
#def __init__(self):
#    self.name="darga"
#    self.age=40
#    self.marks=80
#def talk(self):
#    print("hello i am:"self.name)
#    print("hello my age is:"self.age) 
#    print("hello my marks is:"self.marks)
#class p:
#    def m(self):
#        print("parent method")
class p1(p):
    def m1(self):
        print("child method")        
c=p1()
c.m()