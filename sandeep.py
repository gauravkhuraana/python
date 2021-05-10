def prodDigits(num):
  product=1;
  for ele in (list(str(num))):
    product *= int(ele)
 # print("The product of digits", num, "are: ", product) 
  return product



def answer(num):
 counter=0;
 while(num>10):
    num=prodDigits(num)
    counter=counter+1
 print ("MDR ",num)
 print ("MPersistence ",counter)
   

answer(0);
