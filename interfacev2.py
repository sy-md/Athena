
from InquirerPy import inquirer
from colorama import Back,Fore,Style,init
import json,os,calendar,traceback
from pprint import pprint
from calendar import TextCalendar
#/data/data/com.termux/files/home/Athena/atna_screen/new_examples/InquirerPy/examples

#/data/data/com.termux/files/home/Athena/athena_apps/interface.py

x_json = "mydb.json" # the backend 
my_phone = "display.json" #notebook db
my_cal = "cal.json" # calendar db

class interface():
     
     def start():
        os.system("clear")
        os.system("figlet '              Athena' | lolcat -8")
        print("             Welcome back sy, What can I do for you\n")
        os.system("cal -n3 | lolcat -8")
        

#        TextCalendar.formatyear(self,2022, w=2, l=1, c=6, m=3)
        os.system("date")
        print("\n••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")

        try: #try to read the file
            with open (my_cal,"r") as reading_cal:
                data = json.load(reading_cal)
       
        except FileNotFoundError:
              cal = {
                     "Calendar": [],
                     "category": []
                    }
              with open(my_cal, "w") as sending_cal:
                  json.dump(cal,sending_cal, indent=4)
              return(interface.start())
        else: #if there is nothing wrong continue
          with open (my_cal,"r") as reading_cal:
              data = json.load(reading_cal)        
              for x in data["Calendar"]: 
                 pprint(x)
       
          print("\n••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
          main_op = inquirer.select(
                           message="select your options:",
                           choices=["App","NoteBook","Calendar","exit"]).execute()

          if main_op == "exit":
            exit()

          confirm = inquirer.confirm(message="Confirm?").execute()

          #TODO is there a better way
          if confirm == True and main_op == "App":
               interface.App()
          if confirm == True and main_op == "NoteBook":
               interface.NoteBook()
          if confirm == True and main_op == "Calendar":
               interface.calendar()

          if confirm == False and main_op == "App" or "NoteBook" or "Calendar":
               print("Powering Off")
               exit()
         

     def calendar(): 
        try: # try to open the calendar json
           with open (my_cal,"r") as reading_cal:
               data = json.load(reading_cal)
        #rebuild if not there
        except FileNotFoundError: 
              cal = {
                     "Calendar": [],
                     "category": []
                    }
              with open(my_cal, "w") as sending_cal:
                  json.dump(cal,sending_cal, indent=4)
              return(interface.calendar())
        else: #continue if everthing is fine
          if len(data["category"]) == 0: # fixing empty category

            new = inquirer.text(message="add a new category:").execute()
            data["category"].append(new)

            with open(my_cal, "w") as cal_correction:
                json.dump(data,cal_correction, indent=4)
            return(interface.calendar())
          # start the calendar program
          str = inquirer.text(message="start: time|date ").execute()
          end = inquirer.text(message="end: time|date ").execute()
          category = inquirer.select( message="select your options:",
                           choices=data["category"]).execute()
      
          if category == "add": # adding new category to calendar
            new = inquirer.text(message="add a new category:").execute()
            note = inquirer.text(message="whats your note:").execute()
            data["Calendar"].append("{}•{} {} : {}".format(str,end,new,note))

            with open(my_cal, "w") as sending_cal:
                json.dump((data["category"].append(new),data),sending_cal, indent=4)

            exit = inquirer.confirm(message="go back to home screen").execute()
            if exit == True:
              return(interface.start())
            else:
              return(interface.calendar())

          # continue the calendar program
          note = inquirer.text(message="whats your note:").execute()
          data["Calendar"].append("{}•{} {} : {}".format(str,end,category,note))

          with open(my_cal, "w") as sending_cal:
              json.dump(data,sending_cal, indent=4)
              os.system("sleep 2")
              print("data sent...")

          exit = inquirer.confirm(message="go back to home screen").execute()
          if exit == True:
            return(interface.start())
          else:
            return(interface.calendar())

     def App():
        dir = "/data/data/com.termux/files/home/Athena/temp_apps"
        os.chdir(dir)
        os.system("pwd")
        action = inquirer.fuzzy(
                          message="Select actions:",
                          choices=( os.listdir(".")),max_height="70%").execute()
        #try that video idea you made or import then
        os.system("python {}".format(action))
 
     def NoteBook():
        with open(my_phone, "r") as writing:
            data = json.load(writing)

            pprint(data)

            options = inquirer.select(
                            message="choose a selection ",
                            choices=["reset","edit","add","remove"]).execute()
            if options == "reset":
                confirm = inquirer.confirm(message="Confirm?").execute()
                display = {
                    "notes": {},
                    "Q1": [],
                    "Q2": [],
                    "Q3": [],
                    "Q4": []
                    }
                with open(my_phone, "w") as sending:
                    json.dump(display,sending, indent=4)
                    print("sending data ....")
                    os.system("sleep 3")
                return(interface.start())

            #choose list : make a note
            choose_lst = inquirer.select(message="select which list:",choices=data).execute()
            note = inquirer.text(message="whats your note:").execute()
            confirm = inquirer.confirm(message="Confirm to save?").execute()

            if confirm == True:
              data[choose_lst].append(note)

        with open(my_phone, "w") as sending:
            json.dump(data,sending,indent=2)

interface.start()
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








