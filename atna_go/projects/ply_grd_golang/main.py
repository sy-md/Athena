class person:
    def __init__(self,name):
        self.name = name

class BarDB:
    def __init__(self):
        self.id = []
        self.member = []

    def add(self, list_of_people):
        seen = []
        for x in list_of_people:
            if x.name not in self.id:
                self.id.append(x.name)
                seen.append(x.name)
                print(self.id)
            else:
                break

if __name__ == "__main__":
    p1 = person("marell")
    p2 = person("tilly")
    p3 = person("marell")
    mypeople = [p1,p2,p3]
    mydb = BarDB()
    mydb.add(mypeople)