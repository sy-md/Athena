import os 
#print ("f{""})
avaiable = 500
taken = 0

class hotel:

    
    def hotel_info():
        print("Name of hotel: " "DreamCast")
        #os.system("figlet Dreamcast" | lolcat)
        print("Fonder: " "Martell Dorsett")
        print("Avaible rooms: "  f"{avaiable}")
        print("Rooms taken: "  f"{taken}")
        

    def booking_leaveing():
        my_emplyoees = ("kimber", "carly", "cherry","sam","kindread")
        postions = ("CEO", "clerk", "cleaner", "bell-boy")
        age = (29,34,26,28,28)

        kimber_said = (f"{postions[1]}" + (f"({my_emplyoees[0]})" + (f"[{age[0]}] ") + "said: " ))
        kimber_did = (f"{postions[1]}" + (f"({my_emplyoees[0]})" + (f"[{age[0]}] ") + "did: " ))
        sam_said = (f"{postions[3]}" + (f"({my_emplyoees[3]})" + (f"[{age[4]}] ") + "said: " ))
        sam_did = (f"{postions[3]}" + (f"({my_emplyoees[3]})" + (f"[{age[4]}] ") + "did: " ))

        greeting = input(kimber_said + "hello! are you checking in or checking out? :")
        
        if greeting == "checking in":
            print(kimber_said + "ill have our " + postions[3] + " get your bags")
            print(sam_said + " may i take your bags to your room")
            print(kimber_said + "you are room 001, enjoy!")
    
    def checking_system():
        room_avaiable = (avaiable - 1)
        room_taken = (taken  + 1)
        print(room_avaiable)
        print(room_taken)
    #we need to make a system that keeps track of how many rooms are avaiable and how man room are taken

hotel.hotel_info()
hotel.booking_leaveing()
hotel.checking_system()


    









