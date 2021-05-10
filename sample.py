
var=input("Get the input from the user")
print ("user entered ",var)
print var[0]

def my_function():
  for char in 'Python':
    if(char=='h'):
        pass
        print("Current character: ", char)

def addition():
   a=10
   b=20.52
   sum=a+b
   if(sum>0):
       return sum

print ("Sum is " , addition())
   
def difference(a=10,b=5):
   diff=b-a
   if(diff<0):
       return diff
   else:
       return 0

print ("Difference is " , difference(30,40))
print ("Difference is " , difference())

   
def lang(lng):
 print (lng)
   
print (lang(lng=10)) 


def divider(*num):
 dd=10
 for n in num:
     dd=dd+n//10
     return dd

print("Div " , divider(10))
print("Divider " ,divider(30,40))

def employee(**data):
 for key,value in data.items():
   print (" The value {} is {} ".format(key,value))

employee(Name = "Sachin ", Age = 25,City="Delhi")   
	  
	  
	  ///*
	  
	  Ganesh  

Automation 

Task Level Assignment 

do we have this data at one place just related to taregt architecture diagrma


CCGW - deployment design - ready for review 

Smoke test plan - ajay 

Test plan is ready for BGELK

Deployment deign document



f it is just smoke tests, number is between 10-15, infra is ready, functional knowledge is there, 2 days should be good for a Medium complexity app



*///

