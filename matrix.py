# For user input 

A=([1,2],[3,4])
B=([2,4],[5,6])
A=([1,2,3],[4,5,6])
B=([1,2,3,4],[5,6,7,8],[1,2,3,4])

print (" Matrix one print ")
 
for row in range(len(A)):
   for col in range(len(A[row])):
    print(A[row][col],end=" ")
   print()
 
 
 
print (" Matrix second print ")
for row in range(len(B)):
   for col in range(len(B[row])):
    print(B[row][col],end=" ")
   print()
print(" Matrix final print ")



print (" Final matrix would be having below dimension ")
print (len(A),len(B[row]))

C=[[0 for i in range(len(B[0]))] for j in range(len(A))]

   

sum=0
print ("Final matrix is ")

for row in range(len(A)):
    for col in range(len(B[row])):
        for counter in range(len(B[row])-1):
            #print(row,counter) 
            #print(A[row][counter])
            sum=sum+A[row][counter]*B[counter][row]
        #print("sum =",sum,end=" ")
        #print(row,col)
        C[row][col]=sum
    sum=0
    print()     

print ("Final matrix is ")
for row in range(len(C)):
   for col in range(len(C[row])-1):
    print(C[row][col],end=" ")
   print()	

"""
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append(int(input())) 
    matrix.append(a) 
  
# For printing the matrix 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 
    */
    
    """
    