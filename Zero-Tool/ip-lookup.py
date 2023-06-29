import requests
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

api_key = "22WfDqB635jMOWkxdeC1r2BXew1tXHLU"

phone_number = input(Fore.MAGENTA+"Enter the phone number to locate: ")

phone_details = phone_locator(phone_number, api_key)
print_phone_details(phone_details)