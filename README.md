# Python_Cryptography
Using Python to make an encryption process and an almost successful decryption process
Encryption:
Step 1: Get the word we want to encrypt
Step 2: Convert each letter into numeric values based on where they are in the alphabet
Step 3: Get the row of Pascal's triangle based on the numeric value of all the letters
Step 4: Convert the numbers in each row back into letters using mod(52)
Step 5: Create a binary key from random binary digits
Step 6: 0s are dropped and 1s are kept

Decryption:
Step 1: Get the key and ciphertext
Step 2: Create a list of letters based on the ciphertext we know and the values we don't know (the key will help us know)
Step 3: Get the last 2 known values of the list and find the distance between them
Step 4: Go through Pascal's triangle and find the rows which correspond to the numeric values of the letters and the distance between them using mod(52)
Step 5: Find the one correct row of Pascal's triangle by trying to implement each row into the ciphertext. If the row is correct, it will line up with the ciphertext
Step 6: Remove the known values of the ciphertext
Step 7: Find the second value of the correct row and convert it into a letter
Step 8: Add the letter into a list
Step 9: Repeat until there is no more ciphertext left
Step 10: Print the final message
