a=10;
if(a<10):
  print("the value is ",a)
elif(a<20 | a>=10):
  print("value is more than 10 the value is ",a)  
else:
  print("more value")  


# nested
num = 18
if (num < 0):
  print("Number is negative.")
elif (num > 0):
   if(num<=10):
    print("Number is between 1-10")
   elif(num > 10 and num == 20):
    print("Number is between 11-20")
   else:
       print("Number is greater than 20")
else:
  print("Number is zero")  