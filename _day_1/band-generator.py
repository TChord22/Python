#Exercise 1 String manipulation

# print("Day 1 - String Manipulation")
# print("String Concatenation is done with the" + " " + "sign.")
# print('e.g. print("Hello" + "world")')
# print("New lines can be \ncreated with a backslash and n.")

##############################################################################

#Exercise 2 > User data

# The input is what gathers the users name
# The print hello is added to follow through as prompt has been answered

# name = input("What is your name? ")
# print("Hello " + name) #Started conversation
# input("How are you? ")
# print("That is nice to hear " + name + " I am doing better than you are right now")
# input("Ask me why? ")
# print("Well " + name + " I get to spend time with you of course!")

############################################################################

#Exercise 3 > Word Counting

# print(len('Tasha'))

#First try with variable name
# name = input('What is your name? ') #variable
# print("Your name count is ", len(name))
#Second try without variable
# print("Your name count is", len( input("What is your name? ")))

#Exercise 4 > Variables

# a = input("a: ")
# b = input("b: ")

# temp = a
# a = b
# b = temp

# # a, b = b, a

# print("a = " + a)
# print("b = " + b)


## Band Generator

city_name = input("What is the name of the city you grew up in?\n")
#
user_age = input("What is your age?\n")
#
pet_name = input("Your pets name?\n")

input("Click enter to see your band name! ")
print("Your band name is:" + city_name + " " + pet_name + " " + user_age)