import os,random
bck = "/data/data/com.termux/files/home/storage/pictures/new_pics/.ass"
frt = "/data/data/com.termux/files/home/storage/pictures/new_pics/.tits"
dst = "/data/data/com.termux/files/home/storage/shared/mynudes"
chs_bck = random.choice(os.listdir(bck))
chs_frt = random.choice(os.listdir(frt))


def send_to():
   ass = ("cp -r {}/{} {}/my_baby_ass.png".format(bck,chs_bck,dst))
   tits = ("cp -r {}/{}  {}/titties.png".format(frt,chs_frt,dst))
   os.system("{};{}".format(ass,tits))
send_to()

#os.system("cp -r {}/{} {}".format(bck,chs,dst))
#print("{} \n {}".format(chs_bck,chs_frt))
"""
cooy image randommly from the libaray
send to temp loc
then erase it repeat

"""
