import sqlite3

datas = [
("Adanada aysam","ayyrux"),
("burası f","bursalı keko"),
("x f","f x"),
(" 0 -1 ","exi bir"),
("x li bisi","cilgin cocuq"),
("falan filan ","bisiler fis")
]

dataBase = sqlite3.connect("simple.sqlite")


dbCursor=dataBase.cursor()
# dbCursor.execute("CREATE TABLE IF NOT EXISTS Books (Author, BookName)")
# for data in datas:
#     dbCursor.execute("INSERT INTO Books VALUES (?,?)",data)
# dataBase.commit()

dbCursor.execute("SELECT * FROM Books WHERE Author = 'Mehmet ali Alabora'")

dbDatas = dbCursor.fetchall()
#fetchmany(x) baştan x kadar çeker 
for data in dbDatas:
    print(data)

dataBase.close()