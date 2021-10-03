'''
Rusty DeGarmo
Professor Payne
Intro to Programming with Python
17 April 2021
'''

# Declare a dictionary of all of the Expanse novels/novellas and their release
# year

expanseDict = {
    "Leviathan Wakes" : "2011",
    "Caliban's War" : "2012",
    "Abaddon's Gate" : "2013",
    "Cibola Burn" : "2014",
    "Nemesis Games" : "2015",
    "Babylon's Ashes" : "2016",
    "Persepolis Rising" : "2017",
    "Tiamat's Wrath" : "2019",
    "Leviathan Falls" : "2021",
    "Drive" : "2012",
    "The Churn" : "2014",
    "The Butcher of Anderson Station" : "2011",
    "The Last Flight of the Cassandra" : "2012",
    "Gods of Risk" : "2012",
    "The Vital Abyss" : "2015",
    "Strange Dogs" : "2017",
    "Auberon" : "2019",
}

# Print the keys of my dictionary
for key in expanseDict:
    print(key)

# Ask the user to select a book
releaseYear = input("Select a book to see when it was released: ")

# Print the book that the user selected and the year that it was released
print(f"\n{releaseYear} was released in the year {expanseDict[releaseYear]}\n")



