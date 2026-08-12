# 📁 File Organizer

A 🐍 Python automation tool that automatically organizes files into categorized folders based on their file extensions.

## ✨ Features

- 🖼️ Organizes images into an `Images` folder
- 🎬 Organizes videos into a `Videos` folder
- 📄 Organizes documents into a `Documents` folder
- 💻 Organizes code files into a `Code` folder
- 📦 Moves unsupported file types into an `Others` folder
- 🔄 Handles duplicate filenames automatically
- ✅ Validates the folder path before organizing
- 🛠️ Uses `pathlib` for file and folder operations
- 🚚 Uses `shutil` to move files
- 💬 Simple command-line interface

## 🧰 Technologies

- 🐍 Python
- 📂 pathlib
- 🚚 shutil

## 🚀 How to Run

1. 📥 Clone or download this repository.
2. Open the project folder.
3. Run:

```bash
python main.py

## Example

========================================
             FILE ORGANIZER
========================================

Enter a folder path: C:\Users\Example\Downloads

Moved photo.jpg to Images
Moved video.mp4 to Videos
Moved report.pdf to Documents
Moved script.py to Code
Moved unknown.xyz to Others

Files organized successfully!

Do you want to organize another folder? (yes/no):

🧠 What I Learned

This project helped me practice:

🗂️ File and folder handling
🔄 Loops and conditional statements
🧩 Functions
🐍 Python dictionaries
🛡️ Input validation
📂 pathlib
🚚 shutil
🔍 File extensions
♻️ Handling duplicate filenames
🤖 Basic automation
👨‍💻 Author

Mohammad Rohan

Built as part of my journey learning 🐍 Python and working toward becoming an 🤖 AI Engineer.
