import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  port=3306,
  user="root",
  password="",
  database="stage"
)

#select all
cursor = db.cursor(buffered=True)
cursor.execute("select * from etudiant")
resultat = cursor.fetchall()
for x in resultat:
  print(x)

#select only nom,prenom,age
cursor.execute("select nom,prenom,age from etudiant")
resultat=cursor.fetchall()
for x in resultat :
    print(x)

#select only one
cursor.execute("select * from etudiant")
resultat=cursor.fetchone()
print(resultat)

# select record where the prenom = dridi
rlt="select * from etudiant where prenom = 'dridi'"
cursor.execute(rlt)
resultat=cursor.fetchall()
for x in resultat :
    print(x)

#trié le resultat selon l'age
rlt="select * from etudiant order by age"
cursor.execute(rlt)
resultat=cursor.fetchall()
for x in resultat :
    print (x)

#trié le resultat selon l'age decroissant
rlt = "select * from etudiant order by age DESC"
cursor.execute(rlt)
result = cursor.fetchall()
for x in result:
  print(x)

#Delete any record where the nom is "dridi"
rlt = "delete from etudiant where prenom ='dridi'"
cursor.execute(rlt)
db.commit()
print(cursor.rowcount, "record deleted")

#delete the table etudiant 
# rlt = "drop table etudiant"
# cursor.execute(rlt)

#Delete the table "etudiant" if it exists
# cursor = db.cursor()
# rlt = "drop table if exists etudiant"
# cursor.execute(rlt)

#Overwrite the nom column from "toukebri" to "belhaj":
rlt = "update etudiant set nom = 'belhaj' where nom = 'toukebri'"
cursor.execute(rlt)
db.commit()
print(cursor.rowcount, "record affected")

#Escape values by using the placeholder %s method
rlt = "update etudiant set nom = %s where nom = %s"
val = ("toukebri", "belhaj")
cursor.execute(rlt, val)
db.commit()
print(cursor.rowcount, "recor affected")


