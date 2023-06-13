from sqlalchemy import create_engine
import pyodbc
import fdb

for driver in pyodbc.drivers():
    print(driver)

con = fdb.connect(
    host='localhost', database='/opt/firebird/examples/empbuild/CASHERRN.gdb',
    #host='89.251.77.111/53050', database='C:\_SoftUr\DB\CASHERRN.gdb',
    charset='WIN1251',
    user='SYSDBA', password='masterkey'
  )
cur = con.cursor()
cur.execute("select * from credcard")
print(cur.fetchall())