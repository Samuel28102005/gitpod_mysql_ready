import mysql.connector

# Informazioni di connessione al database (sostituisci con i tuoi dati)
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

# Creazione del database
mycursor.execute("CREATE DATABASE Animali")

# Utilizzo del database appena creato
mydb.database = "Animali"

# Creazione della tabella Mammiferi
mycursor.execute("CREATE TABLE Mammiferi (Id INT AUTO_INCREMENT PRIMARY KEY, Nome_Proprio VARCHAR(255), Razza VARCHAR(255), Peso INT, Eta INT)")

mydb.commit()