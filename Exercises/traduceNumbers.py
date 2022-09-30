# Write a program that traduces your phone number to text using a dictionary
numbers = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
# Ask for phone number
phone = input('Insert your phone number: ')

# Traduce input to text
full_phone_number = ""
for number in phone:
    full_phone_number += numbers.get(number, "-") + " "

# Show result
print(full_phone_number)
