def ensure_ffmpeg():
    import os
    import shutil
    import urllib.request
    import zipfile
   

    # If already installed globally → use it
    if shutil.which("ffmpeg"):
        return None  # yt-dlp will use system ffmpeg

    print("⚠️ FFmpeg not found. Downloading automatically...\n")

    home = os.path.expanduser("~")
    ffmpeg_dir = os.path.join(home, ".octoload", "ffmpeg")
    os.makedirs(ffmpeg_dir, exist_ok=True)

    zip_path = os.path.join(ffmpeg_dir, "ffmpeg.zip")

    # Windows build (you can extend later)
    url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"

    # Download
    urllib.request.urlretrieve(url, zip_path)

    # Extract
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(ffmpeg_dir)

    # Find ffmpeg.exe
    ffmpeg_path = None
    for root, dirs, files in os.walk(ffmpeg_dir):
        if "ffmpeg.exe" in files:
            ffmpeg_path = root
            break

    if ffmpeg_path:
        print("✅ FFmpeg ready!\n")
        return ffmpeg_path
    else:
        print("❌ Failed to setup FFmpeg.")
        return None




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

    choice = input("Choice: ")

    if choice == "1":
        print("Video format-\n")
        print("[1]webm")
        print("[2]mp4\n")
        video_format_choice = input("Choice: ")
        

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