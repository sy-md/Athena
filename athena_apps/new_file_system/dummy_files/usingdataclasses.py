from dataclasses import dataclass, field
from typing import List
@dataclass
class Person:
    name: str
    age: int
    occupation: str = field(init=False, repr=False)

"""
give data class a instance and give not fields its values
 do i need  to give it a instance lets see... no but for print yes
"""
p = Person('John Doe', 34)

#needs field as in im going to give this occuoation later
p.occupation = "Gardener"

#print("{} is a {} and is {}".format(p.name,p.occupation,p.age))


#####################


@dataclass
class House:
    name: str = field(init=False,repr=False)
    age: int


class Home:
    def test():
        House.age = 9
        House.name = input("name: ")
        print("{} is {} years old".format(House.name,House.age))
#Home.test()

##################################

"""
useing datacalss and typing List
"""
@dataclass
class jobs:
    my_jobs: List[str]

    def job_list():
        cal,bk1 = jobs([]),jobs([])

        print("Cal: {} \nbk1: {}".format(cal.my_jobs,bk1.my_jobs))
        chs = input("1.)cal\n2.)bk1: ")
        if chs == "1":
            print(cal.my_jobs)





from dataclasses import dataclass
from typing import Dict, List
import json
@dataclass
class Notebook:
    
    calendar: Dict[str, List[str]]

    def send():
        cal = Notebook( {} )
        print(cal.calendar)
        print(Notebook(Dict[str, List[str]]))
Notebook.send()


# Notebook.start(cal)#       cal,bk1 = jobs([]),jobs([])


#        print("Cal: {} \nbk1: {}".format(cal.my_jobs,bk1.my_jobs))
#        chs = input("1.)cal\n2.)bk1: ")
#        if chs == "1":
#            print(cNotebook.start(cal)al.my_jobs)

#################№############
"""
Concpect works:

    but its not a list its just string of data attachend to certain string of data

Notebook.start(cal)Notebook.start(cal)
"""
