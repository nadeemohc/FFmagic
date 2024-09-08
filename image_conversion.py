import os
import subprocess
import time
from rich import print
from rich.prompt import Prompt
from music_conversion import remove_duplicates  # Uncomment if needed

def convert_images(directory, input_extension, output_format):
    os.chdir(directory)
    for filename in os.listdir(directory):
        if filename.endswith(input_extension):
            output_filename = os.path.splitext(filename)[0] + output_format
            command = ['ffmpeg', '-i', filename, output_filename]
            subprocess.run(command)
            print(f'[bold green]Converted {filename} to {output_filename}[/]')
    print(f'[bold white]{output_format.upper()} conversion completed[/]')

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
    elif choice == '2':
        input_extension = '.jpeg'
        output_format = '.png'
    else:
        print('[bold green]Invalid choice.[/]')
        time.sleep(2)
        print('[bold red]Exiting...[/]')
        return

    convert_images(directory, input_extension, output_format)

    # Uncomment the following line if you need to remove duplicates
    remove_duplicates(directory, input_extension)

if __name__ == "__main__":
    main()
