

def test_dataTypes():
    print("\n")
    
    a=10
    print(type(a))
    
    a="10"
    print( type(a))
    
    a='10'
    print(type(a))
    
    a=10.52
    print(type(a))

    a=10j
    print(a)

    a=(1,2,3)
    print(a)

    a=[1,2,3]
    print(a)

    a=range(6)
    print(a)

    a=True
    print(a)

    a="1234344"
    print(a[0])
    print(a[3])

    a=" Hello Krishna"
    print(a[-5:-1])


def test_list():
     a=[1,'a',"hare",45.5]

     print ("List is ",a)

     # printing list in various ways
     print("Printing via iteration item by item ")
     for x in a:
         print(x)

     print("Printing via indexing")
     for i in range(len(a)):    
         print(a[i])

     #List Comprehension
     print("Printing via List comprehension")
     [print(x) for x in a]



