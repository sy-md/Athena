import os,json

links = "../Youtube_api/output/cleaned.json"
dst = "."

with open(links, "r") as mylks:
    data = json.load(mylks)
    # url: +__++_+__+
    print(data[0]["url"])


    for k in data:
        url = k["url"]
        os.system("youtubedr download 'https://youtu.be/{}' ".format(url))


