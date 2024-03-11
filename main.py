#Parker Johnson
#Checks if password is valid
#must have at needs at least 8 characters, both uppercase and lowercase, and at least one digit. Can have special characters

import re
import random
import string

def validatePassword(password):

  passwordRegex = re.compile(r'[a-zA-Z0-9(\.\$\!\@\+\&\%\#)?]{8,}')
  results = passwordRegex.search(password)
  if results == None:
    return False
  else:
    return True

def newPassword():
  possibleCharacters = string.ascii_lowercase + string.ascii_uppercase + string.digits
  digits = string.digits
  password = ""

  length = random.randint(8, 15)

  for i in range(length + 1):
    n = random.randint(0, len(possibleCharacters))
    # !!Think how to make sure there is lowercase, uppercase, and digits in password !!#

  return password

def main():

  finalPassword = input("Please enter possible password: ")

  while not validatePassword(finalPassword):
    user = input("Type 'y' if you want to try another password, type 'n' if you want one made for you: ")
    if user == 'y' or user == 'Y':
      finalPassword = input("Please enter possible password: ")
    elif user == 'n' or user == 'N':
      finalPassword = newPassword()

  print("SUCCESS: Your new password is {}".format(finalPassword))
      