import os
import subprocess
import sys
import time

def install_requirements():
#---------basically installs the required libraries using pip automatically.----------
    try:
        import yt_dlp
    except ImportError:
        print("yt-dlp is not installed. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
        print("yt-dlp installed successfully.")

#----------function for downloading video----------
def download_video(link, output_path):
#----------downloads the video from the given link and saves it in mp4 format----------
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    ydl_opts = {
        'format': 'mp4',  
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # saves with video title as filename
        'quiet': True,  # makes it so that the download processes are not shown to user to make the output cleaner
    }
    try:
        import yt_dlp
        print('Downloading the video nigger!...')
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print(f"Downloaded successfully to {output_path} nigger!😃")

        # makes it so that the time of creation is set as the time its executed
        # get the downloaded file path
        downloaded_file = os.path.join(output_path, f"{ydl.prepare_filename(ydl.extract_info(link))}")

        # set the current time as the modified time for the downloaded file
        current_time = time.time()  # gets the current time
        os.utime(downloaded_file, (current_time, current_time))  # updates the access and modified time
        
    except Exception as e:
        print(f"An error occurred nigger!: {e}")

def main():
    install_requirements()

    link = input("enter the yt vid url nigger!: ")
    output_path = input("enter the folder path where the vid should be saved nigger!: ")

    download_video(link, output_path)

main()
