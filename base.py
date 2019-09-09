import sys
from sys import argv

import requests

BASE_URL = "https://restcountries.eu/rest/v2"


def get_capital_city_by_country(country_name):
    resource = "/name/"
    country_name = country_name.capitalize()
    response = requests.get(BASE_URL + resource + country_name)
    if response.status_code == 200:
        country_json = response.json()
        for country_object in country_json:
            if country_name in country_object['name']:
                capital_city = country_object['capital']
                return str(capital_city).strip('[]')
            else:
                return "Unable to find the country in the database"
    elif response.status_code == 404:
        return "Invalid URL. Server returned ", response.status_code
    else:
        return requests.exceptions.RequestException


def get_capital_city_by_code(country_code):
    resource = "/alpha/"
    country_code = country_code.upper()
    response = requests.get(BASE_URL + resource + country_code)
    if response.status_code == 200:
        code = response.json()
        res = type(country_code) != int
        if res:
            if len(country_code) == len(code['alpha2Code']) or len(country_code) == len(code['alpha3Code']):
                if country_code == code['alpha2Code'] or country_code == code['alpha3Code']:
                    capital_city = code['capital']
                    return str(capital_city).strip('[]')
            else:
                return "Code has to be alphabets only"
    elif response.status_code == 404:
        return "Invalid URL. Server returned ", response.status_code
    else:
        return requests.exceptions.RequestException


def process_input(user_param):
    print(user_param)
    if user_param == "":
        while True:
            print("Select 1 to find capital city by country name, 2 to find capital city by code or 0 to exit the "
                  "program: ")
            user_selection = input()
            if user_selection not in ("1", "2", "0"):
                print("Choice not within the specified ones \n")
                continue
            elif user_selection == "1":
                capital = get_capital_city_by_country(input("Enter the name of the country: "))
                print(capital)
            elif user_selection == "2":
                capital = get_capital_city_by_code(input("Enter a country code : "))
                print(capital)
            elif user_selection == "0":
                print("Program ends now")
                break


if len(sys.argv) > 1:
    process_input(user_param=sys.argv[1])
else:
    process_input(user_param="")

