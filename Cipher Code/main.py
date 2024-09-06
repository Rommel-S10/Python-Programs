text = 'ucibjg zw s dtpar wio qfg qnuijgytjd'
custom_key = 'software'



def vigenere(message, key, direction=1): #vigenere comes from the last name of the creator of this method
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message


def encrypt(message, key):
    return vigenere(message, key) #direction by the default will be 1 for encryption


def decrypt(message, key):
    return vigenere(message, key, -1) #diection value is assign to -1 for decryption


print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')