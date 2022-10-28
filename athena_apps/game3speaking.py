class person:
    def __init__(self,name,val):
        self.name = name
        self.val = val

class game:
    def __init__(self,npc): # -> list
        self.npc = npc
        self.backend = {1 : "hi",
                        2 : "bye",
                        3:"i have some gold"}

    def speak(self):
        ply = self.npc

        for i,v in enumerate(ply): # list(tuples())
            ply_name = (ply[i].name)
            ply_vals = (v.val)

            said = self.backend[ply_vals]
            print(ply_name,"said",said)

knight1 = person("harry",1)
knight2 = person("jarry",2)
elf = person("lilly",3)

npc = [knight2,knight1,elf]

mygame = game(npc)
mygame.speak()

