'''
Rusty DeGarmo
Professor Payne
Intro to Programming with Python
22 April 2021
'''

#A function that converts miles to kilometers

def kiloConverter(miles):
    kilometers = miles * 1.6093
    print(f"{miles} miles is {kilometers} kilometers.")

#Create string variables to keep the code clean
greeting = "\nHello, I can convert miles to kilometers."
prompt = "How many miles do you want to convert? "

#Greet the user, get the input miles, and convert the input to a float
print(greeting)
miles = input(prompt)

#test that the input is a number
try:
    miles = float(miles)
except:
    print("\nThat was not a number.")
else: #call the function
    print("")
    kiloConverter(miles)

#print the empty string to create some space
print("")

