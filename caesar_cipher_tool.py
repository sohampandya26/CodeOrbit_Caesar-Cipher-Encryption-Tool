"""
Caesar Cipher Encryption Tool
CodeOrbit Tech - Cyber Security Internship (Task 2)

Encrypts and decrypts text using the classic Caesar Cipher technique,
with a user-chosen shift value (key). Non-letter characters (spaces,
numbers, punctuation) are left unchanged.
"""

import string


def caesar_shift(text: str, shift: int, mode: str) -> str:
    """Shift each letter in `text` by `shift` positions.

    mode: 'encrypt' or 'decrypt'
    """
    if mode == "decrypt":
        shift = -shift

    result = []
    for char in text:
        if char in string.ascii_uppercase:
            new_index = (ord(char) - ord("A") + shift) % 26
            result.append(chr(new_index + ord("A")))
        elif char in string.ascii_lowercase:
            new_index = (ord(char) - ord("a") + shift) % 26
            result.append(chr(new_index + ord("a")))
        else:
            result.append(char)

    return "".join(result)


def main():
    print("=== Caesar Cipher Encryption Tool ===")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    choice = input("Choose an option (1 or 2): ").strip()

    text = input("Enter your text: ")

    try:
        shift = int(input("Enter shift value (key), e.g. 3: ").strip())
    except ValueError:
        print("Shift must be a whole number. Exiting.")
        return

    if choice == "1":
        encrypted = caesar_shift(text, shift, "encrypt")
        decrypted_back = caesar_shift(encrypted, shift, "decrypt")
        print(f"\nOriginal text:   {text}")
        print(f"Encrypted text:  {encrypted}")
        print(f"Decrypted back:  {decrypted_back}")
    elif choice == "2":
        decrypted = caesar_shift(text, shift, "decrypt")
        print(f"\nEncrypted text:  {text}")
        print(f"Decrypted text:  {decrypted}")
    else:
        print("Invalid choice. Please run again and choose 1 or 2.")


if __name__ == "__main__":
    main()
