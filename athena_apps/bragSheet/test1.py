from my_career import my_query
print("avgerage hours i work")
my_query.c.execute("SELECT AVG(duration) FROM ic_career")
print(my_query.c.fetchall())


