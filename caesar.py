def encrypt(message, shift):
    encrypted_chars = []
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_chars.append(encrypted_char)
        else:
            encrypted_chars.append(char)
    return ''.join(encrypted_chars)

def decrypt(encrypted_message, shift):
    decrypted_chars = []
    for char in encrypted_message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - base - shift + 26) % 26 + base)
            decrypted_chars.append(decrypted_char)
        else:
            decrypted_chars.append(char)
    return ''.join(decrypted_chars)

def main():
    while True:
        print("Caesar Cipher Program")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = encrypt(message, shift)
            print("Encrypted message:", encrypted_message)

        elif choice == "2":
            encrypted_message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = decrypt(encrypted_message, shift)
            print("Decrypted message:", decrypted_message)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
