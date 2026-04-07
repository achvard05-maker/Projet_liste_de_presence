import sqlite3 

conn = sqlite3.connect('base_test.db')

cur = conn.cursor()

classe = [
    ('ADJAYI','Jacques',2000),
    ('AGBALENYO','Haniel',2001),
    ('AKOTO','Bright',2002),
    ('AKOUTE','Rosita',2003),
    ('ATTAH','Hervé',2004),
    ('DIGBANI','Achille',2005),
    ('ESSEH','Edem',2006),
    ('FOLIKOUE','Maximin',2007),
    ('TIDJANI','Afdal',2008),
    ('KOSSI','Godwin',2009),
]

cur.executemany("INSERT INTO etudiant(nom, prenom, matricule) VALUES (?,?,?)",classe)

conn.commit()

conn.close()

print("Félicitations ! Les étudiants ont été ajoutés avec succès")