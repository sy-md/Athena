from pymongo import MongoClient
import gridfs


def mongo_conn():
    try:
        conn = MongoClient("")
        print("connected", conn)
        return conn.nas_raspi
    except Exception as e:
        print("error", e)

#uri = "
#cli = MongoClient(uri)
#mydb = cli["nas_raspi"]
#collection = mydb["my_files"]

db = mongo_conn()
name = "image.jpg"
#loc = "/" + name
file_data = open(name, "rb")
data = file_data.read()
fs = gridfs.GridFS(db)
fs.put(data, filename = name)
print("upload complete")

data = db.fs.files.find_one({"filename" : name})
my_id = data["_id"]
outputdata = fs.get(my_id).read()
dwn_loc = "img/" + name
output = open(dwn_loc, "wb")
output.write(outputdata)
output.close()
print("download completed")

