import os
import shutil

def get_user_directory():
    user_input = input("Enter the directory path (leave empty for default: Downloads or Desktop): ").strip()
    if not user_input:
        user_input = os.path.expanduser("~/Downloads")
        if not os.path.exists(user_input):
            user_input = os.path.expanduser("~/Desktop")
    return user_input

def find_large_files(directory):
    large_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size >= 100 * 1024 * 1024:  # 100 MB in bytes
                print(f"Found large file: {file_path} ({file_size} bytes)")
                large_files.append(file_path)
    return large_files

def move_large_files(large_files):
    if not large_files:
        print("No files found with size 100MB or more.")
        return

    move_prompt = input("Do you want to move these files? (yes/no): ").strip().lower()
    if (move_prompt == "yes" | move_prompt == "y" | move_prompt = "Y") :
        new_directory = os.path.join(os.path.dirname(large_files[0]), "100MbMore")
        os.makedirs(new_directory, exist_ok=True)
        for file in large_files:
            shutil.move(file, os.path.join(new_directory, os.path.basename(file)))
        print(f"{len(large_files)} files have been moved to {new_directory}.")
    else:
        print("No files were moved.")

if __name__ == "__main__":
    user_directory = get_user_directory()
    large_files = find_large_files(user_directory)
    move_large_files(large_files)
