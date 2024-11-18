import os
import yt_dlp as youtube_dl
from pyfiglet import figlet_format
import shutil

# Made By ASAAD SIDDIQUI
def print_ascii_art():
    ascii_art = figlet_format("PixelDev") 
    print(ascii_art)

# Function to download videos using yt-dlp (supports 2K/4K resolution if available)
def download_videos_from_channel(channel_url, base_folder="videos", resolution="2160"):
    # Create the base download folder if it doesn't exist
    if not os.path.exists(base_folder):
        os.makedirs(base_folder)

    # First, get the channel metadata to use the channel name for the folder
    ydl_opts_info = {'quiet': True, 'skip_download': True} 
    try:
        with youtube_dl.YoutubeDL(ydl_opts_info) as ydl:
            channel_info = ydl.extract_info(channel_url, download=False)
            channel_name = channel_info.get('uploader', 'Unknown_Channel')
            print(f"Downloading videos from channel: {channel_name}")
    except Exception as e:
        print(f"Error retrieving channel info: {str(e)}")
        return

    # Create the specific folder for the channel inside the base folder
    download_folder = os.path.join(base_folder, channel_name)
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Set download options
    ydl_opts = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best',
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Save files with title
        'merge_output_format': 'mp4',  # Merge video and audio to mp4
        'quiet': False,  # Show progress in the console
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([channel_url])  # Download all videos from the channel
    except Exception as e:
        print(f"Error downloading videos: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Print ASCII art before starting the script
    print_ascii_art()

    # Input section
    channel_url = input("👉Enter the YouTube channel URL: ")
    base_folder = input("👉Enter the base folder where you want to store videos (default is 'videos'): ") or "videos"
    resolution = input("👉Enter the resolution (default is 2160p, can be 1440p for 2K or any other): ") or "2160"

    # Start downloading videos
    download_videos_from_channel(channel_url, base_folder, resolution)
