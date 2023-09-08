import os
import shutil

# Function to remove temporary files from a directory
def remove_temp_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Define criteria to identify temporary files (you can customize this)
            if file.endswith('.tmp') or file.startswith('temp_'):
                try:
                    print(f"Removing {file_path}")
                    os.remove(file_path)
                except Exception as e:
                    print(f"Error removing {file_path}: {e}")

if __name__ == "__main__":
    # Get the default directory path from %temp% (or %TMP%)
    default_directory = os.environ.get('TEMP') or os.environ.get('TMP')

    # Ask the user for a custom directory path
    user_directory = input(f"Enter the directory path to remove temp files from (default: {default_directory}): ").strip()

    # Use the default directory if the user input is empty
    target_directory = user_directory if user_directory else default_directory

    if not os.path.exists(target_directory):
        print("Directory not found.")
    else:
        print(f"Removing temp files from '{target_directory}'...")
        remove_temp_files(target_directory)
        print("Temp file removal completed.")
