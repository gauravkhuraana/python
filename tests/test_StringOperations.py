def test_stringSlicing():
    #counting from the back
    a="Hare Krishna, the value can be placed at {} , hari bol {} Krishna is the {} personality"
    print(a[-7:-1])

    b=16
    #c=a+b
    #Not Allowed to combine different data types
    #print(c)

    c=a.format(b,", Hare Krishna","supreme")
    print(a)
    print(b)
    print("b got inserted into string a \n",c)

def test_StringOps():
    a="HareKrishna"
    print("Swap title \n",a.swapcase())