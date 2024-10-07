"""Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com
This program hacks messages encryped with the Caesar cipher by doing
a brute force attack against every possible key.
More info at:
https://enwikipedia.org/wiki/Caesar_cipher
View this code at https://nostartch.com/big-book-small-python-projcest
Tags: tiny, beginner, cryptography, math"""

print ('Caesar Cipher Hacker, but Al Sweigart al@inventwithpython.com')

# Let the user speciy the message to hack:
print ('Enter the encrypted Caesar cipher message to hack.')
message = input('> ')

# Every possible symbol that can be encrypted/decrypted:
# (This must match the symbols used when encrypting the message)
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)): # Loop thorugh every possible key.
    translated = ''

    # Decrypt each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol) # get the number of the symbol
            num = num - key # Decrypt the number.

            # Handle the wrap around if num is less than 0:
            if num < 0:
                num = num + len(SYMBOLS)

            # Add decrypted number's symbol to translated
            translated = translated + SYMBOLS[num]
        else:
            # Just add the symbol without decrypting:
            translated = translated + symbol

    # Display the key being tested, along with the decrypted text:
    print ('Key #{}: {}'.format(key, translated))