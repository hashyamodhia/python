#We have following information on countries and their population (population is in crores),
'''
Country 	 Population
China 	 143
India 	 136
USA   	  32
Pakistan  21
'''
#Using above create a dictionary of countries and its population

population = {"china" : 143,
              "india" : 136,
              "usa": 32,
              "pakistan":21}

#Write a program that asks user for three type of inputs,
#print: if user enter print then it should print all countries with their population in this format,

#china==>143
#india==>136
#usa==>32
#pakistan==>21

#add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it

#remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!

#query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.


# def print_all():
#     for country, p in population.items():
#         print(f"{country}==>{p}")
        
# def query():
#     country = input("Enter the country name: ")
#     country = country.lower()
    
#     if country not in population:
#         print("Country doesn't exist in our dataset. Terminating")
#         return
#     print(f"Population of {country} is: {population[country]} crore")
    
# def add():
#     country = input("Enter the country name to add: ")
#     country = country.lower()
    
#     if country in population:
#         print(f"{country} already exits")
#         return
#     p = input(f"Enter population for {country}: ")
#     population[country] = p
#     print_all()
    
# def remove():
#     country = input("Enter the country name to remove: ")
#     country = country.lower()
    
#     if country not in population:
#         print("Country doesn't exist in our dataset. Terminating")
#         return
#     del population[country]
#     print_all()
    
# def main():
#     op = input("Enter operation (add, remove, query or print): ")
#     if op.lower() == 'add':
#         add()
#     elif op.lower() == 'remove':
#         remove()
#     elif op.lower() == 'query':
#         query()
#     elif op.lower() == 'print':
#         print_all()
#     else:
#         return
        
# if __name__ == '__main__':
#     main()
    
    
#You are given following list of stocks and their prices in last 3 days,
'''
Stock 	Prices
info 	[600,630,620]
ril  	[1430,1490,1567]
mtl 	    [234,180,160]
'''

#Write a program that asks user for operation. Value of operations could be,
#print: When user enters print it should print following,

#info ==> [600, 630, 620] ==> avg:  616.67
#ril ==> [1430, 1490, 1567] ==> avg:  1495.67
#mtl ==> [234, 180, 160] ==> avg:  191.33

# import statistics

# stocks = {
#     "info" : [600, 630, 620],
#     "ril" : [1430, 1490, 1567],
#     "mtl" : [234, 180, 160]
#     }

# def print_all():
#     for stock, price_list in stocks.items():
#         avg = statistics.mean(price_list)
#         print(f"{stock} ==> {price_list} ==> avg", round(avg,2))
        

# def add():
#     s = input("Enter a stock ticker to add: ")
#     p = input(f"Enter the price of {s}: ")
#     p = float(p)
    
#     if s in stocks:
#         stocks[s].append(p)
        
#     else:
#         stocks[s] = [p]
#     print_all()
    
# def main():
#     op = input("Enter operation (print, add): ")
    
#     if op.lower() == "print":
#         print_all()
        
#     elif op.lower() == "add":
#         add()
    
#     else:
#         print(f"Invalid {op}")

# if __name__ == '__main__':
#     main()
    
#Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and returns area, circumference and diameter. You should get these values in your main program by calling circle_calc function and then print them

from math import pi
 
def circle_calc(radius):
    area = pi * (radius**2)
    area = round(area, 2)
    circumference = 2*pi*radius
    circumference = round(circumference, 2)
    diameter = radius/2
    diameter = round(diameter, 2)
    return area, circumference, diameter

if __name__ == '__main__':
    r = input("Enter a radius: ")
    r = float(r)
    area, c, d = circle_calc(r)
    print(f"Area: {area}, circumference: {c}, diameter: {d}")
    