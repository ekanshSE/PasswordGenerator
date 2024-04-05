import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        count = int(input("Enter the number of passwords to generate: "))
        
        if length < 8:
            print("Password length should be at least 8 characters for security.")
        else:
            print("\nGenerated passwords:")
            for _ in range(count):
                print(generate_password(length))
    except ValueError:
        print("Please enter valid numerical values for length and count.")

if __name__ == "__main__":
    main()
