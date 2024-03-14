#After flipping a coin 10 times you got this result,
'''result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]'''
#Using for loop figure out how many times you got heads
'''count = 0
for toss in result:
    if toss == 'heads':
        count = count + 1
print (f"Heads were {count} times")'''

#Print square of all numbers between 1 to 10 except even numbers
'''for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i*i)'''
#Your monthly expense list (from Jan to May) looks like this,
'''expense_list = [2340, 2500, 2100, 3100, 2980]'''
'''month_list = ["Jan", "Feb", "March", "April", "May"]'''
#Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.

'''amount = int(input("Enter a amount"))
month = -1
for i in range(len(expense_list)):
    if amount == expense_list[i]:
        month = i
        break
if month != -1:
    print(f"You spent {amount} in month of {month_list[month]}")
else:
    print ("No expenses matched")'''

#Lets say you are running a 5 km race. Write a program that,

#Upon completing each 1 km asks you "are you tired?"
#If you reply "yes" then it should break and print "you didn't finish the race"
#If you reply "no" then it should continue and ask "are you tired" on every km
#If you finish all 5 km then it should print congratulations message

'''for i in range(5):
    print(f"you ran {i+1} kms")
    tired = input("You tired ?")
    if tired == 'yes':
        break
if i == 4:
    print(f"u completed {i + 1} kms")
else:
    print(f"u finished {i + 1} kms only")'''
#Write a program that prints following shape

#*
#**
#***
#****
#*****

'''for i in range(1,6):
    s = ''
    for j in range(i):
        s += "*"
    print(s)'''
