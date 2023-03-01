# print("")
# print("A")
#
# x = input("Please enter the first number: ")
# y = input("Please enter the second number: ")
# if x > y:
#     print("The first number is bigger!")
# elif x < y:
#     print("The second number is bigger!")
# else:
#     print("The numbers are equal!")
#
# print("")
# print("B")
# for x in range(5):
#     print(x)
#
# print("")
# print("C")
# season = input("Please enter 1-4: ")
# print("You entered: " + season)
# #season = 2
# if season == str(1):
#     print("It is Summer now")
# elif season == str(2):
#     print("It is Winter now")
# elif season == str(3):
#     print("It is fall now")
# elif season == str(4):
#     print("It is Spring now")
# else:
#     print("season cannot be determine")
#
# print("")
# print("D")
# count = 1
# while count < 11:
#     print(count)
#     count = count+1
# # 1. 10 Times
# # 2. 10
#
# print("")
# print("E")

# name = input("Enter your name: ")
# last = input("Enter your last: ")
# age = input("Enter your age: ")
# phone = input("Enter your phone number: ")
# abroad = input("did you fly abroad: ")
# curr = input("what is the current $ value? ")
# my_dictionary = {'name': name, 'last': last, 'age': int(age), 'phone': phone, 'abroad': abroad, 'curr': float(curr)}
#
# print(f"Thank you {my_dictionary['name']} {my_dictionary['last']}, your age is: {my_dictionary['age']}")
#
#
# print("")
# print("F")


# print("")
# print("G")
# def printHello():
#     print("Hello")
#
# def calculate(num1, num2):
#     result = num1 + num2
#     print(result)
#
# printHello()
# calculate(5, 3.2)

# print("")
# print("M")
#
# def printPiramid(levels):
    # Number of levels in the pyramid
    #levels = 10

#     # Outer loop for creating levels
#     for i in range(1, levels + 1):
#         # Inner loop for printing spaces
#         for j in range(levels - i):
#             print(" ", end="")
#         # Inner loop for printing stars
#         for k in range(2 * i - 1):
#             print("*", end="")
#         # Move to the next line after one row of the pyramid is complete
#         print("")
#
# printPiramid(5)

#
# for i in range(7):
#     for j in range(7):
#         if i == j or i+j == 6:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print("")
# # This code uses two nested for loops and an if statement to print the X shape.
# # The outer for loop (for i in range(7)) is responsible for moving the cursor to the next line after every iteration,
# # and the inner for loop (for j in range(7)) is responsible for printing the stars and spaces on each line.
# # The if statement checks if i and j are equal (for the first diagonal) or if i + j is equal to 6 (for the second diagonal)
# # and prints a "*" if either of these conditions is met. If the conditions are not met, a space is printed instead.


# print("")
# # print("P")
#
# tup = ('h', 'e', 'l', 'l', 'o')
# print ((tup[0]), (tup[1]), (tup[2]), (tup[3]),(tup[4])) # h e l l o
# newtup = str(tup)
# print(newtup) # ('h', 'e', 'l', 'l', 'o')
# tupstr = (tup[0])+(tup[1])+(tup[2])+(tup[3])+(tup[4])
# print(tupstr) #hello

# print("")
# print("Q")
# print("")
# def get_smallest_number(numbers):
#     smallest = numbers[0]
#     for number in numbers:
#         if number < smallest:
#             smallest = number
#             print("The smallest number is:", smallest)
#     return smallest
#
# numbers = [3, 5, 1, 9, 7]
# print("The smallest number is:", get_smallest_number(numbers))

# # This program defines a function get_smallest_number that takes a list of numbers as its argument.
# # The function initializes a variable smallest with the first element of the list and then loops over the rest of the elements.
# # For each element, if it is smaller than the current value of smallest, the value of smallest is updated to be the smaller value.
# # Finally, the function returns the smallest number found in the list.

# def printOut(value1, value2, value3):
#     my_dictionary = \
#         {
#         'key1': value1,
#         'key2': value2,
#         'key3': value3
#         }
#     for tempVar in my_dictionary:
#         print(tempVar)
#
# printOut(1,2,3)

# print("")
# print("L")
# print("")
#
# # numbers = [3, 5, 1, 9, 7]
# # for tempVar in numbers:
# #     print(tempVar)
# my_dictionary = {'key1': 3, 'key2': 2, 'key3': 5}
# for val in my_dictionary:
#     print(val)

# def sumNumbersInList():
#     # numbers = input("Enter a 3 digit number: ")
#     numbers = "1 2 3 4 5"
#     number = [int(x) for x in numbers.split()]
#     print(sum(number))
#
# sumNumbersInList()

# def sumUserInput():
#     lst = []
#     errors = []
#     numbers = input("Enter any digits: ")
#     for num in numbers: #For each
#         try:
#             lst.append(int(num)) #Cast the String input into Integer and add them one by one to the list
#             #print(sum(lst)) #Sum the numbers in the List
#         except ValueError:
#             errors.append(num)
#     print(f"{errors} are Not numbers")
#     print(f"The total value of you numbers is: {sum(lst)}") # Sum the numbers in the List
# sumUserInput()
        # # Enter any digits: 12e351r653r
        # # ['e', 'r', 'r'] are Not numbers
        # # The total value of you numbers is: 26

