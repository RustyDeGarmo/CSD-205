'''
Rusty DeGarmo
Professor Payne
Intro to Programming with Python
4 April 2021
Fiber Optic Calculator'''

#The purpose of this code is to welcome a fiber optics customer and calculate the cost of their order for them


print("Hello and welcome to Fiber Optics Specialists!")

company = input("What is your company called? ")
footage = input("\n" + company + ", How many feet of fiber do you need to have installed? ")

total = 0.87 * int(footage)

print("\n" + "Each foot of fiber costs $0.87 to install. " + company + ", your order will cost $" + str(total)) 

'''I can't seem to get it to work as expected within the sublime editor. When I build the program, 
it seems to be working but the program doesn't progress after I enter some input. I type in my 
company name, hit enter, and the cursor just goes to the next line. The program doesn't prompt the next
input. It works fine from the command line though. Any idea what I might be doing wrong in sublime?'''
