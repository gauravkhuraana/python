
x=10

def test_globalVariables():
    x=40
    print("1. I have acces to variables name",x)
    print("2. I have acces to variables name",x)

def test_globalRetainsValueEvenIfSomeOtherFuncChangedIt():
    print("3. I have acces to variables name",x)    

def test_createGlobalFromLocal():
    global y
    y=50

def test_tryToUseGlobal():
    print("Value of y as seen here",y)    