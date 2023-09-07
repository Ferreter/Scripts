
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

The script will guide you through selecting a target directory and then organize files based on their extensions.

## Disclaimer

Use this script with caution, especially when organizing files. Always make sure to have backups of your data before performing any file-moving operations.
