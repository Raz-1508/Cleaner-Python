import os
import shutil
download_folder = os.path.expanduser("~/Downloads")
folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", "jfif", ".webp"],
    "Documentes": [".pdf", ".docx", ".txt", ".xlsx", ".pptx",],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],}
for filename in os.listdir(download_folder):
    file_path = os.path.join(download_folder, filename)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)
        file_extension = file_extension[1].lower()
        for folder_name, extensions in folders.items():
            if file_extension in extensions:
                destination_folder = os.path.join(download_folder, folder_name)
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder, exist_ok=True)
                shutil.move(file_path, destination_folder)
                break