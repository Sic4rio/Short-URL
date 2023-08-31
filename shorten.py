import random
import string
import requests
import os
import getpass
from pyshorteners import Shortener

# Install the pyshorteners library
os.system("pip install pyshorteners")
os.system("clear")

def obfuscate(url, times=100):
    B = times
    A = url
    s = Shortener()

    obfuscated_parts = []
    for _ in range(B):
        obfuscated_part = ''.join(
            random.choice(string.ascii_letters + string.digits) for _ in range(len(url))
        )
        obfuscated_parts.append(obfuscated_part)

    obfuscated_url = '/'.join(obfuscated_parts) + url
    shortened_url = s.tinyurl.short(obfuscated_url)  # Shorten the obfuscated URL

    return shortened_url


def clear():
    os.system("clear" if os.name != "nt" else "cls")

def credit():
    print(
        "\x1b[31;1mh\x1b[32;1mt\x1b[33;1mt\x1b[34;1mp\x1b[35;1ms\x1b[36;1m:\x1b[32;1m/\x1b[33;1m/\x1b[34;1mg\x1b[35;1mi\x1b[36;1mt\x1b[32;1mh\x1b[33;1mu\x1b[34;1mb\x1b[35;1m.\x1b[36;1mc\x1b[32;1mo\x1b[33;1mm\x1b[34;1m/\x1b[35;1mS\x1b[36;1mi\x1b[32;1mc\x1b[33;1m4\x1b[34;1mr\x1b[35;1mi\x1b[36;1mo\x1b[32;1m/\x1b[0m\n\n"
    )


clear()
os.system("URL Obfuscator" if os.name == "nt" else "")
credit()
while True:
    URL = input("Enter URL: ")
    try:
        r = requests.get(URL)
        clear()
        break
    except Exception:
        print("Unable to reach URL!\n")
credit()
print("Processing...")
with open("obf.txt", "w") as file:
    file.write(obfuscate(URL))
clear()
credit()
print(f'Saved URL in "obf.txt"\n')
if os.name == "nt":
    os.system(f"notepad.exe obf.txt")
getpass.getpass("(Press enter to exit)")
