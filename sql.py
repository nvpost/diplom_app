import pymysql
from datetime import datetime, timedelta
import time
import sec_local as secret

con = pymysql.connect(secret.host, secret.user, secret.pas, 'diplom', cursorclass=pymysql.cursors.DictCursor)
cursor = con.cursor()