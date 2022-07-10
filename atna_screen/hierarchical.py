# -*- coding: utf-8 -*-
"""
hierarchical prompt usage example
"""
import sys

sys.path.append("../atna_settings/atna_plugins/PyInquirer")

from PyInquirer import style_from_dict, prompt

from examples import custom_style_2


def inital_question_one():
    directions_prompt = {
        'type': 'list',
        'name': 'type',
        'message': 'what are you looking at?: ',
        'choices': ["power","control"]
    }
    answers = prompt.prompt(directions_prompt)
    return answers['type']

def inital_question_two():
    directions_prompt = {
        'type': 'list',
        'name': 'location',
        'message': 'Where are you? >:',
        'choices': ["mid","aft","fwd"]
    }
    answers = prompt.prompt(directions_prompt)
    return answers['location']

def inital_question_three():
    new_prompt = {
        "type": "input",
        "name": "answ",
        "message": "how much power is there: ",
       }
    answers = prompt.prompt(new_prompt)
    return answers['answ']


def main():
    print('welcome to the catho manger \n')
    my_type = inital_question_one()
    direction = inital_question_two()
    output = inital_question_three()
    next(my_type,direction,output)

def next(my_type,direction,output):
   dic = {
             direction : {
             my_type: output
       }
   }
   print(dic)

if __name__ == '__main__':
    main()
