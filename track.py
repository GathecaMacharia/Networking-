import phonenumbers
from phonenumbers import geocoder, carrier, timezone
numbers= input("Enter your number: ")
phone_number= phonenumbers.parse(numbers)
print(f"Location: {geocoder.description_for_number(phone_number, 'en')}")
print(f"Carrier: {carrier.name_for_number(phone_number, 'en')}")
