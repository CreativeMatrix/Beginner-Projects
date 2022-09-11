from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):  
    encrypted_word = ""
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            shifted_index = index + shift
            shifted_letter = alphabet[shifted_index]
            encrypted_word += shifted_letter
        else:
            encrypted_word += letter
    print(f"The encrypted text is '{encrypted_word}'")

def decrypt(text, shift):
    decoded_word = ""
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            shifted_index = index - shift
            shifted_letter = alphabet[shifted_index]
            decoded_word += shifted_letter
        else:
            decoded_word += letter
    print(f"The decrypted text is '{decoded_word}'")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Please re-run program and retype 'encode' or 'decode' to start cypher.")
    
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if result == "no":
        should_continue = False
        print("GoodBye!")
