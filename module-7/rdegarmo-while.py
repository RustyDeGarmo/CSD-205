'''
Rusty DeGarmo
Professor Payne
Intro to Programming with Python
22 April 2021
'''

#A while loop that determines how long it takes for an investment to double
#at a given interest rate


#get the initial investment from the user and convert it to an integer. Then get
#the interest rate and convert it to a float.
investment = input("Tell me how much are you investing and I will tell you\
how long it will take to double: ")
investment = int(investment)
originalInvestment = investment
rate = input("What is the interest rate on your investment in decimal format? ")
rate = float(rate)

#define a variable to keep track of the years
years = 0

#A while loop that keeps going until the investment doubles
while investment < originalInvestment*2:
    years += 1
    investment += investment * rate

#Output the final investment and how long it will take to double
print(f"It will take {years} years for your initial investment of \
{originalInvestment} to double. You will have a principle balance of \
{investment}")



