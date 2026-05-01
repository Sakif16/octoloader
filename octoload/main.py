import yt_dlp
import os
from pyfiglet import Figlet
from colorama import Fore, Style, init


def main():
    # Initialize colorama
    init()

    # ===== Banner =====
    f = Figlet(font='slant')
    print(Fore.CYAN + f.renderText('OctoLoad') + Style.RESET_ALL)
    print(Fore.GREEN + "Welcome to OctoLoad\n" + Style.RESET_ALL)

    # Download folder (system Downloads)
    download_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    # Choice for audio or video
    print("Download-\n")
    print("[1] Video")
    print("[2] Audio\n")

    choice = input("Choice: ")

    if choice == "1":
        print("Video format-\n")
        print("[1] webm")
        print("[2] mp4\n")
        video_format_choice = input("Choice: ")

    url = input("Paste YouTube video link: ")

    # ================= VIDEO =================
    if choice == '1':
        if video_format_choice == "1":
            ydl_opts = {
                "format": "bestvideo+bestaudio/best",
                "outtmpl": os.path.join(download_folder, '%(title)s.%(ext)s')
            }

        elif video_format_choice == "2":
            ydl_opts = {
                "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
                "outtmpl": os.path.join(download_folder, '%(title)s.%(ext)s')
            }

        else:
            print("Invalid choice")
            return

    # ================= AUDIO =================
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

    else:
        print("Invalid choice")
        return

    # Download
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    main()