#Writing is only allowed if you open in write mode so is reading 
# both can't be done at the same time
# you cannot delete a file while its in use (r/w)
import os

print("Hello Python")

#value=raw_input("Enter the value")
#print("Value enetered was = ",value)

#val=input("value")
#print("value is ",val)

file=open("newfile.txt","r")
file2=open("leapYear.py")
file3=open("s:/Automation/style.css")

print(file.read())
#print(file1.read())
print(file2.readline())

#file2.write("\n test")
file4=open("leapYear.py","w")

file4.write("#new line in leap year")

file5=open("s:/Automation/style.css","r")

#file5.write("\n ok test") 
print(file5.read())
file=open("newfile.txt","w")

file.write("Just testing")
#print(file.read())
file.close()
#os.remove("newfile.txt")

file2.close()
file3.close()
file4.close()
file5.close()

if os.path.exists("a.txt"):
 os.remove("a.text")
 print("File Deleted successfully")
else:
 print("The file does not exist")


