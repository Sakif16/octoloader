import yt_dlp
import os
from pyfiglet import Figlet
from colorama import Fore, Style, init

# Initialized colorama
init()

# ===== Banner =====
f = Figlet(font='slant')
print(Fore.CYAN + f.renderText('YTMP3') + Style.RESET_ALL)

print(Fore.GREEN + "Welcome to Media Downloader" + Style.RESET_ALL)


#Dwonloaded files destination folder
download_folder = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop", "downloaded mp3s")

#choice for audio or video
choice = input("Download Video [1] or Audio [2]?: ")

url = input("Paste YouTube video link: ")


#Video download
if choice == '1':
    ydl_opts ={
        "format":"bestvideo+bestaudio/best",
        "outtmpl": os.path.join(download_folder, '%(title)s.%(ext)s')
    }

#Audio download
elif choice == "2":
    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}
else: print("Invalid choice")


with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])