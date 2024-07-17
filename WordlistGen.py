import itertools
import random
import string

def generate_wordlist_from_user_input():
    strings = []
    print("Enter strings (e.g., Name, Maiden Name, Job) one per line.")
    print("Enter STOP on a new line to finish:")
    
    while True:
        user_input = input().strip()
        if user_input == "STOP":
            break
        strings.append(user_input)
    
    return strings

def generate_wordlist_from_file(filename):
    strings = []
    try:
        with open(filename, 'r') as file:
            strings = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    
    return strings

def generate_passwords(strings, num_passwords, max_length):
    passwords = set()
    
    for _ in range(num_passwords):
        random.shuffle(strings)
        combined_string = ''.join(strings)
        combined_string += ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, max_length - len(combined_string))))
        passwords.add(combined_string)
    
    return passwords

def save_wordlist_to_file(wordlist, filename):
    try:
        with open(filename, 'w') as file:
            for password in wordlist:
                file.write(password + '\n')
        print(f"Wordlist saved to '{filename}'")
    except IOError:
        print(f"Error: Unable to write to file '{filename}'")

# Main program
if __name__ == "__main__":
    print("Welcome to the Wordlist Generator for Brute force attack.")
    print("Choose input method:")
    print("1. Manually enter strings")
    print("2. Load strings from a file")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        strings = generate_wordlist_from_user_input()
    elif choice == '2':
        filename = input("Enter the filename: ")
        strings = generate_wordlist_from_file(filename)
    else:
        print("Invalid choice. Exiting.")
        exit()
    
    num_passwords = int(input("Enter the number of passwords to generate: "))
    max_length = int(input("Enter the maximum length of passwords: "))
    
    wordlist = generate_passwords(strings, num_passwords, max_length)
    
    output_filename = input("Enter the filename to save the wordlist: ")
    save_wordlist_to_file(wordlist, output_filename)
