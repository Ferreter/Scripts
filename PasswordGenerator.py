import random
import string

def generate_random_password(length=24):
    letters = string.ascii_letters  # all letters (both lowercase and uppercase)
    digits = string.digits  # digits '0123456789'
    special_chars = '!@#$%^&*()'  # additional special characters

    
    pool = letters + digits + special_chars

    # Generate a random password
    password = ''.join(random.choice(pool) for _ in range(length))

    return password


if __name__ == "__main__":
    generated_password = generate_random_password()
    print("Generated Password:", generated_password)
