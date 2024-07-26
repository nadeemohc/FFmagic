import os
import subprocess
import time
from rich import print
from rich.prompt import Prompt
from music_conversion import remove_duplicates  # Uncomment if needed

def jpg_to_png(directory, input_extension, output_format):
    os.chdir(directory)
    for filename in os.listdir(directory):
        if filename.endswith(input_extension):
            output_filename = os.path.splitext(filename)[0] + output_format
            command = ['ffmpeg', '-i', filename, output_filename]
            subprocess.run(command)
            print(f'[bold green]Converted {filename} to {output_filename}[/]')
    print('[bold white]PNG conversion completed[/]')

def jpeg_to_png(directory, input_extension, output_format):
    os.chdir(directory)
    for filename in os.listdir(directory):
        if filename.endswith(input_extension):
            output_filename = os.path.splitext(filename)[0] + output_format
            command = ['ffmpeg', '-i', filename, output_filename]
            subprocess.run(command)
            print(f'[bold green]Converted {filename} to {output_filename}[/]')
    print('[bold white]PNG conversion completed[/]')

def main():
    print('[bold green]Welcome to the[/][bold red][underline] Image Converter[/][/]')
    directory = Prompt.ask('[bold yellow]Enter the path of your[/][bold red][underline] Image Folder[/][/]')
    if not os.path.isdir(directory):
        print('[bold green]Invalid directory path.[/]')
        time.sleep(2)
        print('[bold red]Exiting...[/]')
        return
    
    print("[bold green]Select conversion format:[/]")
    print("[bold white]1. [/][bold green][underline].jpg to .png[/][/]")
    print("[bold white]2. [/][bold green][underline].jpeg to .png[/][/]")
    choice = Prompt.ask("[bold yellow]Enter your choice: [/]").strip()

    if choice == '1':
        input_extension = '.jpg'
        output_format = '.png'
        jpg_to_png(directory, input_extension, output_format)
    elif choice == '2':
        input_extension = '.jpeg'
        output_format = '.png'
        jpeg_to_png(directory, input_extension, output_format)    
    else:
        print('[bold green]Invalid choice.[/]')
        time.sleep(2)
        print('[bold red]Exiting...[/]')
        return

    remove_duplicates(directory, input_extension)  # Uncomment if needed

if __name__ == "__main__":
    main()
