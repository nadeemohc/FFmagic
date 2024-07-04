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
