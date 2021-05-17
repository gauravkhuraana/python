
class A:
      # This is a function which returns length  
      def __len__(self):
          return 0
      
      def __init__(self,age,name):
          self.age=age
          self.name=name
      #non static method
      def test_remainder(self,divident,divisor):
          remainder=divident%divisor
          print (divident, " % ", divisor, " = ", remainder)
     
      #Static method
      @staticmethod
      def test_remainderStatic(divident,divisor):
          remainder=divident%divisor
          print (divident, " % ", divisor, " = ", remainder)
      
      @classmethod
      # in place of self you can use cls or any other variable it
      def test_remainderClass(cls,divident,divisor):
          remainder=divident%divisor
          print (divident, " % ", divisor, " = ", remainder)
      

obj = A(10,"HAri bol")
print(bool(obj))
    #calling non static method
print(obj.test_remainder(100,3))
    
    #calling static method
    #print(test_class1().test_remainderStatic(200,3))   
print(A.test_remainderStatic(200,3))   

    #we can even call static method via object
print(obj.test_remainderStatic(300,7))

    #Class methods are similar to static
    #StaticMethod is used for utility 
    #ClassMethod are more like decorators and used to return values like constructor
     #Can change state of a class unlike static
print(obj.test_remainderStatic(400,9))
 
   

