import string

# Caesar Cipher Implementation
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char in string.ascii_lowercase:
            shift_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text += shift_char
        elif char in string.ascii_uppercase:
            shift_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += shift_char
        else:
            encrypted_text += char
    return encrypted_text

# Text Preprocessing Function
def preprocess_text(text):
    text = text.lower()
    text = ''.join(filter(str.isalpha, text))
    return text