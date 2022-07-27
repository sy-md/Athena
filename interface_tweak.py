from InquirerPy import inquirer
from InquirerPy.prompts.expand import ExpandChoice
from colorama import Back,Fore,Style,init
import json,os,calendar,traceback,sys
from pprint import pprint
from calendar import TextCalendar
from typing import List,Dict,Optional
from dataclasses import dataclass,asdict,field

x_json = "mydb.json" # the backend 
my_nbk = "display.json" #notebook db
my_cal = "cal.json" # calendar db


@dataclass
class calendar: #filter data for the calendar with parsing
    note: Optional[str]
    category: Optional[str]

    def check_calendar(data,entry):
        try:
            with open (my_cal,"r") as reading:
                data = json.load(reading)

                #pretend this is a category
                data["note"] = entry

                with open (my_cal,"w") as reading:
                    json.dump(entry,reading)
                return calendar.ant()

        except FileNotFoundError:
            with open (my_cal,"w") as reading:
                json.dump(p1,reading)
                print("i put data in the json")
            return calendar.check(entry)

    def ant():
        with open (my_cal,"r") as reading:
            data = json.load(reading)
            print("checking for int")
            for x in range(len(data["note"])):
               if x > 5:
                   raise ValueError("sy: to big")


class interface:
    def start():
        os.system("clear")
        os.system("figlet '              Athena' | lolcat -8")
        print("             Welcome back sy, What can I do for you\n")
        os.system("cal -n3 | lolcat -8")

        os.system("date")
        main_op = inquirer.expand(
                message="select a option:",
                choices=[
                    ExpandChoice(key="1",name="Calendar",value="1"),
                    ExpandChoice(key="2",name="Notebook",value="2"),
                    ExpandChoice(key="3",name="Exit", value="3")
                ]).execute()

        if main_op == "3": #exit
            print("logging off")
            exit()
        confirm = inquirer.confirm(message="Confirm?").execute()

        #options for path
        if confirm == True and main_op == "App" or "2" or "1":
            return interface.get_json(main_op)
        else:
            if confirm == False and main_op == "App" or "2" or "1":
                print("Powering Off")
                exit()

    def get_json(main_op): #makes and grab write data for the user choose

        opt = [my_cal,my_nbk]
        chs = (int(main_op) - 1)

        try:
            with open (opt[chs],"r") as reading_cal:
                data = json.load(reading_cal)
                if chs == 0: # calendar
                    return interface.my_cal(data)

                if chs == 1: # notebook
                    return interface.my_cal(data)

        except FileNotFoundError:
            with open (opt[chs],'w') as send_cal:
                json.dump({},send_cal,indent=4)

            with open ( opt[chs] ,"r") as reading_cal:
                data = json.load(reading_cal)
            return interface.my_cal(data)


    def my_cal(data):
        note = input("note: ")
        category = input("choose:")
#       if category in data["category"]:
        entry = asdict(calendar(note,category))
#           return calendar.check_calendar(data,entry)
#       if category == "add":
#           new_category = input("make a category: ")
#           entry = asdict(calendar(note,new_category))
        return calendar.check_calendar(data,entry)
    def my_ntbk():
        pass

interface.start()




#         
#
#     def calendar(): 
#        try: # try to open the calendar json
#           with open (my_cal,"r") as reading_cal:
#               data = json.load(reading_cal)
#        #rebuild if not there
#        except FileNotFoundError: 
#              cal = {
#                     "Calendar": [],
#                     "category": []
#                    }(
#              with open(my_cal, "w") as sending_cal:
#                  json.dump(cal,sending_cal, indent=4)
#              return(interface.calendar())
#        else: #continue if file is good
#          if len(data["category"]) == 0: # check if empty fixing empty category
#            #add a filler category 
#            new = inquirer.text(message="add a new category:").execute()
#            data["category"].append(new)
#
#            with open(my_cal, "w") as cal_correction:
#                json.dump(data,cal_correction, indent=4)
#            return(interface.calendar())
#
#          """
#          TODO
#          checkboxes to make item that has passed or that have been finshed
#          or
#          if enddate is given mark it and if date _ matches remove
#          """
#
#
#          # start the calendar program
#          str = inquirer.text(message="start: time|date ").execute()
#          end = inquirer.text(message="end: time|date ").execute()
#          category = inquirer.select( message="select your options:",
#                           choices=data["category"]).execute()
#      
#          if category == "add": # adding new category to calendar
#            new = inquirer.text(message="add a new category:").execute()
#            note = inquirer.text(message="whats your note:").execute()
#            data["Calendar"].append("{}•{} {} : {}".format(str,end,new,note))
#
#            with open(my_cal, "w") as sending_cal:
#                json.dump((data["category"].append(new),data),sending_cal, indent=4)
#
#            exit = inquirer.confirm(message="go back to home screen").execute()
#            if exit == True:
#              return(interface.start())
#            else:
#              return(interface.calendar())
#
#          # continue the calendar program
#          note = inquirer.text(message="whats your note:").execute()
#          data["Calendar"].append("{}•{} {} : {}".format(str,end,category,note))
#
#          with open(my_cal, "w") as sending_cal: #send a entry
#              json.dump(data,sending_cal, indent=4)
#              os.system("sleep 2")
#              print("data sent...")
#
#          exit = inquirer.confirm(message="go back to home screen").execute()
#          if exit == True:
#            return(interface.start())
#          else:
#            return(interface.calendar())
#
#     def App():
#        dir = "/data/data/com.termux/files/home/Athena/temp_apps"
#        os.chdir(dir)
#        os.system("pwd")
#        action = inquirer.fuzzy(
#                          message="Select actions:",
#                          choices=( os.listdir(".")),max_height="70%").execute()
#        #try that video idea you made or import then
#        os.system("python {}".format(action))
# 
#     def NoteBook():
#        """
#        first:
#             check for any bugs on the first go through
#
#        TODO:
#            Try to read the file
#            good then continue
#            else create the files data
#
#           add pick list add note
#           remove pick like and postion remove
#           edit pick list change value
#            
#
#        """
#        try: 
#            with open(my_phone, "r") as writing:
#                data = json.load(writing)
#
#        except FileNotFoundError:
#              display = {
#                    "notes": {}, # want to change to a dict
#                    "Q1": {},
#                    "Q2": {},
#                    "Q3": {},
#                    "Q4": {}
#                    }
#              with open(my_phone, "w") as sending:
#                  json.dump(display,sending, indent=4)
#        else:
#         pprint(data,sort_dicts=True,indent=2)
#   
##        for k,v in data.items(): 
##           new_data = ("{}:{}".format(k,v))
##           pprint(new_data,sort_dicts=True)
#
#         options = inquirer.select(
#                            message="choose a selection ",
#                            choices=["reset","edit","add","remove"]).execute()
#         if options == "reset":
#                confirm = inquirer.confirm(message="Confirm?").execute()
#                display = {
#                    "notes": {}, # want to change to a dict
#                    "Q1": {},
#                    "Q2": {},
#                    "Q3": {},
#                    "Q4": {}
#                    }
#                with open(my_phone, "w") as sending:
#                    json.dump(display,sending, indent=4)
#                    print("sending data ....")
#                    os.system("sleep 3")
#                return(interface.start())
#
#         if options == "remove":
#           choose_lst = inquirer.select(message="select which list:",choices=data).execute()
#           chs_title = inquirer.select(message="choose witch entry:",choices=data[choose_lst]).execute()
#           confirm = inquirer.confirm(message="Confirm to remove").execute()
#
#           if confirm == True:
#             del  data[choose_lst][chs_title]
#
#             with open(my_phone, "w") as sending:
#                 json.dump(data,sending,indent=2)
#
#             exit = inquirer.confirm(message="go back to home screen").execute()
#             if exit == True:
#               return(interface.start())
#             else:
#                 return(interface.NoteBook())
#
#         # edit list : make changes *.replace
#         if options == "edit": #a switch would be cool
#
#             choose_lst = inquirer.select(message="select which list:",choices=data).execute()            
#             choose_itm = inquirer.select(message="choose witch entry:",choices=data[choose_lst]).execute()
#             ed_note = inquirer.text(message="whats your note: ").execute()
#             confirm = inquirer.confirm(message="Confirm to change message?").execute()
#           
#             if confirm == True:
#               data[choose_lst][choose_itm] = (ed_note)
#
#             with open(my_phone, "w") as sending:
#              json.dump(data,sending,indent=2)
#
#             exit = inquirer.confirm(message="go back to home screen").execute()
#             if exit == True:
#               return(interface.start())
#             else:
#                  return(interface.NoteBook())
#     
#         #choose list : make a note
#         if options == "add":
# 
#           choose_lst = inquirer.select(message="select which list:",choices=data).execute()
#           title = inquirer.text(message="title your note:").execute()
#           note = inquirer.text(message="whats your note:").execute()
#           confirm = inquirer.confirm(message="Confirm to save?").execute()
#
#           if confirm == True:
#             data[choose_lst][title] = note
#
#             with open(my_phone, "w") as sending:
#                 json.dump(data,sending,indent=2)
#
#             exit = inquirer.confirm(message="go back to home screen").execute()
#             if exit == True:
#               return(interface.start())
#             else:
#                  return(interface.NoteBook())


#interface.start()
"""
TODO: code to disppay notes fom my_phone  

with open(my_phone, "r") as writing:
    data = json.load(writing)

    #quick_list vertical display
    convert = data["quick_list"]
    color_format = ("\t" + Fore.CYAN + Style.BRIGHT)
    for i in range(len(convert)):
        print(color_format + "{} : {}".format(i + 1 ,convert[i]))

    print(Fore.CYAN + Style.BRIGHT + "")

    #prints the topic and description
    for x in data:
        test_1 = x
        test_2 = data[x]

        pprint("{} - {}".format(test_1,test_2),compact=True)
"""








