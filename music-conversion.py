import os
import subprocess

def convert_files_to_flac(directory, input_extension, output_format, flac_compression_level):
    os.chdir(directory)
    for filename in os.listdir(directory):
        if filename.endswith(input_extension):
            output_filename = os.path.splitext(filename)[0] + "." + output_format
            command = ['ffmpeg', '-i', filename, '-compression_level', flac_compression_level, output_filename]
            subprocess.run(command)
            print(f'Converted {filename} to {output_filename}')
    print("FLAC Conversion Completed")

def convert_files_to_mp3(directory, input_extension, output_format, mp3_bitrate):
    os.chdir(directory)
    for filename in os.listdir(directory):
        if filename.endswith(input_extension):
            output_filename = os.path.splitext(filename)[0] + "." + output_format
            command = ['ffmpeg', '-i', filename, '-b:a', mp3_bitrate, output_filename]
            subprocess.run(command)
            print(f'Converted {filename} to {output_filename}')
    print('MP3 Conversion Completed')

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
    print("2. .weba to .mp3")
    choice = input("Enter your choice: ").strip()
    
    if choice == '1':
        input_extension = '.weba'
        output_format = 'flac'
        flac_compression_level = '5'
        convert_files_to_flac(directory, input_extension, output_format, flac_compression_level)
    elif choice == '2':
        input_extension = '.weba'
        output_format = 'mp3'
        mp3_bitrate = '320k'
        convert_files_to_mp3(directory, input_extension, output_format, mp3_bitrate)
    else:
        print("Invalid choice. Exiting...")
        return
    
    remove_duplicates(directory, input_extension)

if __name__ == "__main__":
    main()
