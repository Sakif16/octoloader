import urllib.request
import os

def ensure_ffmpeg():
    ffmpeg_path = os.path.join(os.getcwd(), "ffmpeg", "bin", "ffmpeg.exe")

    if os.path.exists(ffmpeg_path):
        return ffmpeg_path

    print("⚠️ FFmpeg not found. Downloading automatically...\n")

    url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
    zip_path = "ffmpeg.zip"

    # 🔥 Fix: remove broken partial file
    if os.path.exists(zip_path):
        os.remove(zip_path)

    try:
        urllib.request.urlretrieve(url, zip_path)
    except Exception as e:
        print("❌ Download failed. Please check your internet and try again.")
        raise e

    print("✅ Download complete. Extracting...")

    import zipfile
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall("ffmpeg")

    os.remove(zip_path)

    return ffmpeg_path


def main():

    import yt_dlp
    import os
    from pyfiglet import Figlet
    from colorama import Fore, Style, init

    # Initialized colorama
    init()

    ffmpeg_location = ensure_ffmpeg()

    # ===== Banner =====
    f = Figlet(font='slant')
    print(Fore.CYAN + f.renderText('OctoLoad') + Style.RESET_ALL)

    print(Fore.GREEN + "Welcome to Octoloader\n" + Style.RESET_ALL)


    #Dwonloaded files destination folder
    download_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    #choice for audio or video
    print("Download-\n")
    print("[1] Video")
    print("[2] Audio\n")

    choice = input("Choice: \n")

    if choice == "1":
        print("Video format-\n")
        print("[1]webm")
        print("[2]mp4\n")
        video_format_choice = input("Choice: \n")
        

    url = input("Paste YouTube video link: ")


    #Video download
    if choice == '1':
        if video_format_choice == "1":
            ydl_opts ={
                "format":"bestvideo+bestaudio/best",
                "outtmpl": os.path.join(download_folder, '%(title)s.%(ext)s'),
                "ffmpeg_location": ffmpeg_location
            }
        elif video_format_choice == "2":
            ydl_opts ={
                "format":"bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
                "outtmpl": os.path.join(download_folder, '%(title)s.%(ext)s'),
                "ffmpeg_location": ffmpeg_location
            }
        else: print("Invalid choice")


    #Audio download
    elif choice == "2":
        ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        "ffmpeg_location": ffmpeg_location,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
    else: print("Invalid choice")


    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])








if __name__ == "__main__":
    main()