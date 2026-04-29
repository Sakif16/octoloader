#OctoLoad

## 🧩 Intro
A simple command-line tool to download YouTube videos or convert them into high-quality MP3 files.

---

## 📖 Description
OctoLoad is a lightweight Python-based CLI tool designed for quick and efficient media downloading from YouTube. It provides an interactive terminal experience where users can choose between downloading videos or extracting audio.

### 🔹 What you can do:
- Download YouTube videos in high quality  
- Convert videos into **320kbps MP3 audio**  
- Choose between video formats (MP4 / WEBM)  
- Automatically merge audio and video streams  
- Use a clean and user-friendly CLI interface  

---

## 🛠️ Tech Stack
- Python  
- yt-dlp  
- FFmpeg  
- pyfiglet  
- colorama  

---

## ⚙️ Installation & Usage

### 🔹 Step 1: Clone the repository
```bash
git clone https://github.com/Sakif16/octoloader.git
```
### 🔹 Step 2: Enter directory
```bash
cd octoloader
```
### 🔹 Step 3: Install the dependencies
```bash
pip install .
```
### 🔹 Step 4: Install ffmpeg
- For Windows, Download FFmpeg from: https://ffmpeg.org/download.html
- Extract the file
- add the bin folder to your system PATH

### 🔹 Step 5: Run the tool
```bash
python -m octoload.main 
```
## 🤝 Contributions
Contributions are welcome!

### You can contribute by:
- Reporting bugs or issues  
- Suggesting new features or improvements  
- Refactoring code for better performance or readability  
- Improving CLI experience and user interaction  
- Enhancing documentation  

### How to contribute:
### 1) Fork the repository
### 2) Clone your fork
```bash
git clone https://github.com/YOUR_USERNAME/octoloader.git
```
### 3) Create a new branch
```bash
git checkout -b feature-name
```
### 4) Make your changes and commit
```bash
git commit -m "Add: your feature description"
```
### 5) Push to your fork
```bash
git push origin feature-name
```
### 6) Open a Pull Request on GitHub

## ⚠️ Known Issues
- FFmpeg auto-download currently supports Windows only  
- First-time execution may be slow due to FFmpeg download  
- Some YouTube formats may not be available without a JavaScript runtime  
- No progress indicator for FFmpeg download  
- CLI error messages can be improved for better clarity  
- PATH-related issues may prevent the `octoload` command from running on some systems  
- Limited testing on Linux and macOS environments  

## 🚀 Future Development
- Cross-platform FFmpeg support (Linux & macOS)  
- Add download progress bars (media + FFmpeg)  
- Allow users to select video/audio quality  
- Support for playlists and batch downloads  
- Improve error handling and user-friendly prompts  
- Add configuration options (custom download directory, defaults, etc.)  
- Publish to PyPI for one-command installation (`pip install octoload`)  
- Optimize performance and reduce initial setup time  
- Add update checker for new versions  
