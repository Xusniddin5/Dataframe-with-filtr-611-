# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1s-cXZxOk_AlKmPtH_GelzMPn5Sp2MvoG
"""

import pandas as pd
baza={
    "FISH":[ "Yo'ldashev Xusniddin ","Rahmatov Husniddin","Turg'unov Abdulbosit", "Sodiqova Mahliyo","Komilova Dinora","Kabirova Soliha","Sulaymonova Mahliyo","Abduhakimov Xursandbek", 'Nemotova Dildora','Mamadaliyev Zikrullo' ],
    "YOSHI":[ '19','19','19','20','19','18','19','19','19','19'  ],
    "MAKTABI":[ '33-IDUM','33-IDUM','12-maktab','5-maktab','5-maktab','33-IDUM','2-maktab','8-maktab','10-maktab','14-maktab'  ],
    "JINSI":["o'g'il bola","o'g'il bola","o'g'il bola",'ayol','ayol','ayol','ayol',"o'g'il bola", 'ayol', "o'g'il bola" ],
    "Manzili":[ 'Beshariq tumani ','Beshariq tumani','SHahrihon tumani','Beshariq tumani','Beshariq tumani','Beshriq tumani','Fargona viloyati','Boston tumani','Yaypan tumani','Fargona shahri' ]
}
db=pd.DataFrame(baza)
print(db)

filtr=db[db['JINSI']=="ayol"]
print(filtr)

filtr=db[db['JINSI']=="o'g'il bola"]
print(filtr)