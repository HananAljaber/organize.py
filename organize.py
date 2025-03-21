import os
import shutil
import sys

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"},
    "Archives": {".zip", ".rar", ".tar", ".gz"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov"},
    "Audio": {".mp3", ".wav", ".aac"},
    "Others": set()
}

def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        print(f"❌ الخطأ: '{folder_path}' ليس مجلداً صحيحاً.")
        return

    for name in os.listdir(folder_path):
        src = os.path.join(folder_path, name)
        if os.path.isfile(src):
            ext = os.path.splitext(name)[1].lower()
            dest = next((cat for cat, exts in CATEGORIES.items() if ext in exts), "Others")
            dest_dir = os.path.join(folder_path, dest)
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(src, os.path.join(dest_dir, name))
            print(f"✔ نقل '{name}' → {dest}/")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\nالاستخدام:")
        print("  python organize.py <مسار المجلد>")
        print("\nمثال:")
        print("  python organize.py \"C:\\Users\\PC1\\Downloads\"\n")
    else:
        organize_folder(sys.argv[1])
