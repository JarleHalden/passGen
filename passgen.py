import pyperclip
from random import choice

UPPER   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER   = "abcdefghijklmnopqrstuvwxyz"
DIGITS  = "0123456789"
SYMBOLS = "!@#$%&*-_=?"

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    charset = ""
    if use_upper:   charset += UPPER
    if use_lower:   charset += LOWER
    if use_digits:  charset += DIGITS
    if use_symbols: charset += SYMBOLS

    if not charset:
        print("Must use at least one type of chars")
        return None

    return "".join(choice(charset) for _ in range(length))

def ask(prompt, default=True):
    svar = input(f"{prompt} (y/n, enter={('y' if default else 'n')}): ").strip().lower()
    if svar == "": return default
    return svar == "y"

def main():
    print("\nPassword generator\n")

    length = input("Length (enter=16): ").strip()
    length = int(length) if length.isdigit() else 16

    use_upper   = ask("Uppercase?")
    use_lower   = ask("Lowercase?")
    use_digits  = ask("Digits?")
    use_symbols = ask("Symbols?", default=False)

    while True:
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

        if password:
            print(f"\nPassword: {password}")
            print(f"Length:   {length}\n")
            pyperclip.copy(password)
            print("Copied to clipboard!")

        again = input("\nGenerate again? (y/n, enter=y): ").strip().lower()
        if again == "n":
            break


if __name__ == "__main__":
    main()