

import random
import string

def generate_password(length):
    """Generate a random password of given length"""
    
    # All characters: letters + digits + symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate random password
    password = ""
    for i in range(length):
        password = password + random.choice(characters)
    
    return password

def main():
    print("RANDOM PASSWORD GENERATOR")
    print("=" * 40)
    
    while True:
        try:
            length = int(input("\nEnter password length: "))
            
            if length < 4:
                print("Password length must be at least 4!")
                continue
            
            # Generate password
            password = generate_password(length)
            
            # Show result
            print("\n" + "=" * 40)
            print("YOUR GENERATED PASSWORD:")
            print(f"   {password}")
            print("=" * 40)
            
            # Ask if user wants another
            again = input("\nGenerate another? (y/n): ")
            if again.lower() != 'y':
                print("\n Goodbye!")
                break
                
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main()
