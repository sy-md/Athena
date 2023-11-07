import os,json

links = "my_youtube.json"
dst = "/data/data/com.termux/files/home/Athena/athena_music"

with open(links, "r") as mylks:
    data = json.load(mylks)

    for k in data:
       os.system(
            "youtube-dl 'https://youtu.be/{}' {} ".format(k,dst)
       )


