'''
Rusty DeGarmo
Professor Payne
Intro to Programming with Python
4 April 2021
Fiber Optic Calculator'''

#The purpose of this code is to welcome a fiber optics customer and calculate 
#the cost of their order for them


print("\nHello and welcome to Fiber Optics Specialists!")

#Gather the customer information
company = input("What is your company called? ")
footage = int(input("\n" + company + ", how many feet of fiber do you need to \
have installed? "))

print(footage)
#A series of if, elif, else statements to determine the customers price/foot
#I can't seem to get it to display two decimal places
if footage > 500:
    total = round(0.50 * footage, 2)
elif footage > 250:
    total = round(0.70 * footage, 2)
elif footage > 100:
    total = round(0.80 * footage, 2)
else:
    total = round(0.87 * footage, 2)

# A series of if statements to personalize order message based on order size
if footage > 500:
    print(f"\nEach foot of fiber will cost $0.50 to install because you ordered \
{footage} feet. \n{company}, your order will cost ${total}")
elif footage > 250:
    print(f"\nEach foot of fiber will cost $0.70 to install because you ordered \
{footage} feet. \n{company}, your order will cost ${total}")
elif footage > 100:
    print(f"\nEach foot of fiber will cost $0.80 to install because you ordered \
{footage} feet. \n{company}, your order will cost ${total}")
else:
   print(f"\nEach foot of fiber costs $0.87 to install with an order of {footage} \
feet. \n{company}, your order will cost ${total}") 
print()
 
