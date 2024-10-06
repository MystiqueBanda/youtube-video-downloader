# YouTube Video Downloader

This is a Python script that allows you to download YouTube videos in MP4 format using the `yt-dlp` library. The video is saved in a specified folder on your system, with the video title as the filename. The script automatically installs `yt-dlp` if it is not already installed.

## Features
- Automatically installs the required dependencies (`yt-dlp`).
- Downloads videos in MP4 format.
- Saves the video with the original YouTube title as the filename.
- Updates the creation and modification times of the downloaded video to the time of download.
- Simple and clean user interface with minimal output during the download process.

## Requirements
- Python 3.x installed on your system.
- Internet connection (to install `yt-dlp` and download videos).

## Installation
1. Clone or download the repository to your local machine.
2. Ensure you have Python 3 installed. If not, you can download it from the official Python website: https://www.python.org/downloads/
3. Open a terminal/command prompt and navigate to the folder where the script is located.

## Usage
1. Run the Python script by executing the following command in the terminal:

    ```bash
    python <script_name>.py
    ```

    Replace `<script_name>` with the actual name of the Python file (e.g., `yt_downloader.py`).

2. When prompted, enter the URL of the YouTube video you want to download.

3. Provide the folder path where you want the video to be saved. For example:

    ```
    enter the folder path where the vid should be saved: C:\Downloads
    ```

4. The video will be downloaded, and the download progress will be hidden for a cleaner output.

## Notes
- The script saves videos with their original titles in the provided folder path. If the folder doesn't exist, it will be created automatically.
- If `yt-dlp` is not installed, the script will install it automatically during runtime.

## Example
Here's an example of how you might use the script:

```plaintext
enter the yt vid url: https://www.youtube.com/watch?v=dQw4w9WgXcQ
enter the folder path where the vid should be saved: C:\Users\Username\Downloads
Downloading the video!...
Downloaded successfully to C:\Users\Username\Downloads! 😃
