# Inserimento di 5 animali
sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
val = [
  ('Fido', 'Canis lupus familiaris', 25, 3),
  ('Micio', 'Felis catus', 5, 2),
  ('Rocky', 'Canis lupus familiaris', 30, 4),
  ('Luna', 'Felis catus', 4, 1),
  ('Max', 'Equus caballus', 500, 10)
]

mycursor.executemany(sql, val)

mydb.commit()