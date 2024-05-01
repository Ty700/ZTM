#####################################################################################
# Usage:                                                                            #
#   Checks any number of passwords to see if they have been leaked                ` #
#                                                                                   #
# How to use:                                                                       #
#   # Can accept any number of passwords to check.                                  #
#   # Insert passwords as plain text <- Will be changed soon.                       #
#                                                                                   #
#   Example:                                                                        #
#       python3 checkpass.py <password1> <password2> ... <passwordn>                #
#                                                                                   #
#####################################################################################

import requests
import hashlib
import sys

def leak_count(hashes, local_hash):
    hashes = (line.split(':') for line in hashes.text.splitlines())

    for hash, leak_count in hashes:
        if hash == local_hash:
            return leak_count
        
    return 0


def request_api_data(query_chars):
    url = 'https://api.pwnedpasswords.com/range/' + query_chars
    res = requests.get(url)    

    if res.status_code != 200:
        raise RuntimeError(f'Request Error: {res.status_code}')
    
    return res

def pwned_api_check(password):
    # API needs sha1 and all upper and encoded in UTF-8
    sha1password = hashlib.sha1(password.encode('UTF-8')).hexdigest().upper()
    query_chars, tail = sha1password[:5], sha1password[5:] 

    res = request_api_data(query_chars)

    return leak_count(res, tail)

def main(password_list):
    for password in password_list:
        leak_count = pwned_api_check(password)

        if leak_count:
            print(f'Password has been found {leak_count} times.')
        else:
            print(f'Password was not found.')
    
    return None

if __name__ == '__main__':
    # Todo -> Convert this so that it reads passwords from a .txt
        # Passwords will be stored as plain text in CLI as it stands now which is being saved somewhere locally.
        # If program grabs passwords from a .txt, the .txt can be deleted with ease rather than trying to figure out where the CLI saves it's previous run cmds
    main(sys.argv[1:])