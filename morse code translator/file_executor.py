#A simple project on Morse code translation from plain Text to morse code and vice versa

#Importing the user defined modules
import encryption as cipher
import decryption as decipher                           

print("\t\t\t\t***********************")
print("\t\t\t\t THIS IS MORSE CODE TRANSLATOR ")
print("\t\t\t\t***********************")
print("\t\t\t\t THE PROGRAM IS STARTING ")
print("\t\t\t\t***********************")
print("\n")

ch= input("Press 'E' for encryption and 'D' for decryption: ")
print("\n")

if (ch=='E' or ch== 'e'):
    plain_Text= input("Enter Text to be encrypted: ").upper()
    print("\n")
    
    #Calling encryption function
    cipher.encryptor(plain_Text)

elif (ch=='D' or ch== 'd'):
    morse_code= input("Enter morse code to be decrypted: ")
    print("\n")
    
    #Calling decryption function
    decipher.decryptor(morse_code)

else:
    print("Invalid input!!!")        