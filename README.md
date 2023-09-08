
# File Organizer Script

This Python script is designed to help you organize files in a directory based on their file extensions. It provides a user-friendly interface for selecting a target directory and categorizes files into specific folders based on their extensions.

## How to Use

1. Run the script in a Python environment.

2. You will be prompted with the following options to choose a target directory:

   - **Downloads (Default)**
   - **Desktop (Default)**
   - **Enter a custom directory path**

3. Select the desired option by entering the corresponding number (1, 2, or 3). If you choose option 3, you can enter a custom directory path.

4. The script will create subdirectories within the selected target directory for various file categories, including:

   - **Images**
   - **Documents**
   - **AudioVideo**
   - **Programs**
   - **Archived**

5. It will then search for files in the current working directory (or a custom directory if specified) with extensions matching those in each category. Files found will be moved to their respective subdirectories within the target directory.

6. Any errors encountered during the file-moving process will be displayed with details.

## Supported File Categories

- **Images**: Supported extensions include jpeg, JPG, jpg, png, gif, webp, tiff, tif, psd, raw, bmp, svg, ai, eps.

- **Documents**: Supported extensions include doc, docx, html, htm, odt, pdf, xls, xlsx, ods, ppt, pptx, txt, log.

- **AudioVideo**: Supported extensions include webm, mpg, mp2, mpeg, mpe, mpv, ogg, mp4, m4p, m4v, avi, wmv, mov, qt, flv, swf, avchd.

- **Programs**: Supported extensions include ppk, lnk, bat, bin, cmd, com, cpl, exe, inf1, ins, msc, msi, msp, pif, scr, vb, vbe, vbs, sh, deb, jar, java.

- **Archived**: Supported extensions include rar, 7z, zip, tar.gz.

## Example Usage

Here's an example of how to use the script:

```
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


