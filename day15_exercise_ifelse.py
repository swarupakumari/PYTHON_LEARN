from datetime import datetime

# Get current date and time
now = datetime.now()

# Extract only the time
# current_time = now.strftime("%H:%M:%S")
hr = now.hour
if(hr>=1 and hr<=11):
   print("Good Morning")
elif(hr>=12 and hr<=15):
   print("Good afternoon") 
elif(hr>=16 and hr<=19):
   print("Good Evening") 
else:
   print("good night")     
