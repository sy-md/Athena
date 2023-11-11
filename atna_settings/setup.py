import os

my_user = "sy"
comp_home = f"home/{my_user}"
phone = f"data/data/com.termux/files"

pc = {

   "backend" : {
      "etc" : "/etc/",
      "docs" : "/usr/share/doc/"
   },

   "home" : {
      "zsh" :f"/{comp_home}/.zshrc",
      "ssh" :f"/{comp_home}/.ssh",
      "config" :f"/{comp_home}/.config",
      "oh-my-zsh" :f"/{comp_home}/.oh-my-zsh"
   },

   "tomorrowland": {
      "settings" : f"/{comp_home}/Athena/atna_settings",
      "go" : f"/{comp_home}/Athena/atna_go",
      "screen" : f"/{comp_home}/Athena/atna_screen",
      "apps" : f"/{comp_home}/Athena/atna_settings",
      "portfoilio" : f"/{comp_home}/Athena/atna_portfoilio",

   },

}
phone = {

   "backend" : {
      "etc" : f"{phone}/usr/etc/",
      "docs" : f"{phone}/usr/share/doc/"
   },

   "home" : {
      "zsh" :f"/{phone}/home/.zshrc",
      "ssh" :f"/{phone}/home/.ssh",
      "config" :f"/{phone}/home/.config",
      "oh-my-zsh" :f"/{phone}/home/.oh-my-zsh"
   },

   "tomorrowland": {
      "settings" : f"/{phone}/home/Athena/atna_settings",
      "go" : f"/{phone}/home/Athena/atna_go",
      "screen" : f"/{phone}/home/Athena/atna_screen",
      "apps" : f"/{phone}/home/Athena/atna_settings",
      "portfoilio" : f"/{phone}/home/Athena/atna_portfoilio",

   },
}
class pc_cli:

   def get_list(key):
      """
         search the pc backend for
         the paths and stores them
      """
      make_list = []
      for x in pc[key].values():
         make_list.append(x)
      return make_list

   def check_a_system(trg):
      """
         check one thing like pc.backend{...}
         reuturn [of paths] and check folders
         for existance and create them if not

      """
      search = trg
      data = pc_cli.get_list(search) # --> [keys of the pc {search}]
      for x in data:
         exist = os.path.exists(x)
         if exist == False :
            print(f"it is {exist} that path {x} exists fixing the issues")
            os.system(f'touch {x}') # create a function
         else:
            print(f"it is {exist} that path {x} exists")

   def get_system():
      """
         used to scan the whole Tomorowland

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

if __name__ == "__main__":
   pc_cli.check_a_system("home")
