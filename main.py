import os
import shutil


directory = "path/to/your/directory"


file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx'],
    'Spreadsheets': ['.xlsx', '.xls', '.csv'],
    'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
}

for folder in file_types:
    os.makedirs(os.path.join(directory, folder), exist_ok=True)


others_folder = os.path.join(directory, 'Others')
os.makedirs(others_folder, exist_ok=True)


def move_file(filename, file_path):
    for folder, extensions in file_types.items():
        if filename.lower().endswith(tuple(extensions)):  
            shutil.move(file_path, os.path.join(directory, folder, filename))
            return
    
    shutil.move(file_path, os.path.join(others_folder, filename))


for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        move_file(filename, file_path)

print(f"Files in '{directory}' have been organized successfully.")
