"""
this is going to be a huge project basically athna mk6 but in python,
 this fike will be a huge class that does multiple things:
    
    1.) takes input from flight ops and stores it into another python for
     organzitiin. with that being said we will also be downloading ploty to then
      make viusals
    
    2.)a dictionary

    3.)todo list:
        + i need to find a away to create a really alert todo this.
         i need time or dste to work agh
    
    4.)meassage server:
        Messages:
            Make a list containing a series of short text messages.
             Pass the list to a function called show_messages(),
              which prints each text message.
        Sending Messages:
            Start with a copy of your program from Exercise 8-9. Write a function
             called send_messages() that prints each text message and moves each
              message to a new list called sent_messages as it’s printed.
               After calling the function, print both of your lists to make
                sure the messages were moved correctly.
        Archived Messages:
            Start with your work from Exercise 8-10. Call the function
             send_messages() with a copy of the list of messages. After calling
              the function,print both of your lists to show that the original
               list has retained its messages.

"""

"""filename = 'bash.bashrc'

with open(filename, 'a') as file_object:
    file_object.write("#hey bash.bashrc can you here me, i just add a hastmark")
    file_object.write("\necho -e 'testing for another line' | lolcat")
  file_object.write("\nread -p 'this is being created from a .py file ok?:")
"""""
#this could be a dictiona d and you coukd put the var inside of def options(menu)
#need to creste the files for [ls,cd,cls,tree,cat] and alias things also
#i think that was why that file called var in ~/usr and or ~/login
#make a bash file dude and start cutting this athena.py up [this is rough]
menu = ("[1] Dictionary\n[2] Flight-log\n[3] todolist\n[4] meassage SRV\n")
file_one =  bash.bashrc

def login_screen():
    user = input('username: ')
    if user == ('mrcnotes'):
        print ('')
    elif user != ('mrcnotes'):
        return(end())
        pswd == input('password: ')
    if pswd == ('121200mdcD'):
        return(options())
    elif pswd != ('121200mdcD'):
        return(end) 
            

def options(file_one):
    print(menu)
    menu_answer = input(":")
if menu_answer == ('1'):
    #the code for Dictionary
    print("i would be you're dictionary")
    return(file_one)
    #dictionary()
elif menu_answer == ("2"):
    #the code for flight-log
    print("i would be you're flight-log ")
    #flight_log()
#elif menu_answer == ("3"):
    #the code for todo list
#    while True:
#        filename = 'todo-db.bashrc'
#        todo = input("type your meassage:\n")
#        with open(filename, 'a') as file_object: 
#            file_object.write("echo -e []        "+ todo +" | lolcat\n ")
        # so reformat to have a varoable amd when its entered you be able to
        # chnage in box.... honsetly we just need to think a little bit harder
#elif menu_answer == ("4"):
        #the code for meassage SRV
#    print("i would be you're meassage SRV ")
            # you could create a hard coded meassage server, you know how you like to 
            # talk to your self send a meassgae as a user A and have user be be abale to
            # text backa nd say you  convo in a fike and simple color code it with bashrc
            #meassage()
def end():
    print("access granted.") 
login_screen()

