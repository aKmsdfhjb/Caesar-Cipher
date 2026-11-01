def caesar(text, shift, encrypt=True):
    """Encrypt or decrypt text with a classical Caesar shift.

    Non-alphabetic characters and the original letter case are preserved.
    """
    if not isinstance(text, str):
        return "Text must be a string."
    if not isinstance(shift, int) or isinstance(shift, bool):
        return "Shift must be an integer value."
    if shift < 1 or shift > 25:
        return "Shift must be an integer between 1 and 25."

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    amount = shift if encrypt else -shift
    shifted_alphabet = alphabet[amount:] + alphabet[:amount]
    table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper(),
    )
    return text.translate(table)


def main():
    """Run the interactive command-line interface."""
    print("CAESAR CIPHER")
    choice = input("1. Encrypt\n2. Decrypt\nChoose an option: ").strip()

    if choice not in {"1", "2"}:
        print("Choose 1 to encrypt or 2 to decrypt.")
        return

    message = input("Enter text: ")
    raw_shift = input("Enter shift (1-25): ").strip()

    try:
        shift = int(raw_shift)
    except ValueError:
        print("Shift must be an integer value.")
        return

    result = caesar(message, shift, encrypt=(choice == "1"))
    print("Result:", result)


if __name__ == "__main__":
    main()
