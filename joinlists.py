
a='MeContext/ManagedElement/ENodeBFunction/EUtranCellTDD/EUtranFreqRelation'
b='STNWLAAFBBULTE0275782/STNWLAAFBBULTE0275782/1/STNWLAAFBBULTE027578217/8763'

x=a.split("/")
y=b.split("/")


# using list comprehension + zip() 
# interlist element concatenation 
res = [i + '=' + j for i, j in zip(x, y)] 

print (res)

#items[3:6] = [''.join(items[3:6])]
res=[','.join(res[3:])]
print(res)
