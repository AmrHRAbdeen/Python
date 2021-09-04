# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

### Get info about a specific phone number
### Needed Packages ###
### pip install phonenumbers

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
PhoneNumber=""

## Get the Country of the number
ch_number = phonenumbers.parse(PhoneNumber,"CH")
print(geocoder.description_for_number(ch_number,"en"))

##  Get Service Provider
servic_number=phonenumbers.parse(PhoneNumber,"RO")
print(carrier.name_for_number(servic_number,"en"))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
