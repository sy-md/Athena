import json
from dataclasses import dataclass, asdict


class test:


    def func2():
        print("dataclasss callled meover")

    @dataclass
    class house:
        name: []

        try:
            def __post_init__(self):
 #               def check(): 
                    with open ("cal.json", "r")as reading:
                        data = json.load(reading)
                        print("im check")
                        print("post running")
                        print(data)            
                        if "martell" in data["name"]:
                            raise ValueError("cant be your name")
#                return check()
        except FileNotFoundError:
            print("something hmmmmm")

    name = house("martell")
    fix = (asdict(name))

    with open ("cal.json", "w")as send:
        json.dump(fix,send)

test.func2()
