# Import and display the logo from art.py
from art import logo

# Initialize the control variable to keep the program running
go_on = True

# Define the alphabet list for the Caesar cipher
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
print(logo)


def caesar(original_text, shift_amount, encode_or_decode):
    """Performs Caesar cipher encryption or decryption."""
    output_text = ""

    for letter in original_text:
        # Reverse the shift if decoding
        if encode_or_decode == "decode":
            shift_amount *= -1

        # If the character is not in the alphabet, leave it unchanged
        if letter not in alphabet:
            output_text += letter
            continue

        # Calculate the new position after shifting
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)  # Wrap around if necessary
        output_text += alphabet[shifted_position]

    # Print the final result
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# Main loop to keep the program running until the user decides to stop
while go_on:
    # Get user choice: encode or decode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    # Get the message to be encrypted or decrypted
    text = input("Type your message:\n").lower()

    # Get the shift value and convert it to an integer
    shift = int(input("Type the shift number:\n"))

    # Call the caesar function with the provided inputs
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask the user if they want to continue or exit
    go_on = input("Do you want to continue? yes or no: ")
    if go_on == "no":
        go_on = False
