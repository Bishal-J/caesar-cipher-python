import string

alphabet = list(string.ascii_lowercase)

instruction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
user_message = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(message, shift_amount, action_type):
    text = ""
    if action_type == 'decode':
        shift_amount *= -1

    for letter in message:
        shifted_position = abs(alphabet.index(letter) + shift_amount)
        shifted_position %= len(alphabet)
        text += alphabet[shifted_position]

    if action_type == 'decode':
        print(f"Your Decoded Text: {text}")
    else:
        print(f"Your Encoded Text: {text}")

ceaser(message=user_message, shift_amount=shift, action_type=instruction)