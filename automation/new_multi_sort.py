import os
import shutil

# Hardcoded path to your Desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Define the target folder
text_folder = os.path.join(desktop_path, "TextFiles")

# Check if the folder exists
if not os.path.exists(text_folder):
    os.makedirs(text_folder)
    print("📁 'TextFiles' folder did not exist. It has been created.")
else:
    print("📁 'TextFiles' folder already exists.")

# Move all .txt files from Desktop to TextFiles
moved_any = False  # flag to track if anything was moved

for file in os.listdir(desktop_path):
    if file.endswith(".txt"):
        source = os.path.join(desktop_path, file)
        destination = os.path.join(text_folder, file)
        shutil.move(source, destination)
        print(f"Moved: {file}")
        moved_any = True

if not moved_any:
    print("ℹ️ No .txt files were found on the Desktop.")
else:
    print("✅ All .txt files have been moved to the TextFiles folder.")
