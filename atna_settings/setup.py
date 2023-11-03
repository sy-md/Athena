import os

my_user = "sy"
comp_home = f"home/{my_user}"

pc = {

   "backend" : {
      "etc" : "/etc/",
      "docs" : "/usr/share/doc/",
   },
   "tomorrowland": {
      "zsh" :f"/{comp_home}/.zsh",
      "ssh" :f"/{comp_home}/.ssh",
      "config" :f"/{comp_home}/.config",
      "oh-my-zsh" :f"/{comp_home}/.oh-my-zsh",

   },

}

def main():
   # ask the user for the whaoami
   print("starting")

def get_list(key):
   """
   search the pc backend for
   the paths and stores them
   """
   make_list = []
   for x in pc[key].values():
      make_list.append(x)
   return make_list

def check_a_system():
   """
      check one thing like pc.backend{...}
      reuturn [of paths] and cxheck folers
   """
   search = "tomorrowland"
   data = get_list(search) # --> [keys of the pc {search}]
   for x in data:
      exist = os.path.exists(x)
      print(f"it is {exist} that path {x} exists")

def get_system():
   """
      used to scan the whole tomorrowland system

   """
   make_list = []
   for key in pc:
      for paths in pc[key].values():
         make_list.append(paths)
   return make_list

def system_check():
   """
      check system wide pc
      theis will check pc[key] for x in its cvalues

   """
   data = get_system()
   for x in data:
      exist = os.path.exists(x)
      print(f"it is {exist} that path {x} exists")


#check_a_system()
system_check()
#os.path.exists(path) dir
#os.path.isfile(path) file
