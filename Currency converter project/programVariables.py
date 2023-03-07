import os
import requests
import xmltodict
import json


import tkinter as tk

logfilePath = "C:\\Users\\" + os.getlogin() + "\\OneDrive - Ofakim Group\\Desktop\\log.txt"
api_key = "96753c12b86447d2932b6502c72e36a8"
url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
response = requests.get(url)
data = json.loads(response.text)

curdict = {
    "USD": 3.52,
    "ILS": 0.28,
    "EUR": 4.23
}

fromilsdic = {
    "USD": 0.28,
    "EUR": 0.26
}

fromusddic = {
    "ILS": 3.58,
    "EUR": 0.94
}

fromeurdic = {
    "USD": 1.07,
    "ILS": 3.82
}


def get_curr_ils_rate():
    ils_rate = data["rates"]["ILS"]
    return ils_rate


def get_curr_usd_rate():
    usd_rate = data["rates"]["USD"]
    return usd_rate


def get_curr_eur_rate():
    eur_rate = data["rates"]["EUR"]
    return eur_rate