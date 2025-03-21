import string

alphabet = list(string.ascii_lowercase)

instruction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
user_message = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_letter = alphabet.index(letter) + shift_amount
        shifted_letter %= len(alphabet)
        cipher_text += alphabet[shifted_letter]

    print(f"Your Encoded Text: {cipher_text}")


def decrypt(encrypted_text, shift_amount):
    plain_text = ""
    for letter in encrypted_text:
        shifted_letter = abs(alphabet.index(letter) - shift_amount)
        shifted_letter %= len(alphabet)
        plain_text += alphabet[shifted_letter]

    print(f"Your Decoded Text: {plain_text}")


encrypt(original_text=user_message, shift_amount=shift)
decrypt(encrypted_text=user_message, shift_amount=shift)