import os
import zipfile
from datetime import datetime


def create_backup(source_dir, backup_dir):
    # Create the backup file name with the current date
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    zip_filename = f"backup_{date_str}.zip"
    zip_filepath = os.path.join(backup_dir, zip_filename)
    
    # Create the zip file
    with zipfile.ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
        # Walk through the source directory and add files to the zip file
        for foldername, subfolders, filenames in os.walk(source_dir):
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                # Add file to the zip with relative path
                backup_zip.write(filepath, os.path.relpath(filepath, source_dir))
    
    print(f"Backup created: {zip_filepath}")
    manage_backups(backup_dir)

def manage_backups(backup_dir, max_backups=10):
    # List all files in the backup directory that start with 'backup_'
    backup_files = [f for f in os.listdir(backup_dir) if f.startswith("backup_") and f.endswith(".zip")]
    
    # Sort the backup files by creation time
    backup_files.sort(key=lambda f: os.path.getctime(os.path.join(backup_dir, f)))
    
    # If there are more backups than max_backups, delete the oldest
    while len(backup_files) > max_backups:
        oldest_backup = backup_files.pop(0)
        os.remove(os.path.join(backup_dir, oldest_backup))
        print(f"Deleted old backup: {oldest_backup}")
