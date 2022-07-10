"""
advacne if statments
"""

def greet(username):
   print("hi {}".format(username))

#1st ask the user for name
username =  input("name plz:")
#2nd put in memory
actions = {"martell" : greet}

#3rd puts in memory
test = actions.get(username)
#4th grabs everything it knows and then runs everything
test(username)

