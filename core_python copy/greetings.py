import time
TimeStamp = int(input("Enter The Time: "))
TimeStamp = (time.strftime("%H:%M:%S"))
if int(0<=TimeStamp<=11):
    print("Good Morning")
elif int(12<=TimeStamp<=16):
    print("Good Afternoon")
else:
    print("Good Night")     

