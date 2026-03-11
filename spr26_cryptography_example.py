# cryptography

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 '!?."

plain_text = "apples/*-+=-"
cipher_text = ""
shift_key = 23

for letter in plain_text:

    # get numerical value of letter
    position = alphabet.find(letter)
    # check position
    if position == -1:
        # if letter not found
        cipher_text += letter
    else:
        # if letter found, apply encryption

        # apply shift key
        encrypt_position = position + shift_key
        if encrypt_position > len(alphabet)-1:
            encrypt_position -= len(alphabet)-1

        # get letter back
        encrypted_letter = alphabet[encrypt_position]

        # save encrypted letter
        cipher_text += encrypted_letter

print(f'{plain_text} is encrypted to {cipher_text}')