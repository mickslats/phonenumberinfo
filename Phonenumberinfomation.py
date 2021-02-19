import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
import pyttsx3

Edith = pyttsx3.init()

Phonenumber=input("Enter your phonenumber: ")

number=phonenumbers.parse(Phonenumber)

############################ Info section ###################################


national = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.NATIONAL)

internationl = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

formatnumber = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)

geo = geocoder.description_for_number(number,'en')

carr = carrier.name_for_number(number,'en')



#####################################################################################

############################ Location infomation with voice  ###################################
Edith.say(national)
Edith.runAndWait()
Edith.say(internationl)
Edith.runAndWait()
Edith.say(formatnumber)
Edith.runAndWait()
Edith.say(geo)
Edith.runAndWait()
Edith.say(carr)
Edith.runAndWait()

###################################################################################################

############################ Location infomation with no voice  ###################################

print(national)
print(internationl)
print(formatnumber)
print(geo)
print(carr)

###################################################################################################
