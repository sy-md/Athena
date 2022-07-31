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
        end_mnth = end[:3]
        end_day = end[3:5]

        #display a test of manipulation
        print("start month is {} end month is {} \n \
        start is date {} and end date is {}".format(
                srt_mnth,end_mnth,srt_day,end_day)
              )

        #gonna just test the comparing with date
        if srt_mnth == end_mnth: # might need to compare to date
                print("same month")
        else:
                print("not the same month")

        #print the differ between the dates
        if int(srt_day) <= int(end_day):
                diff = int(end_day) - int(srt_day)
                print("the difference in day is {}".format(int(end_day) - int(srt_day)))
                #so we have the diff now for calculation
                one_wk = 7
                if diff <= one_wk:
                        print("{} is less then {}".format(diff,one_wk))
                if diff >= one_wk:
                        print("{} is more then {}".format(diff,one_wk))
