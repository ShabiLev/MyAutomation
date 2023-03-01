# Range is from until "smaller" than the value - range(5)=from 0 - 4 ==> until < 5

# for x in range(10):
#     if x == 2:
#         continue # "Jumps" over the single iteration
# print(x)

# for x in range(1, 100, 3): # (1, 100, 3) - From, Until, Iteration
#     print(x)

# userInput = input("Please enter a number between 1-10: ")
# while not userInput == '7':
#     userInput = input("Wrong number, try again: ")
# print("Success!")

# Function
# def main(argument):
#     print("Hello!")
#     print (argument * 2) or any use for the argument
#
# main(argument to use) # call the main function

# def run(name, last):
#     return "Hello " + name + " " + last
# or
# var1 = run(last = "blabla", name = "Shabi") #Hello Shabi blabla
# var1 = run("shabi", "blabla") # Hello Shabi blabla

# print(var1)

# or
# print(f"{name}{last}")

# return = "brake" the function, stop it from continue
# pass = is a placeholder to meanwhile not put nothing in the function for now
# yield = pause\suspend the function, return the yield value than continue again with the function

#
# Global variable
# name = "John" # outside the function
# def main():
#         print(name)
#
# def main2():
#         print(name)
#
# # Local Variable
# def main():
#         name = "John"
#         print(name)

# Data Structure

# my_list = [5, "a", True]
# # my_list.append() # Add another element in the next index
# # my_list.pop(0) # Remove the value from the 0 Index
# # my_list.insert(1,7) # Insert the number 7 to Index 1 and shift the rest
#
# # Run in the lenght of the list (the Python way)
# for tempVar in my_list:
#     print(tempVar)
# # or
# # Run in the lenght of the list (NOT the Python way)
# for i in range(len(my_list)):
#     print(my_list[i])

# Tuple (Too-Pel) this list is constant, cannot Edit like "List", like seasons
# x =  1,2,3,4
# y = ('Summer', 'Winter', 'Fall', 'Spring')

# Dictionary
# my_dictionary = {'key1': value1, 'key2': value2, 'key3': value3}
# my_dictionary['key1'] = value5 # Change a value
# print(my_dictionary.keys()) # Print all the keys
# print(my_dictionary.values()) # Print all the values
# print (my_dictionary['key1']) # Prints the Value of 'key1'
# del(my_dictionary['key1']) # Delete 'key1': value1

# Keyboard input
# name = int(input("Something: ")) # casting the input to integer

