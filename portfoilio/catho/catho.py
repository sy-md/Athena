from InquirerPy import inquirer
from colorama import Back,Fore,Style,init
import json,os,calendar
from pprint import pprint

db = "/data/data/com.termux/files/home/Athena/temp_apps/catho.json"
class my_catho: 

     def start():

        with open(db, "r") as writing:
            data = json.load(writing)

            # prints with pretty-print
            pprint(data)

            options = inquirer.select(
                            message="choose a selection ",
                            choices=["reset","-edit-","add","-remove-"]).execute()      
            if options == "reset":
              confirm = inquirer.confirm(message="Confirm?").execute()
              display = {"fwd" : {"power" : "","control" : []},
                           "mid" : {"power" : "", "control" : []},
                           "aft" : {"power" : "", "control" : []}
                          }   

              with open(db, "w") as sending:
                  json.dump(display,sending,indent=2)
            return(my_catho.catho())

     def catho(): 
        with open(db, "r") as writing:
            data = json.load(writing)


            #choose list : make a note


            pos = inquirer.select(message="select which list:",choices=["fwd","mid","aft"]).execute()
            unit = inquirer.select(message="select which list:",choices=["power","control"]).execute()
            text = inquirer.text(message=":> ").execute()
#            note = inquirer.text(message="whats your note:").execute()
            confirm = inquirer.confirm(message="Confirm to save?").execute()

            if confirm == True:
              data[pos][unit] = text

        with open(db, "w") as sending:
             json.dump(data,sending,indent=2)
        my_catho.start()
my_catho.start()
