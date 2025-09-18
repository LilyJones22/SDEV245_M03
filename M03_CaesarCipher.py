FIRST_CHAR_CODE = ord("A")
LAST_CHAR_CODE = ord("Z")
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1


def caesar_shift(message, shift): 
    result = "" # placeholder for converted text

    for char in message.upper(): # converts entire message string to uppercase for simplicity
        if char.isalpha(): # checks if character is a letter
            char_code = ord(char) # getting ASCII of character
            new_char_code = char_code + shift # adds shift value to ASCII value of character

            if new_char_code > LAST_CHAR_CODE: # makes sure all ASCII values stay that of letters only
                new_char_code -= CHAR_RANGE

            if new_char_code < FIRST_CHAR_CODE:
                new_char_code += CHAR_RANGE

            new_char = chr(new_char_code) # character of new ASCII value

            result += new_char

        else: 
            result += char # adds character as is if not letter

    print (result)


user_message = input("Message to Encrypt: ")
user_shift_key = int(input("Shift Key (integer): "))

caesar_shift(user_message, user_shift_key)