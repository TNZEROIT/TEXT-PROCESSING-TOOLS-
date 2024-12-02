import os
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def display_menu():
    os.system('clear')  # Use 'cls' on Windows
    logo = r"""
 ___ _____   __________ ____   ___    _   _ _____ ____   ___  
|_ _|_   _| |__  / ____|  _ \ / _ \  | | | | ____|  _ \ / _ \ 
 | |  | |     / /|  _| | |_) | | | | | |_| |  _| | |_) | | | |
 | |  | |    / /_| |___|  _ <| |_| | |  _  | |___|  _ <| |_| |
|___| |_|   /____|_____|_| \_\\___/  |_| |_|_____|_| \_\\___/ 
    """
    
    print(Fore.RED + logo)
    print(Fore.BLUE + "☠️☠️☠️WARNING: ANY USE IS AT YOUR OWN RISK!☠️☠️☠️")
    print(Fore.CYAN + "*" * 55)
    print(Fore.YELLOW + "* Author   : TnZeroIT")
    print(Fore.YELLOW + "* GitHub   : https://github.com/TNZEROIT")
    print(Fore.YELLOW + "* YouTube  : TNZEROIT")
    print(Fore.YELLOW + "* Telegram : https://t.me/TNZEROIT")
    print(Fore.YELLOW + "* Instagram: TNZEROIT")
    print(Fore.GREEN + "************* TEXT PROCESSING TOOLS ********************")

def add_to_each_line(input_file, output_file):
    print(Fore.YELLOW + "")
    addition = input("What word/number would you like to add?\n=")
    
    try:
        # Read the content of the input file
        with open(input_file, 'r') as file:
            lines = file.readlines()
        
        # Add user input to each line
        lines = [line.strip() + addition + '\n' for line in lines]
        
        # Write the changes to the output file
        with open(output_file, 'w') as file:
            file.writelines(lines)
        
        print(f"The word '{addition}' has been added to each line and saved in {output_file}.")
    except FileNotFoundError:
        print(f"The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Display the menu
display_menu()

# Call the function with the input file 'drokk.txt' and output file 'drokk1.txt'
add_to_each_line('yourteks.txt', 'ressultteks.txt')