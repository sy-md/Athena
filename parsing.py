import json,os

my_cal = "cal.json"

with open (my_cal, "r") as rd:
        data = json.load(rd)

        #grabe the data needed
        srt = data["duration"][0]
        end = data["duration"][1]

        #parsed start date[month,day]
        srt_mnth = srt[:3]
        srt_day = srt[3:5]

        #parsed end date[month,day]
        end_mnth = srt[:3]
        end_day = srt[3:5]

        #display a test of manipulation
        print("start month is {} end month is {} \n \
        start is date {} and end date is {}".format(
                srt_mnth,end_mnth,srt_day,end_day)
              )
 
        """
        take the parsed data and compaare then and find
        the differecees in weeks

        we also have to add the new Q-system to the database
        """
