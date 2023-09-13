import os
import time

# Function to remove files older than a week from the recycle bin
def clean_recycle_bin():
    # Get the path to the recycle bin
    recycle_bin_path = "C:\$Recycle.Bin"

    if not os.path.exists(recycle_bin_path):
        print("Recycle bin not found.")
        return

    # Get the current time
    current_time = time.time()

    # Iterate through files in the recycle bin
    for root, _, files in os.walk(recycle_bin_path):
        for file in files:
            file_path = os.path.join(root, file)

            # Get the file's modification time
            file_mtime = os.path.getmtime(file_path)

            # Check if the file is older than a week (604800 seconds)
            if current_time - file_mtime >= 604800:
                try:
                    print(f"Removing {file_path}")
                    os.remove(file_path)
                except Exception as e:
                    print(f"Error removing {file_path}: {e}")

if __name__ == "__main__":
    print("Cleaning up the recycle bin...")
    clean_recycle_bin()
    print("Recycle bin cleanup completed.")
