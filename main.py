import string

from sympy import false

alphabet = list(string.ascii_lowercase + string.digits  + string.punctuation)

def ceaser(message, shift_amount, action_type):
    text = ""
    if action_type == 'decode':
        shift_amount *= -1

    for letter in message:
        if letter not in alphabet:
            text += letter
        else:
            shifted_position = abs(alphabet.index(letter) + shift_amount)
            shifted_position %= len(alphabet)
            text += alphabet[shifted_position]

    if action_type == 'decode':
        print(f"Your Decoded Text: {text}")
    else:
        print(f"Your Encoded Text: {text}")


exit_caesar = False

while not exit_caesar:
    instruction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower().strip()
    user_message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n").strip())
    ceaser(message=user_message, shift_amount=shift, action_type=instruction)
    should_continue = input("Do you want to continue? Type 'y' for Yes and 'n' for No: ").lower().strip()
    if should_continue != 'y':
        exit_caesar = True
        print("Goodbye! Do visit again.")