# # Write a program with the following:
# # 1. Create a class named Dog
# # 2. Create a constructor (_init)- in class Dog with name and age parameters.
# # 3. Instantiate Dog class from main using constructor (create an object with name and age) call it rexi.
# # 4. Print rexi name in main class.
#
# class dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# # dog1 = dog('rexi', 6)
# # print(dog1.name)
#
# # Create a program with the following:
# # 1. Create a list of 3 objects of class dog (each has an age and a name)
# # 2. Iterate through the list and print all dogs names.
# dog_list = []
# dog1 = dog('rexi', 6)
# dog2 = dog('blacki', 8)
# dog3 = dog('Joya', 3)
#
# dog_list.append(dog1.name)
# dog_list.append(dog2.name)
# dog_list.append(dog3.name)
#
# print(dog_list)


# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://www.google.com/search?q=usd+to+nis&rlz=1C1GCEA_en-GBIL1043IL1043&oq=usd&aqs=chrome.1.69i57j0i131i433i512l2j0i433i512l2j69i61j69i60l2.4101j0j4&sourceid=chrome&ie=UTF-8'
# response = requests.get(url)
#
# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, 'html.parser')
#     element = soup.find('div', {'data-value': 'data-value'})
#     if element is not None: #and 'data-value' in element.attrs:
#         data_value = element['data-value']
#         print(f'The data-value is: {data_value}')
#     else:
#         print('No data-value found in element')
# else:
#     print(f'Request failed with status code {response.status_code}')

# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
# from calendar import month_name
#
# root = tk.Tk()
#
# # config the root window
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Combobox Widget')
#
# # label
# label = ttk.Label(text="Please select a month:")
# label.pack(fill=tk.X, padx=5, pady=5)
#
# # create a combobox
# selected_month = tk.StringVar()
# month_cb = ttk.Combobox(root, textvariable=selected_month)
#
# # get first 3 letters of every month name
# month_cb['values'] = [month_name[m][0:3] for m in range(1, 13)]
#
# # prevent typing a value
# month_cb['state'] = 'readonly'
#
# # place the widget
# month_cb.pack(fill=tk.X, padx=5, pady=5)


# bind the selected value changes
# def month_changed(event):
#     """ handle the month changed event """
#     showinfo(
#         title='Result',
#         message=f'You selected {selected_month.get()}!'
#     )
#
# month_cb.bind('<<ComboboxSelected>>', month_changed)
#
# root.mainloop()


import tkinter as tk


import requests
import json

import xmltodict as xmltodict

api_key = "96753c12b86447d2932b6502c72e36a8"
# url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}&base=USD"
# response = requests.get(url)
# data = json.loads(response.text)
# usd_rate = data["rates"]["USD"]
#
# eur_amount = 1
# usd_amount = eur_amount * usd_rate
# print(f"{eur_amount} EUR is worth {usd_amount} USD")
#

# Replace YOUR_APP_ID with your Open Exchange Rates API key
# url2 = f"https://openexchangerates.org/api/latest.json?{api_key}=YOUR_APP_ID&symbols=ILS,NGN"
#
# # Make a request to the API and retrieve the response
# response = requests.get(url2)
#
# # Parse the JSON response and retrieve the exchange rate for ILS to NGN
# data2 = response.json()
# ils_to_ngn_rate = data2["rates"]['NGN'] / data2["rates"]['ILS']
#
# print("Exchange rate for ILS to NGN:", ils_to_ngn_rate)
#
# url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}&symbols=ILS,USD,EUR"
# response = requests.get(url)
# data = json.loads(response.text)
# usd_rate = data["rates"]["USD"]
# ils_rate = data["rates"]["ILS"]
# eur_rate = data["rates"]["EUR"]
#
# # eur_amount = 1
# usd_amount = eur_rate * usd_rate
# print(f"{eur_rate} EUR is worth {usd_amount} USD")

# def get_curr_rates():

# import requests
# import json
#
# # Replace YOUR_APP_ID with your own app ID from Open Exchange Rates
# url = f"https://openexchangerates.org/api/latest.json?app_id=96753c12b86447d2932b6502c72e36a8"
#
# # Retrieve the currency rates data from the API
# response = requests.get(url)
# data = json.loads(response.text)
#
# # Extract the currency rates for USD, EUR, and ILS
# usd_rate = data["rates"]["USD"]
# eur_rate = data["rates"]["EUR"]
# ils_rate = data["rates"]["ILS"]
#
# # Print the currency rates
# print(f"USD rate: {usd_rate}")
# print(f"EUR rate: {eur_rate}")
# print(f"ILS rate: {ils_rate}")


# USD rate: 1
# EUR rate: 0.93664
# ILS rate: 3.587093

# To calculate how much 1 EUR is in USD, you can divide 1 by the exchange rate of 1 USD to 0.93664 EUR:
#
# 1 / 0.93664 = 1.06783

# Therefore, 1 EUR is equal to approximately 1.06783 USD.



import tkinter as tk

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.selection1 = []
        self.selection2 = []

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.label1 = tk.Label(self.frame, text='Select options for selection 1:')
        self.label1.pack()

        self.option_vars1 = []
        for i in range(3):
            var = tk.IntVar()
            chk = tk.Checkbutton(self.frame, text=f'Option {i+1}', variable=var)
            chk.pack(side='top', anchor='w')
            self.option_vars1.append(var)

        self.button1 = tk.Button(self.frame, text='Save selection 1', command=self.save_selection1)
        self.button1.pack()

        self.label2 = tk.Label(self.frame, text='Select options for selection 2:')
        self.label2.pack()

        self.option_vars2 = []
        for i in range(3):
            var = tk.IntVar()
            chk = tk.Checkbutton(self.frame, text=f'Option {i+1}', variable=var)
            chk.pack(side='top', anchor='w')
            self.option_vars2.append(var)

        self.button2 = tk.Button(self.frame, text='Save selection 2', command=self.save_selection2)
        self.button2.pack()

        self.button3 = tk.Button(self.frame, text='Calculate combination', command=self.calculate_combination)
        self.button3.pack()

    def save_selection1(self):
        self.selection1 = [i+1 for i, var in enumerate(self.option_vars1) if var.get() == 1]

    def save_selection2(self):
        self.selection2 = [i+1 for i, var in enumerate(self.option_vars2) if var.get() == 1]

    def calculate_combination(self):
        combination = set()
        for i in self.selection1:
            for j in self.selection2:
                combination.add((i, j))
        self.show_combination(combination)

    def show_combination(self, combination):
        self.new_window = tk.Toplevel(self.master)
        self.new_window.title('Combination')

        self.frame = tk.Frame(self.new_window)
        self.frame.pack()

        self.label = tk.Label(self.frame, text='The combination of selections 1 and 2 is:')
        self.label.pack()

        self.text = tk.Text(self.frame, height=5)
        self.text.pack()

        self.button = tk.Button(self.frame, text='Close', command=self.new_window.destroy)
        self.button.pack(side='bottom')

        self.text.insert('end', str(combination))

if __name__ == '__main__':
    root = tk.Tk()
    main_window = MainWindow(root)
    root.mainloop()

