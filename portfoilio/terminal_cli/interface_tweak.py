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
lnkls = "tessll.json"
@dataclass
class Node:
    data: Dict[str,Dict[str,List | str]]
    Next: Optional[None]

    def linked(my_cal):
        try:
            with open(my_cal,"r") as rd:
                data = json.load(rd)
                red = {"duration" : "1wk",
                    "type" : "Urgent",
                    "time" : [],
                    "timediff" : "days till"}

                yellow = {"duration" : "2wk",
                    "type" : "warning",
                    "time" : [],
                    "timediff" : "days till"}

                green = {"duration" : "3wk",
                    "type" : "still got time",
                    "time" : [],
                    "timediff" : "days till"}

                pink = {"duration" : "4wk",
                    "type" : "get planning",
                    "time" : [],
                    "timediff" : "days till"}

                #build indivual node
                Node.Next = ""
                a = Node(red,Node.Next)
                b = Node(yellow,Node.Next)
                c = Node(green,Node.Next)
                d = Node(pink,"null")

                #chain them together
                a.Next = b
                b.Next = c
                c.Next = d

                #my linked list
                my_l_lst = (asdict(a))

                print("file was found ready for manip")
                print(my_l_lst)

                #grabe the data needed
                srt = data["duration"][0][0]
                end = data["duration"][0][1]

                #parsed start date[month,day]
                srt_mnth = srt[:3]
                srt_day = srt[3:5]

                #parsed end date[month,day]
                end_mnth = end[:3]
                end_day = end[3:5]

                months = {"jan" : 31,"feb" : 28,"mar": 31,
                  "apr" : 30,"may" : 31,"jun" : 30,
                  "jul" : 31,"aug" : 31,"sept" : 30,
                  "oct" : 31,"nov" : 30,"dec": 31}

                """ # secound part of the function
                    if i need to you can use this formula to convert negtive to postive
                    postive = ( neg(nth) + ( pos(nth) * 2 ) )

                    were also gonna have to ad that other feeatur the tuple featue
                    (diff in days, diff in moths)
                """

                if srt_mnth in months:
                    cap = ( months[srt_mnth] )
                    f1 = ( (cap - int(srt_day)) + int(end_day) )
                    f2 = ( (int(end_day)) - int(srt_day) )

                    print("my tuple idea (f1,f2) ({},{})".format( f1,f2 ) )
                    one_wk = 7
                    same_mnth = (srt_mnth == end_mnth)
                    diff_mnth = (srt_mnth != end_mnth)

                    #if diff lst or eqt one_wk and same month
                    #if diff lst or eqt onw_wk and diff f1 <= one_wk and diff months
                    if ( f2 <= one_wk ) and (same_mnth):
                        print(" same month :red urgent one week")
                        print(f2)
                    elif (f1<= one_wk ) and ( f1 <= one_wk and diff_mnth):
                        print("diff months: red urgent onw week")
                        print(f1)
                    if ((f2 > one_wk) and (same_mnth) and (f2 <= (one_wk * 2)) ):
                        print("same moths two week")
                        result = f2

#                        if len( b.data["time"] ) == 0:
#                            print("put result in node")
#                            b.data["time"].append(result)
#                        elif ( f2 <= one_wk ) and (same_mnth):
#                            rm = b.data["time"].pop(rm)
#                            a.data["time"].append(rm)
                        return(Node.render(my_l_lst,result))

                    elif ((f1 > one_wk) and (f1 <= ( one_wk * 2 )) and (diff_mnth) ):
                        print("diff moths two weeks")
                        print(f1)
                    if ((f2 > one_wk * 2) and (same_mnth) and (f2 <= (one_wk * 3)) ):
                        print("same moths three weeks")
                        print(f2)
                    elif ((f1 > one_wk * 2 ) and (f1 <= ( one_wk * 3 )) and (diff_mnth) ):
                        print("diff moths three weeks")
                        print(f1)

                    if ((f2 > one_wk * 3) and (same_mnth) and (f2 <= (one_wk * 4)) ):
                        print("same moths four weeks")
                        print(f2)
                    elif ((f1 > one_wk * 3 ) and (diff_mnth) ):
                        print("diff moths four +  weeks")
                        print(f1)

        except FileNotFoundError:
            print("making the file")
            with open(lnkls,"w") as snd:
                json.dump(my_l_lst,snd,indent=3)

    def render(my_l_lst,result):
        print(my_l_lst)
        print("made a the file")
        with open ("tessll.json","w") as snd:
            json.dump(my_l_lst,snd,indent=3)

        with open("tessll.json","r") as rd:
            data=json.load(rd)
            print(data)
            """
            make new varibles that equal to the json links
            like a = Node(red,NOde.next)
            but to read json  do a = data[][][][][]
            to the right one


            """
            if data["data"]["next"]["data"]["duration"] == "2wk":
                print("put result in node")
                data["data"]["next"]["data"]["duration"]["time"].append(result)
                print("we could just use time to ")
                print(data)
#                b.data["time"].append(result)
            elif ( f2 <= one_wk ) and (same_mnth):
                pass
#                rm = b.data["time"].pop(rm)
#                a.data["time"].append(rm)
                """
                red = {"duration" : "1wk",
                    "type" : "Urgent",
                    "time" : [],
                    "timediff" : "days till"}

                yellow = {"duration" : "2wk",
                    "type" : "warning",
                    "time" : [],
                    "timediff" : "days till"}

                green = {"duration" : "3wk",
                    "type" : "still got time",
                    "time" : [],
                    "timediff" : "days till"}

                pink = {"duration" : "4wk",
                    "type" : "get planning",
                    "time" : [],
                    "timediff" : "days till"}
                """
                """
                all done borded tired aug04-aug05 00:22 15hr session
                loggin off aug5 todo:
                    * create liknked list
                    * and add funcionality

                PRINTS THE STATMENT AND THEN CHECK THE LINKED THE LIST OF IHAS FOR
                EXAMPLE  SAEM MONTH THREE WEEKS {WARNINGN} THEN LOOK IN THE THE JSON
                IF THAT WORD IS  THE JSON THEN PUT THE DATA IN THE THAT SLOT

                """


@dataclass
class calendar: #filter data for the calendar with parsing
    duration: Optional[List[str]]
    note:     Optional[Dict[str,str]]
    category: Optional[List[str]]

    def check_calendar(data,entry): #check during and after
        try:

            with open (my_cal,"r") as reading:
                data = json.load(reading)

                #pretend this is a category
                #data["note"] = entry
                print(entry["category"])
                with open (my_cal,"w") as reading:
                    json.dump(entry,reading,indent=4)
                return calendar.vaildation()

        except FileNotFoundError:
            with open (my_cal,"w") as reading:
                json.dump(p1,reading)
                print("i put data in the json")
            return calendar.check_calendar(entry)

    def vaildation():
        print("Vaildating...")
        with open (my_cal,"r") as reading:
            data = json.load(reading)
            print("checking for zize of message")
            for x in range(len(data["note"])):
               if x > 5:
                   raise ValueError("sy: to big")
        return(Node.linked(my_cal))


class interface:
    def start():# gets user choice for direction of program
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
                json.dump(asdict(calendar([],{},[])),send_cal,indent=4)
            with open ( opt[chs] ,"r") as reading_cal:

                data = json.load(reading_cal)
                os.system("touch cal.json")
                os.system("sleep 2")
            return interface.start()

    def my_cal(data):
        #start the calendar program
        stt = inquirer.text(message="start: time|date ").execute()
        end = inquirer.text(message="end: time|date ").execute()
        my_lst = (stt,end)
        #making anote
        msg = inquirer.text(message="note: ").execute()
        print(data["category"]) # []

        with open ("cal.json",'r') as rd:
            data = json.load(rd)


            if "add" not in data["category"]:
                data["category"].append("add")

            category_ops = inquirer.select( message="select your options:",
                choices=data["category"]).execute()

            if category_ops == "add":
                new_cat = inquirer.text(message="make a new category: ").execute()
                data["category"].append(new_cat)

            category = data["category"]
            data["note"][new_cat] = msg
            note = data["note"]
            duration = data["duration"]
            duration.insert(0,my_lst) #stack
            with open ("cal.json",'w') as update_cal:
                json.dump(data,update_cal,indent=4)

        entry = asdict(calendar(duration,note,category))
        return calendar.check_calendar(data,entry)

    def my_ntbk():
        pass
        note = inquirer.text(message="add a new category:").execute()

interface.start()

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








