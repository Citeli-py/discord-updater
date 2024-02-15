import requests, os

r = requests.get("https://discord.com/api/download/stable?platform=linux&format=deb")

with open("discord.deb", "wb") as file:
    for chunk in r.iter_content(chunk_size=4096):
        file.write(chunk)

