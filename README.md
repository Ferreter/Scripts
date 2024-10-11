# Index of Scripts below 
1. [File Organizer Script](#file-organizer-script)
2. [Temporary File Remover](#temporary-file-remover)
3. [Recycle Bin Cleaner ](#recycle-bin-cleaner)
4. [Large File Finder](#large-file-finder)
5. [Password Generator](#password-generator)


# File Organizer Script
This Python script is designed to help you organize files in a directory based on their file extensions. It provides a user-friendly interface for selecting a target directory and categorizes files into specific folders based on their extensions.

## Features

- Organizes files into categories such as **Images**, **Documents**, **Audio/Video**, **Programs**, **Archived**, and **Coding**.
- Provides a **dry run** option to preview file movements before they happen.
- Displays a **progress bar** while moving files to keep track of the operation's progress.
- Creates an **"Others"** folder for files that do not fit into any predefined category.

## How to Use

1. **Run the script in a Python environment**.
   
2. You will be prompted with the following options to choose a target directory:
   - `1. Downloads (Default)`
   - `2. Desktop (Default)`
   - `3. Enter a custom directory path`

   Select the desired option by entering the corresponding number (`1`, `2`, or `3`). If you choose option `3`, you can enter a custom directory path.

3. **Dry Run Option**:  
   After selecting the directory, you’ll be asked if you want to perform a **dry run**. Choosing `y` will simulate the process and display which files would be moved, without actually moving them.

4. The script will create subdirectories within the selected target directory for various file categories, including:
   - **Images**
   - **Documents**
   - **Audio/Video**
   - **Programs**
   - **Archived**
   - **Coding** (New)
   - **Others** (for uncategorized files)

   Files matching the extensions of each category will be moved to their respective subdirectories.

5. Any errors encountered during the process will be displayed in the console.

### Supported File Categories

| Category      | Supported Extensions                                                                                      |
|---------------|----------------------------------------------------------------------------------------------------------|
| **Images**    | `jpeg`, `JPG`, `jpg`, `png`, `gif`, `webp`, `tiff`, `tif`, `psd`, `raw`, `bmp`, `svg`, `ai`, `eps`         |
| **Documents** | `doc`, `docx`, `html`, `htm`, `odt`, `pdf`, `xls`, `xlsx`, `ods`, `ppt`, `pptx`, `txt`, `log`, `xlsm`, `odp` |
| **Audio/Video** | `webm`, `mpg`, `mp2`, `mpeg`, `mpe`, `mpv`, `ogg`, `mp3`, `mp4`, `m4p`, `m4v`, `avi`, `wmv`, `mov`, `qt`, `flv`, `swf`, `avchd` |
| **Programs**  | `ppk`, `lnk`, `bat`, `bin`, `cmd`, `com`, `cpl`, `exe`, `inf1`, `ins`, `msc`, `msi`, `msp`, `pif`, `scr`, `vb`, `vbe`, `vbs`, `sh`, `deb`, `jar`, `java` |
| **Archived**  | `rar`, `7z`, `zip`, `tar.gz`                                                                              |
| **Coding**    | `html`, `css`, `js`, `py`, `c`, `cpp`, `php`, `xml`, `json` (New)                                         |

Files that do not fit into any of the above categories will be moved to an **"Others"** folder.

### Example Usage

```bash
$ python file_organizer.py
```

# Temporary File Remover

The Temporary File Remover is a Python script designed to help you remove temporary files from a directory. It provides the flexibility to specify a custom directory or use the system's temporary directory as a default option.

## Features

- Remove temporary files from a specified directory.
- Use the system's temporary directory as a default option.
- Customizable criteria for identifying temporary files.

## How to Use

1. Run the script in a Python environment:

   ```
   python temp_file_remover.py
   ```

2. You will be prompted with the following options:

   - Enter the directory path to remove temp files from (default: system's temporary directory).
   - Press Enter to use the default directory (system's temporary directory).

3. The script will identify and remove files from the specified directory that match the criteria for temporary files. By default, it looks for files with extensions `.tmp` and filenames starting with "temp_". You can customize these criteria in the script.

4. Any errors encountered during the file removal process will be displayed with details.

## Customization

You can customize the criteria used to identify temporary files in the script. By default, it checks for files with the following characteristics:

- File extensions ending with `.tmp`.
- Filenames starting with "temp_".

To customize the criteria, modify the `remove_temp_files()` function in the script.

## Example Usage

Here's an example of how to use the script:

```
python temp_file_remover.py
```

The script will prompt you to specify a directory or use the default system's temporary directory and then remove temporary files from that directory.

## Disclaimer

Use this script with caution, especially when removing files. Ensure that you have backups of important data, as the script will permanently delete files that match the specified criteria.

Certainly! Here's a `README.md` file generated for your script that cleans up files older than a week from the recycle bin:


# Recycle Bin Cleaner

The Recycle Bin Cleaner is a Python script designed to help you clean up files that have been in the recycle bin for more than a week. It specifically targets the Windows recycle bin.

## Features

- Remove files older than one week from the Windows recycle bin.
- Simple and straightforward script.

## How to Use

1. Run the script in a Python environment:

   ```
   python recycle_bin_cleaner.py
   ```

2. The script will automatically locate the Windows recycle bin folder (typically "C:\$Recycle.Bin") and check for files that have been in the recycle bin for more than a week (604800 seconds).

3. Any files that meet the age criteria will be permanently removed from the recycle bin.

4. Any errors encountered during the removal process will be displayed with details.

## Disclaimer

Use this script with caution, especially when removing files. Ensure that you have backups of important data, as the script will permanently delete files that match the specified criteria.

## Customization

This script is specifically designed for the Windows recycle bin. If you need to adapt it for other platforms or customize the age criteria, you can modify the script accordingly.

## Example Usage

Here's an example of how to use the script:

```
python recycle_bin_cleaner.py
```

The script will automatically locate and clean the Windows recycle bin.


# Large File Finder

This Python script allows you to find and optionally move files that are 100MB or larger within a specified directory.

## Prerequisites

- Python 3.x

## Usage

1. Clone or download the script to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script by entering the following command:

   ```
   python large_file_finder.py
    ```
Follow the prompts:

You will be asked to enter a directory path. You can leave it empty to use the default directories (Downloads or Desktop).

The script will then scan the specified directory and its subdirectories to find files that are 100MB or more in size. The path of each large file will be displayed as it is found.

After the scan, you will be prompted to decide whether you want to move the large files to a new directory.

If you choose to move the files, a new directory named "100MbMore" will be created in the same location as the input directory. All the large files will be moved into this new directory.

The script will display a message indicating the number of files that have been moved.


# Password Generator

This Python script generates a secure, random password using a combination of letters, digits, and special characters.

## Features

- Generates passwords with a mix of **lowercase** and **uppercase letters**, **digits**, and **special characters**.
- The default password length is set to **24 characters**.
- The password length can be easily customized by passing a different length as an argument to the function.

## How to Use

1. **Run the script in a Python environment**.

2. By default, the script generates a password with **24 characters**, but you can modify the `length` parameter in the `generate_random_password()` function to adjust the password length.

3. The password will be printed in the console once generated.

### Example Usage

```bash
$ python PasswordGenerator.py
```

The script will output something like:

```bash
Generated Password: A1b2C3d4E5f6G7!@#$%^
```

### Customizing Password Length

If you'd like to generate a password of a specific length, modify the call to `generate_random_password()` in the script:

```python
# Example: Generate a password of 16 characters
generated_password = generate_random_password(16)
```

This will produce a 16-character password.

## Password Character Set

The password is generated using the following set of characters:

- **Letters**: `a-z`, `A-Z` (lowercase and uppercase)
- **Digits**: `0-9`
- **Special Characters**: `!@#$%^&*()`
