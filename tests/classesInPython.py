class student:
    # will be called anytime class is initialised 
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print (" I am constructor ")
               

    def func(self):    
        print (" I am class function")

    def paramFunc(self,name,age):
        print(" Name is ",name)
        # To call a funcion within same class 
        self.func()
        print(" Age is",age)


objStudent = student("HariBol",4000)
objStudent.func()
objStudent.paramFunc("HarKrishna",8)
