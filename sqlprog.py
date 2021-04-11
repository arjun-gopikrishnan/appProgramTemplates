import sqlite3

connection = sqlite3.connect("receipts.db")


cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS rentTable (date TEXT, receipt TEXT, company TEXT, representative TEXT, location TEXT, city TEXT, phone TEXT, leasee TEXT, license TEXT, address TEXT, state TEXT)")

#cursor.execute("CREATE TABLE company (name TEXT, reg TEXT, age INTEGER)")

#cursor.execute("INSERT INTO rentTable VALUES ('11-04-21', '0001', 'Uber', 'Monke','Dwarka','Delhi','9042120126','DL15AD12345','bigMonke','plot6','new Delhi')")

rows = connection.execute("select * from rentTable")
for row in rows:
    print(row)

connection.commit()
connection.close()
