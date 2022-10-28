
x_json = "mydb.json" # the backend 
my_nbk = "display.json" #notebook db
my_cal = "cal.json" # calendar db

from InquirerPy import inquirer
from InquirerPy.prompts.expand import ExpandChoice
from colorama import Back,Fore,Style,init
import json,os,calendar,traceback,sys
from pprint import pprint
from calendar import TextCalendar
from typing import List,Dict,Optional
from dataclasses import dataclass,asdict,field


@dataclass
class person: #filter data for the calendar with parsing
    name: Optional[str]

    def check(p1):
        try:
            with open (my_cal,"r") as reading:
                data = json.load(reading)
                #pretend this is a category
                data["name"] = p1
                with open (my_cal,"w") as reading:
                    json.dump(p1,reading)
                return person.ant()

        except FileNotFoundError:
            with open (my_cal,"w") as reading:
                json.dump(p1,reading)
                print("i put data in the json")
            return person.check(p1)

    def ant():
        with open (my_cal,"r") as reading:
            data = json.load(reading)
            print("checking for int")
            for x in range(len(data["name"])):
               if x > 5:
                   raise ValueError("sy: to big")


class test:
    def mystart():
        msg = input("note: ")
        p1 = asdict(person(msg))
        return person.check(p1)


test.mystart()

#good 
