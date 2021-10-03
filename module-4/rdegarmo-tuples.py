'''
Rusty DeGarmo
Professor Payne
Intro to Programming with Python
4 April 2021
Tuple Iteration
'''

#initialize my food tuple
foodsTuple = ("Pizza", "Pasta", "Chicken Parmesan", "Ice Cream", "Sandwiches", "Rotisserie Chicken", "Pie", "Cheesecake", "Pot Pie", "Lasagna", "Garlic Toast", "Eggs", "Milk", "Egg Nog", "Cheese", "Bulletproof Coffee", "Almost any food")

#print the entire contents of my food tuple then a new line
print(foodsTuple, "\n")

#iterate through my food tuple with a formatted string
for food in foodsTuple:
    print(f"{food} is one of my favorite things!")

#print a new line to seperate the iterations
print("\n")

#iterate through my food tuple in reverse order
foodIndex = 0 #initialize a variable to store the negative index outside of the loop
for food in foodsTuple:
    foodIndex -= 1
    reverseFood = foodsTuple[foodIndex]
    print(f"I really enjoy {reverseFood}!")


