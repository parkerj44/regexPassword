#Parker Johnson
#Checks if password is valid
#must have at needs at least 8 characters, both uppercase and lowercase, and at least one digit. Can have special characters
#However special characters not required

import re
import random
import string
import secrets

#Validates if password has all requirements
def validatePassword(password):

  #use of regex to check requirements
  passwordRegex = re.compile(r'[(a-z)+(A-Z)+(0-9)+(\.\$\!\@\+\&\%\#)?]{8,}')
  results = passwordRegex.search(password)
  if results == None:
    return False
  else:
    return True

#Computer generated password adding in missed requirements
def checkReq(password):
  upperCase = string.ascii_uppercase
  lowerCase = string.ascii_lowercase
  digits = string.digits

  #addition of any missed requirements
  if sum(i.islower() for i in password) == 0:
    password += secrets.choice(lowerCase)
  if sum(i.isupper() for i in password) == 0:
    password += secrets.choice(upperCase)
  if sum(i.isdigit() for i in password) == 0:
    password += secrets.choice(digits)

  return password

#Computer generated password
def newPassword():
  possibleCharacters = string.ascii_letters + string.digits
  password = ""

  #possible lengths between 8 and 15
  length = random.randint(8, 15)

  #adding random characters from possibleCharacters length amount of times
  password = ''.join(secrets.choice(possibleCharacters) for i in range(length + 1))
  password = checkReq(password)

  return password

def main():

  print("Password must have lowercase, uppercase, and at least one digit.")
  print("Special characters such as .$!@+&%# are allowed but not required")
  finalPassword = input("Please enter possible password: ")

  #will continue to run as long as password not valid
  while not validatePassword(finalPassword):
    print("ERROR: Password does not match requirements.")
    #user option
    user = input("Type 'y' if you want to try another password, type 'n' if you want one made for you: ")
    if user == 'y' or user == 'Y':
      finalPassword = input("Please enter possible password: ")
    elif user == 'n' or user == 'N':
      finalPassword = newPassword()

  print("SUCCESS: Your new password is {}".format(finalPassword))

main()
      