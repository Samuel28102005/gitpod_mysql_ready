mycursor.execute("SELECT * FROM Mammiferi")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)