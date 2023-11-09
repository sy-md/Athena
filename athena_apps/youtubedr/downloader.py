import os,json

links = "/data/data/com.termux/files/home/Athena/athena_apps/Youtube_api/output/cleaned.json"
dst = "/data/data/com.termux/files/home/Athena/athena_music"

with open(links, "r") as mylks:
    data = json.load(mylks)
    # url: +__++_+__+
    print(data[0]["url"])


    for k in data:
        url = k["url"]
        os.system("youtubedr download 'https://youtu.be/{}' ".format(url))


