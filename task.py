import os
import time


directory = "path/to/cleanup/directory"


max_age = 30 * 24 * 60 * 60  


current_time = time.time()


for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    
    if os.path.isfile(file_path):
        
        file_age = current_time - os.path.getmtime(file_path)

        
        if file_age > max_age:
            print(f"Deleting {file_path}...")
            os.remove(file_path)

print(f"Cleanup of {directory} complete.")
