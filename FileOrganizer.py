import os
import shutil
import glob

# Function to get user input for the directory and provide default options
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

# Function to create a directory if it doesn't exist
def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

# Function to move files to their respective directories based on file extensions
def organize_files(source_dir, target_dir):
    # Define file extensions for different categories
    file_categories = {
        "Images": ['jpeg', 'JPG', 'jpg', 'png', 'gif', 'webp', 'tiff', 'tif', 'psd', 'raw', 'bmp', 'svg', 'ai', 'eps'],
        "Documents": ['doc', 'docx', 'html', 'htm', 'odt', 'pdf', 'xls', 'xlsx', 'ods', 'ppt', 'pptx', 'txt', 'log'],
        "AudioVideo": ['webm', 'mpg', 'mp2', 'mpeg', 'mpe', 'mpv', 'ogg', 'mp4', 'm4p', 'm4v', 'avi', 'wmv', 'mov', 'qt', 'flv', 'swf', 'avchd'],
        "Programs": ['ppk', 'lnk', 'bat', 'bin', 'cmd', 'com', 'cpl', 'exe', 'inf1', 'ins', 'msc', 'msi', 'msp', 'pif', 'scr', 'vb', 'vbe', 'vbs', 'sh', 'deb', 'jar', 'java'],
        "Archived": ['rar', '7z', 'zip', 'tar.gz']
    }

    for category, extensions in file_categories.items():
        category_dir = os.path.join(target_dir, category)
        create_directory(category_dir)

        for ext in extensions:
            pattern = os.path.join(target_dir, f"*.{ext}")  # Update pattern to target_dir
            files = glob.glob(pattern)

            print(f"Found {len(files)} files with extension '{ext}' in {source_dir}")

            for file in files:
                try:
                    print(f"Moving {file} to {category_dir}")
                    shutil.move(file, category_dir)
                except Exception as e:
                    print(f"Error moving {file} to {category_dir}: {e}")


if __name__ == "__main__":
    current_directory = os.getcwd()
    target_directory = get_target_directory()
    
    print(f"Organizing files from '{current_directory}' to '{target_directory}'...")
    organize_files(current_directory, target_directory)
    
    print("File organization completed.")
