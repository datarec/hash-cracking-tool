# # Hash matcher | 18/03/2024 | coolpancakes
# Matches hashes. 


import hashlib
import os
import time

# function to clear the screen.

def clean_display():
    OPERATING_SYSTEM = os.name
    if OPERATING_SYSTEM == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# class that contains objects that are used throughout the script

def dehasher(value):
    clean_display()
    class encryption_types():
        def __init__(self):
            self.SHA256 = hashlib.sha256()
            self.SHA256_TITLE = 'SHA256'
            self.MD5 = hashlib.md5()
            self.MD5_TITLE = 'MD5'
            self.SHA1 = hashlib.sha1()
            self.SHA1_TITLE = 'SHA1'
            self.SHA512 = hashlib.sha512()
            self.SHA512_TITLE = 'SHA512' 

    # stores the class inside of a namespace to access 
    
    encryption = encryption_types()

    # if value which is the hash_menu namespace from the main_menu function is equal to 
    # the following string values then make METHOD_PLACEHOLDER equal to the string number selected from the main_menu
    
    if value == '1':
        METHOD_PLACEHOLDER = encryption.SHA256_TITLE
    elif value == '2':
        METHOD_PLACEHOLDER = encryption.MD5_TITLE
    elif value == '3':
        METHOD_PLACEHOLDER = encryption.SHA1_TITLE
    elif value == '4':
        METHOD_PLACEHOLDER = encryption.SHA512_TITLE

    # input hash and use METHOD_PLACEHOLDER to tell the user which encryption mode they've selected. 

    HASH_INPUT = input(f'''

     {METHOD_PLACEHOLDER} | Dehash   
   
  [|       Enter hash to commence dehashing.                 
   |]            1) Return to menu.                  
  [|                       
   |]                       
                         
     {METHOD_PLACEHOLDER}> ''')

    # if HASH_INPUT equal to '1' return to menu
    
    if HASH_INPUT == '1':
        main_menu()


    # opens the password txt file to read
    
    with open('mn7.txt', 'r') as unhashed_passwords:

        # iterates list of passwords  
        # through each iteration it casts unhashed to a f string & raw string in order to -
        # strip the escape character from the line of text. 

        for unhashed in unhashed_passwords:
            unhashed_real = fr'{unhashed}'.strip('\n')

            # for each iteration encrypt each password in sha256 to match it with the users one. 

            if value == '1':
                hashe = hashlib.sha256()
            elif value == '2':
                hashe = hashlib.md5()
            elif value == '3':
                hashe = hashlib.sha1()
            elif value == '4':
                hashe = hashlib.sha512()

            hashe.update(f'{unhashed_real}'.encode())
            hashed_passwords = hashe.hexdigest()
        
            # check IF hashed_passwords is equal to '' and if it's equal to that str then
            # print the value associated with the hash. 
        
            if hashed_passwords == HASH_INPUT:
                print(f'\n     CRACKED: {unhashed_real}')
                quit()
        
            # ELSE, keep iterating through the list until a match is found. 
        
            else:
                print(f'     Trying: {hashed_passwords} FAIL!')

        print('\n     No hashes were successful, status: Failed.')
       

def main_menu():
    clean_display()
    
    hash_menu = input('''

     made by coolpancakes | hashleaf | https://github.com/cookpancakes
     _____________________ __________ ___________________________________  
    
    | H |   1) SHA-256 - RAW hash    3) SHA1
    | A |                  
    | S |   2) MD5 - Raw hash        4) SHA512
    | H |   
    | L |                         
    | E |            
      |             
      |              
    | A |  
    | F |     
    
            MENU> ''')

    # if, elif statements used for 
    
    if hash_menu == '1':
        dehasher(hash_menu)
    elif hash_menu == '2':
        dehasher(hash_menu)
    elif hash_menu == '3':
        dehasher(hash_menu)
    elif hash_menu == '4':
        dehasher(hash_menu)
    else:
        print('Please select using numbers. ')
        main_menu()

main_menu()
