import subprocess
playlist=[]
with open("playlist.txt","r") as file:
    f=file.readlines()
    for line in f:
        playlist.append(line.strip())
for song in playlist:
    subprocess.run(["python", "download.py", song])
