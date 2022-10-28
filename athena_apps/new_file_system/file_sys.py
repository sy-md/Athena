"""

dummy_files - unfiltered files
new_sys_files - filtered files

collector:
    •grab all files
    • can filter between .txt .py ect
    • json lib {file name : [tags]} ablie to groups tags

    can also do  the same with pictures | differnt os sys

dispenser:
    •display files and choose edit,run


example:

.txt .go .py
active = not finsh
done = finished
zombie = temp

.md
first filename its asscoiated to

"""

x = "helper_zombie.py"
y = "helper.py"

qus = input("what do u wanna save this files as: a(not finsh),d(finished),z(zombie)")
extract = y.split()
g = extract[0][:6]
z = extract[0][6:]
if qus == "d":
    qus = "_finished{}".format(z)
print("{}{}".format(g,qus))
