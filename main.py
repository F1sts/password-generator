from rich.console import Console
from datetime import datetime
import pyperclip
import locale
import string
import random
import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def ask_until_necessary(msg: str, choice_list: list[str] = []):
    while True:
        console.print(msg, end="")
        choice = input().lower()
        
        if (len(choice_list) == 0 and choice.isdigit() and int(choice) <= 128) or (choice in choice_list):
            return choice
        else:
            console.print(f"❗️ [bold #f51818]| Please pick one of them: {choice_list}" if len(choice_list) > 0 else "❗️ [bold #f51818]| Please enter a valid number.")
            continue

def generate_pass(uppercase: bool, digits: bool, symbols: bool, length: int):
    char_pool = string.ascii_lowercase
    
    if uppercase: char_pool += string.ascii_uppercase
    if digits: char_pool += string.digits
    if symbols: char_pool += string.punctuation
    
    return "".join(random.choices(char_pool, k=length))

if __name__ == "__main__":
    console = Console()
    locale.setlocale(locale.LC_TIME, "")
    
    while True:
        clear_console()
        console.print(fr"""[bold #0ea5e9]
                      ______  _       _        
                      |  ___|(_)     | |       
                      | |_    _  ___ | |_  ___ 
                      |  _|  | |/ __|| __|/ __|
                      | |    | |\__ \| |_ \__ \
                      \_|    |_||___/ \__||___/
        [reset][bold #f0b616]                 
           ____                                            _     
          |  _ \  __ _  ___  ___ __      __ ___   _ __  __| |    
          | |_) |/ _` |/ __|/ __|\ \ /\ / // _ \ | '__|/ _` |    
          |  __/| (_| |\__ \\__ \ \ V  V /| (_) || |  | (_| |    
          |_|    \__,_||___/|___/  \_/\_/  \___/ |_|   \__,_|    
          ____                                 _               
         / ___|  ___  _ __    ___  _ __  __ _ | |_  ___   _ __ 
        | |  _  / _ \| '_ \  / _ \| '__|/ _` || __|/ _ \ | '__|
        | |_| ||  __/| | | ||  __/| |  | (_| || |_| (_) || |   
         \____| \___||_| |_| \___||_|   \__,_| \__|\___/ |_|   
        
                    Thanks for using my program 🤗
        """)
        contain_uppercase = ask_until_necessary("❓ [#dbde16]| Should your password contain uppercase letters?: ", ["yes", "no"])
        contain_numbers = ask_until_necessary("❓ [#dbde16]| Should your password contain numbers?: ", ["yes", "no"])
        contain_symbols = ask_until_necessary("❓ [#dbde16]| Should your password contain symbols?: ", ["yes", "no"])
        pass_length = ask_until_necessary("❓ [#dbde16]| How many characters should your password have?: ")
        
        generated_pass = generate_pass(True if contain_uppercase == "yes" else False,
                                       True if contain_numbers == "yes" else False,
                                       True if contain_symbols == "yes" else False,
                                       int(pass_length))
        pyperclip.copy(generated_pass)
        with open("./password_history.txt", "a", encoding="utf-8") as file:
            file.write(f"[{datetime.now().strftime("%A, %d %B %Y - %H:%M (%I:%M %p)")}] → {generated_pass}\n")
        
        console.print("\n✔️  [bold #1cd916]| Your password generated and saved successfully!")
        console.print(f"📢 [bold #1cd916]| The password will not be displayed for security purposes, but it has been copied to your clipboard!")
        console.print("❗️ [bold #f51818]| Don't forget to clear password_history.txt!")
        console.print("🤫 [bold #f0b616]| Keep it safe and secure!", end="\n\n")
        
        decision = ask_until_necessary("❓ [#dbde16]| Would you like to generate another password?: ", ["yes", "no"])
        if decision == "no":
            clear_console()
            break