# -*- coding: utf-8 -*-
"""Untitled47.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10JlQQPX9EQF7PrITLpQ7chlWAusyqUaZ
"""

import pandas as pd
baza={
    "FISH":["Aliyeva Ra'no" , "Valiyev Vali"   ],
    "Yoshi":[ '11',  '15' ],
    "Maktabi":['Prezident maktabi' , 'Prezident maktabi'    ],
    "Jinsi":[  'qiz bola' ,  "o'g'il bola"  ],
    "Manzili":[ 'Andijon shaxar'  ,  "Farg'ona shaxar" ]
}
db=pd.DataFrame(baza)
print(db)

filtr=db[db['Maktabi']=='Prezident maktabi']
print(filtr)

filtr=db[(db['Maktabi']=='Prezident maktabi') & (db['Jinsi']=="o'g'il bola")]
print(filtr)