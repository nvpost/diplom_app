import pymysql
from datetime import datetime, timedelta
import time

# import secret as secret

import sec_local as secret

print (secret.host)

con = pymysql.connect(secret.host, secret.user, secret.pas, 'diplom', cursorclass=pymysql.cursors.DictCursor)
cursor = con.cursor()
query = "select * from data"
cursor.execute(query)
rows = cursor.fetchall()

print(rows[0])