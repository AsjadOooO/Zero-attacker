import requests
import re
from colorama import Fore

def phone_locator(phone_number, api_key):
    url = f"https://api.apilayer.com/number_verification/validate?number={phone_number}"
    headers = {
        "apikey": api_key
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

def print_phone_details(phone_details):
    print("Phone Details:")
    print(f"Number: {phone_details['number']}")
    print(f"Country: {phone_details['country_name']} ({phone_details['country_code']})")
    print(f"Carrier: {phone_details['carrier']}")
    print(f"Line Type: {phone_details['line_type']}")
    print(f"Location: {phone_details['location']}")
    print(f"Valid: {phone_details['valid']}")
api_key1 = input("Enter your, Api Key")

api_key = "32WfDqB635jMOWkxdeC1r2BXew1tXHLU"
api_key1 = api_key
flag = 0
while True:
    if (len(api_key)<=32):
        flag = -1
        break
    elif not re.search("[a-z]", api_key):
        flag = -1
        break
    elif not re.search("[A-Z]", api_key):
        flag = -1
        break
    elif not re.search("[0-9]", api_key):
        flag = -1
        break

    elif re.search("\s" , api_key):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Api-Key")
        break
 
if flag == -1:
    print("Not a Valid Api-Key ")

api_key = input("Enter your, Api Key")


phone_number = input("Enter the phone number to locate: ")

phone_details = phone_locator(phone_number, api_key)
print_phone_details(phone_details)