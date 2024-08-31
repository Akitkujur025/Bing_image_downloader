# Bing Image Downloader

A Windows application built with Python and `tkinter` to download images from Bing based on a search query. This tool is useful for creating datasets for deep learning applications like object detection with YOLO, Detectron2, etc. The app has been packaged into a `.exe` file using PyInstaller, with all assets included.

## Features

- **Search & Download:** Download up to 10,000 images for a specified query.
- **Folder Selection:** Choose a folder to save the downloaded images.
- **Progress Tracking:** Displays a progress bar during the download.
- **Easy Distribution:** The app is packaged as a standalone `.exe` file.

## Installation

1. Clone the repository or download the code.
2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Create the executable using PyInstaller:
    ```bash
    pyinstaller --onefile --add-data "picture.png;." app.py
    ```
4. The executable will be in the `dist` folder along with the necessary assets.

## Usage

1. Launch the `.exe` file from the `dist` folder.
2. Enter your search query and set the limit for the number of images.
3. Select the folder where images will be saved.
4. Click "Search" to start downloading images.
5. Monitor the progress with the built-in progress bar.

## Files

- `app.py`: The main script for the application.
- `picture.png`: Icon for the app.
- `dist/`: Folder containing the compiled `.exe` file and assets.

## Applications

- **Dataset Creation:** Ideal for generating large datasets for deep learning models, including object detection tasks.
  
## Credits

Developed by Ankit Kujur.
