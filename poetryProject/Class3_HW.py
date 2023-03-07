# import logging
#
# try:
#     a = 1/0
# except ZeroDivisionError:
#     print("Error")
#
#
import logging
from datetime import datetime

# from PIL import Image, Image
# # Call an image
# im = Image.open("C:\\Users\\shabil\\Downloads\\images.jfif")
# print(im.format, im.size, im.mode) # Get the image info.
# im.show() #Present the Image
#
# # Create a new image with a white background
# image = Image.new('RGB', (300, 300), color='white')
#
# # Draw a red rectangle on the image
# draw = Image.Draw(image)
# draw.rectangle((50, 50, 250, 250), fill='red')
#
# # Save the image to a file
# image.save('C:\\Users\\shabil\\Downloads\\rectangle.png')

# def getcurrentTime():
#     now = datetime.now()
#     year = now.strftime("%Y")
#     month = now.strftime("%m")
#     day = now.strftime("%d")
#     time = now.strftime("%H:%M:%S")
#
#     date_time = now.strftime("%d-%m-%Y %H:%M:%S")
#     print(date_time)
# getcurrentTime()


def sumUserInput():
    lst = []
    errors = []
    numbers = input("Enter any digits: ")
    for num in numbers: #For each
        try:
            lst.append(int(num)) #Cast the String input into Integer and add them one by one to the list
            #print(sum(lst)) #Sum the numbers in the List
        except ValueError:
            errors.append(num)
    print(f"{errors} are Not numbers")
    print(f"The total value of you numbers is: {sum(lst)}") # Sum the numbers in the List
sumUserInput()
# Enter any digits: 12e351r653r
# ['e', 'r', 'r'] are Not numbers
# The total value of you numbers is: 26

# print(dir(locals()['__builtins__']))

# from Useful_Functions import get_current_time
#
# print(get_current_time())
#
# try:
#     failure = 1/0
# except ZeroDivisionError as ZeroDivisionError:
#     print(ZeroDivisionError)
# # # Error types:
# logging.basicConfig(filename='C:\\Users\\shabil\\Downloads\\example.log', encoding='utf-8', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
# # DEBUG:root:This message should go to the log file
# # INFO:root:So should this
# # WARNING:root:And this, too
# # ERROR:root:And non-ASCII stuff, too, like Øresund and Malmö

import logging
from Useful_Functions import get_current_time
from Useful_Functions import Mbox

filePath = "C:\\Users\\shabil\\OneDrive - Ofakim Group\\Desktop\\log.txt"
logging.basicConfig(level=logging.INFO)

def sum_user_input():
    lst = []
    errors = []
    numbers = input("Enter any digits: ")
    for num in numbers:
        try:
            lst.append(int(num))
        except ValueError:
            errors.append(num)
    my_file = open(filePath, 'a')
    my_file.write(f'\n {get_current_time()} - WARNING: {errors} are Not numbers')
    my_file.write(f'\n {get_current_time()} - INFO: The total value of you numbers is: {sum(lst)}')
    my_file.close()
    print(f"The total value of you numbers is: {sum(lst)}")
    Mbox('The total value of you numbers is', f'{sum(lst)}', 1)

sum_user_input()
