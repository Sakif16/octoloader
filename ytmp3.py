import yt_dlp
import os

#Dwonloaded files destination folder
download_folder = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop", "downloaded mp3s")

url = input("Paste YouTube video link: ")

#conversion
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])