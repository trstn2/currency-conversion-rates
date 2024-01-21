import requests

# Function to get exchange rates
def get_exchange_rates(base_currency):
    api_key = "your_api_key_here"  # Replace with your API key
    url = f"https://open.er-api.com/v6/latest/{base_currency}?apikey={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        return data["rates"]
    except Exception as e:
        print(f"Error fetching exchange rates: {e}")
        return None

# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    exchange_rates = get_exchange_rates(from_currency)

    if exchange_rates is not None and to_currency in exchange_rates:
        converted_amount = amount * exchange_rates[to_currency]
        return converted_amount
    else:
        print("Invalid currency or error fetching exchange rates.")
        return None

# Main program
print("Choose your base currency:")
base_currency_option = input("(CAD|USD|EUR|GBP|JPY): ").upper()

if base_currency_option not in ["CAD", "USD", "EUR", "GBP", "JPY"]:
    print("Invalid base currency option. Exiting.")
    exit()

option = float(input("How much money would you like to convert? "))
user_option = input("What currency would you like to convert to: (CAD|USD|EUR|GBP|JPY): ").upper()

if user_option not in ["CAD", "USD", "EUR", "GBP", "JPY"]:
    print("Invalid target currency option. Exiting.")
    exit()

converted_amount = convert_currency(option, base_currency_option, user_option)

if converted_amount is not None:
    print(f"{option} {base_currency_option} is equal to {converted_amount:.2f} {user_option}")
