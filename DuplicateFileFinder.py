import os
import hashlib
from collections import defaultdict
from tqdm import tqdm

# Function to get user input for the directory
def get_target_directory():
    default_options = {
        '1': os.path.expanduser('~') + '/Downloads',
        '2': os.path.expanduser('~') + '/Desktop',
    }

    print("Choose a target directory:")
    print("1. Downloads (Default)")
    print("2. Desktop (Default)")
    print("3. Enter a custom directory path")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '3':
        custom_directory = input("Enter a custom directory path: ")
        target_dir = os.path.expanduser(custom_directory)
    else:
        target_dir = default_options.get(choice, default_options['1'])

    return target_dir

# Function to calculate file hash (MD5)
def calculate_hash(file_path, chunk_size=1024):
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(chunk_size), b""):
                hash_md5.update(chunk)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None
    return hash_md5.hexdigest()

# Function to find duplicate files
def find_duplicates(directory, dry_run=False):
    files_by_hash = defaultdict(list)

    # Traverse the directory recursively
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path)

            if file_hash:
                files_by_hash[file_hash].append(file_path)

    # List duplicate files
    duplicates = [file_list for file_list in files_by_hash.values() if len(file_list) > 1]

    # If dry run, just print the duplicates
    if dry_run:
        print("\n--- Duplicate Files Found (Dry Run Mode) ---")
        for file_list in duplicates:
            print(f"\nDuplicate group (Hash: {calculate_hash(file_list[0])}):")
            for file in file_list:
                print(file)
    else:
        print("\n--- Duplicates Detected ---")
        for file_list in duplicates:
            print(f"\nDuplicate group (Hash: {calculate_hash(file_list[0])}):")
            for file in file_list:
                print(file)

    return duplicates

# Function to delete duplicates (optional)
def delete_duplicates(duplicates, keep_first=True):
    for file_list in duplicates:
        if keep_first:
            file_list = file_list[1:]  # Keep the first file, delete the rest
        for file in file_list:
            try:
                os.remove(file)
                print(f"Deleted {file}")
            except Exception as e:
                print(f"Error deleting {file}: {e}")

if __name__ == "__main__":
    target_directory = get_target_directory()

    # Ask the user if they want a dry run
    dry_run = input("Do you want to perform a dry run? (y/n): ").lower() == 'y'

    print(f"Searching for duplicate files in '{target_directory}'...")
    duplicates = find_duplicates(target_directory, dry_run=dry_run)

    if dry_run:
        print("\nDry run completed. No files were deleted.")
    else:
        if duplicates:
            delete = input("\nDo you want to delete the duplicates? (y/n): ").lower() == 'y'
            if delete:
                delete_duplicates(duplicates)
            else:
                print("No files were deleted.")
        else:
            print("No duplicates found.")
