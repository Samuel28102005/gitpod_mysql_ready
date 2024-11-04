for i in range(5):
  nome = input("Inserisci il nome dell'animale: ")
  razza = input("Inserisci la razza: ")
  peso = input("Inserisci il peso: ")
  eta = input("Inserisci l'età: ")

  # Verifica se peso ed età sono interi
  try:
    peso = int(peso)
    eta = int(eta)
    sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
    val = (nome, razza, peso, eta)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Animale inserito correttamente!")
  except ValueError:
    print("Peso ed età devono essere numeri interi.")

# Verifica finale (stampa tutti gli animali)
mycursor.execute("SELECT * FROM Mammiferi")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)