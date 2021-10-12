import dictionary as dict

# Function used to encrypt plain text into morse code
def encryptor(inp):
    encrypted_inp= ""
    for letter in inp:
        if letter != " ":

            #Accessing the values of letters entered and seperating each by a space and storing into a variable
            encrypted_inp= encrypted_inp + dict.MORSE_CODE_DICT.get(letter) + " "
        else:
            #Providing double space if it encounters a space within letters or words
            encrypted_inp += " "
    print("The morse code is : ",encrypted_inp)
    return(encrypted_inp)
    