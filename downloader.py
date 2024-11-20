import os
import yt_dlp as youtube_dl
from pyfiglet import figlet_format
import shutil


def print_ascii_art():
    ascii_art = figlet_format("PixelDev") 
    print(ascii_art)


def download_videos_from_channel(channel_url, base_folder="videos", resolution="2160"):
    if not os.path.exists(base_folder):
        os.makedirs(base_folder)

    ydl_opts_info = {'quiet': True, 'skip_download': True} 
    try:
        with youtube_dl.YoutubeDL(ydl_opts_info) as ydl:
            channel_info = ydl.extract_info(channel_url, download=False)
            channel_name = channel_info.get('uploader', 'Unknown_Channel')
            print(f"Downloading videos from channel: {channel_name}")
    except Exception as e:
        print(f"Error retrieving channel info: {str(e)}")
        return

    download_folder = os.path.join(base_folder, channel_name)
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    ydl_opts = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best',
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'quiet': False,
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([channel_url])  
    except Exception as e:
        print(f"Error downloading videos: {str(e)}")


if __name__ == "__main__":
    
    print_ascii_art()

    channel_url = input("👉Enter the YouTube channel URL: ")
    base_folder = input("👉Enter the base folder where you want to store videos (default is 'videos'): ") or "videos"
    resolution = input("👉Enter the resolution (default is 2160p, can be 1440p for 2K or any other): ") or "2160"


    download_videos_from_channel(channel_url, base_folder, resolution)
