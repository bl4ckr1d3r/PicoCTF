import base64

with open('enc_flag', 'r') as file:
    encoded_message = file.read()
    
decoded_message = base64.b64decode(encoded_message).decode('utf-8')
decoded_message = decoded_message.strip("b'").strip("'")
decoded_message = base64.b64decode(decoded_message)
decoded_message = decoded_message.decode('utf-8')
flag = ""
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            shifted = ord(char) - shift_amount
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def brute_force_caesar(ciphertext):
    for shift in range(26):
        decrypted = caesar_decrypt(ciphertext, shift)
        if "pico" in decrypted:
            print("Your flag is here : ", decrypted)

brute_force_caesar(decoded_message)

 
