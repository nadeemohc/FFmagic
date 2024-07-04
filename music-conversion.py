import os
import subprocess

def convert_files(directory, input_extension, output_format, flac_compression_level):
    os.chdir(directory)
    for filename in os.listdir(directory):
        if filename.endswith(input_extension):
            output_filename = os.path.splitext(filename)[0] + "." + output_format
            command = ['ffmpeg', '-i', filename, '-compression_level', flac_compression_level, output_filename]
            subprocess.run(command)
            print(f'Converted {filename} to {output_filename}')
    print("Conversion Completed")

def remove_duplicates(directory, input_extension):
    query = input('Remove all the duplicate files? (y/n): ').strip().lower()
    if query == 'y':
        for filename in os.listdir(directory):
            if filename.endswith(input_extension):
                file_path = os.path.join(directory, filename)
                os.remove(file_path)
                print(f"Removed {file_path}")
    else:
        print("No files were removed.")

def main():
    print('Welcome to Music Converter')
    
    directory = input("Enter the path of your Music Folder: ").strip()
    if not os.path.isdir(directory):
        print("Invalid directory path. Exiting...")
        return
    
    print("Select conversion format:")
    print("1. .weba to .flac")
    choice = input("Enter your choice: ").strip()
    
    if choice == '1':
        input_extension = '.weba'
        output_format = 'flac'
        flac_compression_level = '5'
    else:
        print("Invalid choice. Exiting...")
        return
    
    convert_files(directory, input_extension, output_format, flac_compression_level)
    remove_duplicates(directory, input_extension)

if __name__ == "__main__":
    main()
import os
import subprocess

directory = '/home/kenpachi/Music/spotube/'
os.chdir (directory)
output_format = 'flac'
flac_compression_level = '5'

for filename in os.listdir(directory):
    if filename.endswith(".weba"):
        output_filename = os.path.splitext(filename) [0] + "." + output_format
        if output_format == 'flac':
            command = ['ffmpeg', '-i', filename,
                       '-compression_level', flac_compression_level,
                       output_filename
                       ]
            subprocess.run(command)

print("Conversion Completed")

query = input('Remove all the duplicate files?')
if query == 'y':
    for filename in os.listdir(directory):
        if filename.endswith(".weba"):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
print(f"Removed {file_path}")
