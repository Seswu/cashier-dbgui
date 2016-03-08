import pypyodbc
#{}[] sg_v2
driver = '{SQL Server}'
user = 'dbscript'
password = 'rettekasse34'
server = 'WIN7_MIC_KASSE\SIOGES'
database = 'sg_v2'

conn_string = "DRIVER=%s; UID=%s; PWD=%s; SERVER=%s; DATABASE=%s;" % (driver, user, password, server, database)
connection = pypyodbc.connect(conn_string)
c = connection.cursor()
c.execute('select top 15 * from dbo.td_CobrosTicket')
result = c.fetchone()

print("Første række i tabel dbo.td_CobrosTicket:")
print(result)
c.close()
