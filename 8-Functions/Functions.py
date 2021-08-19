import sys

def addNumber(fNum, lNum): #starts the function and calls it add Number
    sumNum = fNum + lNum
    return sumNum

print(addNumber(1, 4))
#adding numbers


long_string = "I'll catch you if you fall - The Floor"

print(long_string[:4])
#print first five characters

print(long_string[-5:])
#print last 5 caracters

print(long_string[:-5])
#print everything up to last 5 characters

print(long_string[:4] + " be there")

print(long_string.capitalize())

print(long_string.find('Floor'))
#finds how many characters it is into the sentence

print(len(long_string))
#finds the lenght

print(long_string.replace('Floor', 'Ground'))
#Replaces the word

quote_list = long_string.split(' ')
print(quote_list)
#changes it to a list
