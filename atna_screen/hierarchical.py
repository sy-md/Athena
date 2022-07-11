# -*- coding: utf-8 -*-
"""
hierarchical prompt usage example
"""
import sys

sys.path.append("../atna_settings/atna_plugins/PyInquirer")

from PyInquirer import style_from_dict, prompt

from examples import custom_style_2

from pprint import pprint


class catho():
     def question_one():
        directions_prompt = {
                  'type': 'list',
                  'name': 'type',
                  'message': 'what are you looking at?',
                  'choices': ["power","control"]
                }
        answers = prompt.prompt(directions_prompt)
        return answers['type']

     def question_two():
         directions_prompt = {
                   'type': 'list',
                   'name': 'location',
                   'message': 'Where are you?',
                   'choices': ["mid","aft","fwd"]
                 }
         answers = prompt.prompt(directions_prompt)
         return answers['location']

     def question_three():
        new_prompt = {
           "type": "input",
           "name": "answ",
           "message": "how much power is there: "
         }
        answers = prompt.prompt(new_prompt)
        return answers['answ']

     def question_four():
        new_prompt = {
           "type": "input",
           "name": "answ_otther",
           "message": "so what the readings: "
         }
        answers = prompt.prompt(new_prompt)
        return answers['answ_other']


     def main():
        print('Welcome to the catho manger\nSo what are you waiting for... fill me in!!! \n')
        type = catho.question_one() #power or control
        pos = catho.question_two() #fwd,mid,aft
        pwr = catho.question_three()
        cnt = catho.question_four()

"""
make one class of catho and make one def that has a INPUT




"""
if __name__ == '__main__':
    catho.main()
