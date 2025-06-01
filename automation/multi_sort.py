import os
import shutil

# Automatically get path to your Desktop
desktop_path =r"C:\Users\gidea\Desktop"
text_folder = os.path.join(desktop_path, "TextFiles")

# Create the folder if it doesn't exist
os.makedirs(text_folder, exist_ok=True)

# Go through all files on Desktop
for file in os.listdir(desktop_path):
    if file.endswith(".txt"):
        source = os.path.join(desktop_path, file)
        destination = os.path.join(text_folder, file)
        shutil.copy2(source, destination)
        print(f"Moved: {file}")

print("All .txt files moved to TextFiles folder.")

