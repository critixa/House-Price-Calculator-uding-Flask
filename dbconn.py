# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:25:28 2023

@author: HP
"""
import pymysql as pms

conn = pms.connect(host="localhost", 
                   port=3306,
                   user="root",
                   password="Sundhar@1610",
                   db="employee")
cur = conn.cursor()
#%%
cur.execute("select * from login")
#%%
output = cur.fetchone()
print(output)

#%%
import pandas as pd
sql = "select * from login"
df = pd.read_sql(sql, conn)























