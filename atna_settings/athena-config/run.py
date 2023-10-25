import os

#first install python 
#secound install git 
comfirm = input("are you in your Home directory with your dotfiles: y/n ")
if comfirm == "y":

#	os.system("rm -r Athena && yes | cp -rf .config/ .oh-my-zsh/ .vim/ .zshrc ../")
#	os.system("git clone 'https://github.com/sy-md/Athena.git'")
	os.system("git clone 'https://github.com/sy-md/ohmyzsh.git' ")
#	os.system("git clone 'https://github.com/sy-md/nvim.git' ")
#	os.system("mv nvim ../ ")
#	os.sytem("mv ohmyzsh .ohmyzsh && mv .ohmyzsh ../")
	
if comfirm  == "n":
	exit()





	






