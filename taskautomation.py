import os
import shutil

def organize_files(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    files = os.listdir(source_dir)

    for file in files:
        source_path = os.path.join(source_dir, file)
        if os.path.isfile(source_path):
            _, extension = os.path.splitext(file)
            destination_path = os.path.join(destination_dir, extension[1:].lower())

            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
            
            shutil.move(source_path, destination_path)

    print("Files organized successfully!")

if __name__ == "__main__":
    source_directory = input("Enter the source directory path: ")
    destination_directory = input("Enter the destination directory path: ")

    organize_files(source_directory, destination_directory)