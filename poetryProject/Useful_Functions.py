import datetime
import logging


def get_current_time():
    now = datetime.datetime.now()
    cur_date_time = now.strftime("%d-%m-%Y %H:%M:%S")
    return cur_date_time


def log_info(errorText, Value):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s', file='C:\\Users\\shabil\\OneDrive - Ofakim Group\\Desktop\\log.txt')

    return log_info()



import ctypes  # An included library with Python install.
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
# Mbox('Your text', 'Your title', 1)

##  Styles:
##  0 : OK
##  1 : OK | Cancel
##  2 : Abort | Retry | Ignore
##  3 : Yes | No | Cancel
##  4 : Yes | No
##  5 : Retry | Cancel
##  6 : Cancel | Try Again | Continue