# Password has to be 8 characters long
# Can contain any sort of letters, numbers, and $%#@

import re

def main():

    #This regular expression ensures that a string contains at least:
        # one lowercase letter
        # one uppercase letter
        # one digit
        # and one special character from the set [@$#%]
        # Minimum length of 8 characters, without matching any substrings.
    valid_password = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#%])[A-Za-z\d$@$#%]{8,}$")

    user_password = ''
    
    while(not valid_password.search(user_password)):
        print("Enter a password that is:")
        print('\t- At least 8 characters')
        print('\t- Contains 1 upper and lowercase letter')
        print('\t- Contains 1 digit')
        print('\t- And can only contain special characters from: $ % @ or #')
        
        user_password = input()
        
if __name__ == '__main__':
    main()