import re

phone_number = re.findall(r"[\d]{11}", "My phone number is 0762376193")

print((phone_number[0]))