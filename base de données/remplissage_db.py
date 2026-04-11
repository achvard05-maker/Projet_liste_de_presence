import sqlite3 

conn = sqlite3.connect('vraie_base.db')

cur = conn.cursor()

classe = [
    ('ABALO','Ganiatou Celia','IAI-2025-11-01043'),
    ('ADETONA','Djamal','IAI-2025-11-aaaaa'),
    ('ADJAYI','Jacques Emmanuel','IAI-2025-11-01139'),
    ('AGBALENYO',' Koami Haniel','IAI-2025-11-01248'),
    ('AHOULOU','Kodjo Romaric','IAI-2025-11-01116'),
    ('AKOTO','Bright Osborn Freeman','IAI-2025-11-01125'),
    ('AKOUETE','Kafoui Cyntia','IAI-2025-11-01133'),
    ('ALI-BIDJOWE','Zeynab','IAI-2025-11-01236'),
    ('ANANI','Dede Louise Sylvana','IAI-2025-12-01274'),
    ('ASSI','Essowèdéou Crepin','IAI-2025-11-01062'),
    ('ATTAH','Hervé','IAI-2025-11-01073'),
    ('AYENA','Germain','IAI-2025-11-01078'),
    ('BADOHOUN','Abla Eyram Lorraine','IAI-2025-11-01161'),
    ('BATCHOUDI','Hodalou Gnimdou','IAI-2025-11-01089'),
    ('BODJONA','Alphonse Magnoudéwa','IAI-2025-11-01028'),
    ('DAKETSE','Koffi Semefia','IAI-2025-11-01051'),
    ('DJIGBANI','Moni Achille','IAI-2025-11-01068'),
    ('DOSSA','Akou Yekonia','IAI-2025-11-01108'),
    ('EGAH','Elom Jérémie','IAI-2025-11-bbbbb'),
    ('ESSEH','Edem Junior','IAI-2025-11-01188'),
    ('FOLIKOUE','Foli Yao Maximin','IAI-2025-11-01218'),
    ('GABIAM','Emefa Phoebé','IAI-2025-11-01221'),
    ('GBEGBENI','Nnabè','IAI-2025-11-01170'),
    ('GNANZA','M. Alexandre-Marie','IAI-2025-11-01172'),
    ('HALOUBIYOU','Béni Essowaza','IAI-2025-11-01059'),
    ('KALAO','Esso-Wazam','IAI-2025-11-01099'),
    ('KOKOU','Edoh Rodrigue','IAI-2025-11-01180'),
    ('KOSSI','Godwin','IAI-2025-11-01144'),
    ('KOUYAKOUTOULI','Makiliwè Bénédicte','IAI-2025-11-01183'),
    ('LAWSON-PLACCA','Latevi Jean Jonathan','IAI-2025-11-01038'),
    ('MALOU','Manamédédé Ulrich','IAI-2025-11-01050'),
    ('MENSAH','Samuel Folly Wollagno','IAI-2025-11-01114'),
    ('NAGBANI','Dammipi Corneille','IAI-2025-11-01135'),
    ('NYAKOU','Yawo Laélien Jason','IAI-2025-11-01158'),
    ('PAKAMEY','Damba Nadège','IAI-2025-12-01295'),
    ('POTAPOU','Tchein Idaya','IAI-2025-11-01227'),
    ('SEMEDO','Kokou Ethiel','IAI-2025-11-ccccc'),
    ('SOADAN','Koffi Sylvain','IAI-2025-11-ddddd'),
    ('TABATE','Ephraim Essowaza','IAI-2025-11-01240'),
    ('TCHAKOROM','Atcha Ziade','IAI-2025-12-01280'),
    ('TCHEGBELE','Ramziya','IAI-2025-12-01287'),
    ('TIDJANI','Afdal','IAI-2025-12-01299'),
    ('TOLAKE','Lidaou Henri','IAI-2025-12-01304'),
    ('VEDOMEY','Amy Gloria','IAI-2025-12-01310'),
    ('WILSON','Adjé Kingson','IAI-2025-11-01254'),
    ('YIBOKOU','Yao','IAI-2025-11-eeeee')
  
]

cur.executemany("INSERT INTO etudiant(nom, prenom, matricule) VALUES (?,?,?)",classe)

conn.commit()

conn.close()

print("Félicitations ! Les étudiants ont été ajoutés avec succès")