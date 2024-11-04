import random
import string

def generate_password(length=12):
    """Generates a random password with a default length of 12 characters."""
    
    # Define possible characters: letters (uppercase and lowercase), digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password contains at least one letter, one digit, and one punctuation
    password = []
    password.append(random.choice(string.ascii_lowercase))  # At least one lowercase letter
    password.append(random.choice(string.ascii_uppercase))  # At least one uppercase letter
    password.append(random.choice(string.digits))           # At least one digit
    password.append(random.choice(string.punctuation))      # At least one punctuation
    
    # Fill the rest of the password length with random characters
    password += random.choices(characters, k=length-4)
    
    # Shuffle the password list to make it more random
    random.shuffle(password)
    
    # Join the list into a string
    return ''.join(password)

# Example usage
if __name__ == "__main__":
    print("Randomly generated password:", generate_password())
