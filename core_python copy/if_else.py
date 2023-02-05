# Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
 # Ask user to enter his fasting sugar level
# If it is below 80 to 100 range then print that sugar is low
    # If it is above 100 then print that it is high otherwise print that it is normal
# sugar_level = int(input("Enter the sugar level: "))
# if sugar_level < 100:
#     print("sugar is low")
# elif sugar_level == 100:
#     print("sugar is normal")
# elif sugar_level > 100:
#     print("sugar is high")
# else:
#     print("Thanku for measure sugar level")                
# Using for loop figure out how many times you got heads

# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# count = 0
# count2 = 0
# for i in result:
#     if i == "heads":
#         count +=1
#     elif i == "tails":
#         count2 +=1    
# print(count,count2)   

# Print square of all numbers between 1 to 10 except even numbers

# for i in range(11):
#     if i%2 == 1:
#         print(i*i)     



# Lets say you are running a 5 km race. Write a program that,

#     Upon completing each 1 km asks you "are you tired?"
#     If you reply "yes" then it should break and print "you didn't finish the race"
#     If you reply "no" then it should continue and ask "are you tired" on every km
#     If you finish all 5 km then it should print congratulations message

# for i in range(5):
#     print(f"You ran {i+1} miles") # i starts with zero hence adding 1
#     tired = input("Are you tired? ")
#     if tired == 'yes':
#         break
# if i == 4: # 4 because the index starts from 0
#     print("Hurray! You are a rock star! You just finished 5 km race!")
# else:
#     print("You didn't finish 5 km race but hey congrats anyways! You still ran {i+1} miles")

month_list = ["January", "February", "March", "April", "May"]
expense_list = input[2340, 2500, 2100, 3100, 2980]
e = input("Enter expense amount: ")
e = int(e)

month = -1
for i in range(len(expense_list)):
    if e == expense_list[i]:
        month = i
        break

if month != -1:
    print(f'You spent {e} in {month_list[month]}')
else:
    print(f'You didn\'t spend {e} in any month')