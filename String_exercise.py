#Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line

'''street = "Satya Margh"
city = "Ahmedabad"
country = "India"

address = street + '\n' + city + '\n' + country
print(address,'\n')

address = f"{street}\n{city}\n{country}"
print(address)'''
    
#Create a variable to store the string "Earth revolves around the sun"
#Print "revolves" using slice operator
#Print "sun" using negative index

'''string =  "Earth revolves around the sun"
print(string[6:15])
print(string[-3:])'''

#Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.

'''fruits = 4
vegetables = 5
print(f"I eat {vegetables} veggies and {fruits} fruits daily") '''

#I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.

'''s = 'maine 200 banana khaye'

s = s.replace('200', '10')
print(s)
s = s.replace('banana', 'samosa')
print(s)
s = s.replace('200', '10').replace('banana', 'samosa')
print(s)'''