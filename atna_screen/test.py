# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import sys

sys.path.append("../atna_settings/atna_plugins/PyInquirer")

from pprint import pprint

from PyInquirer import prompt, Separator

from examples import custom_style_1


questions = [
      {
            "type": "input",
            "name": "first name: ",
            "message": "what\'s you last name",
      }
]

answers = prompt.prompt(questions, style=custom_style_1)
pprint(answers)
