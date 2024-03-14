#Using following list of cities per country,
'''india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]'''
#Write a program that asks user to enter a city name and it should tell which country the city belongs to
#Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"

'''city = input("Enter a city: ")
if city in india:
    print(f"{city} belongs to india")
elif city in pakistan:
    print(f"{city} belongs to pakistan")
elif city in bangladesh:
    print(f"{city} belongs to bangladesh")
else:
    print(f"{city} doesnt belongs to any country")'''
    
'''city1 = input("Enter city1: ")
city2 = input("Enter city2: ")
if city1 in india and city2 in india:
    print(f"{city1} and {city2} belongs to india")
elif city1 in pakistan and city2 in pakistan:
    print(f"{city1} and {city2} belongs to pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print(f"{city1} and {city2} belongs to bangladesh")
else:
    print(f"{city1} and {city2} doesnt belongs to any country")'''
    
#Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
#Ask user to enter his fasting sugar level
#If it is below 80 to 100 range then print that sugar is low
#If it is above 100 then print that it is high otherwise print that it is normal

'''sugarlevel = int(input("Enter sugar level: "))

if sugarlevel > 100:
    print("Sugar is high")
elif sugarlevel < 80:
    print("Sugar is low")
else:
    print("Sugar is normal")'''
    