import json,os

my_cal = "cal.json"
#first part of the function 
with open (my_cal, "r") as rd:
        data = json.load(rd)

        #grabe the data needed
        srt = data["duration"][0][0]
        end = data["duration"][0][1]

        #parsed start date[month,day]
        srt_mnth = srt[:3]
        srt_day = srt[3:5]

        #parsed end date[month,day]
        end_mnth = end[:3]
        end_day = end[3:5]

        months = {"jan" : 31,"feb" : 28,"mar": 31,
                  "apr" : 30,"may" : 31,"jun" : 30,
                  "jul" : 31,"aug" : 31,"sept" : 30,
                  "oct" : 31,"nov" : 30,"dec": 31}

        """ # secound part of the function
        if i need to you can use this formula to convert negtive to postive
                postive = ( neg(nth) + ( pos(nth) * 2 ) )

        were also gonna have to ad that other feeatur the tuple featue
                (diff in days, diff in moths) 
        """

        if srt_mnth in months:
                cap = ( months[srt_mnth] )
                f1 = ( (cap - int(srt_day)) + int(end_day) )
                f2 = ( (int(end_day)) - int(srt_day) )

                print("my tuple idea (f1,f2) ({},{})".format( f1,f2 ) )
                one_wk = 7
                same_mnth = (srt_mnth == end_mnth)
                diff_mnth = (srt_mnth != end_mnth)

                #if diff lst or eqt one_wk and same month
                #if diff lst or eqt onw_wk and diff f1 <= one_wk and diff months
                if ( f2 <= one_wk ) and (same_mnth):
                        print(" same month :red urgent one week")
                elif (f1<= one_wk ) and ( f1 <= one_wk and diff_mnth): 
                        print("diff months: red urgent onw week")

                if ((f2 > one_wk) and (same_mnth) and (f2 <= (one_wk * 2)) ):
                       print("same moths two week")
                elif ((f1 > one_wk) and (f1 <= ( one_wk * 2 )) and (diff_mnth) ):
                        print("diff moths two weeks")

                if ((f2 > one_wk * 2) and (same_mnth) and (f2 <= (one_wk * 3)) ):
                        print("same moths three weeks")
                elif ((f1 > one_wk * 2 ) and (f1 <= ( one_wk * 3 )) and (diff_mnth) ):
                        print("diff moths three weeks")

                if ((f2 > one_wk * 3) and (same_mnth) and (f2 <= (one_wk * 4)) ):
                        print("same moths four weeks")
                elif ((f1 > one_wk * 3 ) and (diff_mnth) ):
                        print("diff moths four +  weeks")

                """
                all done borded tired aug04-aug05 00:22 15hr session
                loggin off aug5 todo:
                        * create liknked list
                        * and add funcionality

                """
