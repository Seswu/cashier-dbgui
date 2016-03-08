import tkinter as tk
import pypyodbc
import os
#{}[] sg_v2

class SQLServer:
	def __init__(self):
		driver = '{SQL Server}'
		user = 'dbscript'
		password = 'rettekasse34'
		current_machine = os.environ['COMPUTERNAME']
		server = current_machine + '\SIOGES'
		database = 'sg_v2'

		try:
			conn_string = "DRIVER=%s; UID=%s; PWD=%s; SERVER=%s; DATABASE=%s;" % (driver, user, password, server, database)
			self.connection = pypyodbc.connect(conn_string)
			self.c = self.connection.cursor()

		except pypyodbc.Error(e):
			print(str(e))

	def load_table(self):
		try:
			self.c.execute('select top 2 * from dbo.td_CobrosTicket')
			result = self.c.fetchall()
			print(result)
			return result
		except pypyodbc.Error(e):
			print(str(e))

	def delete_tables(self):
		self.c.execute('DELETE FROM [sg_v2].[dbo].[td_CabecerasTicket]')
		self.c.execute('DELETE FROM [sg_v2].[dbo].[td_CobrosTicket]')
		self.c.execute('DELETE FROM [sg_v2].[dbo].[td_DescuentosTicket]')
		self.c.execute('DELETE FROM [sg_v2].[dbo].[td_ImpuestosTicket]')
		self.c.execute('DELETE FROM [sg_v2].[dbo].[td_LineasTicket]')
		self.c.execute('DELETE FROM [sg_v2].[dbo].[td_LineasTicketImpuestos]')
		self.c.commit()
		
	def status(self, table):
		countstring = "SELECT COUNT(*) FROM [sg_v2].[dbo].[%s]" % (table)
		print(countstring)
		self.c.execute(countstring)
		return self.c.fetchone()
		

	def close(self):
		c.close()


class App:
	def __init__(self, master, server):
		self.server = server
		
		frame = tk.Frame(master)
		frame.pack()
		
		self.intro=tk.Label(frame, text="Table row count for sg_v2:")
		self.intro.pack(side=tk.TOP)
		
		self.lb=tk.Listbox(frame, width=100)
		self.lb.pack(side=tk.TOP)
		
		self.deletebutton = tk.Button(frame, text="Delete all", command=self.delete_all)
		self.deletebutton.pack(side=tk.BOTTOM)
		
		self.quitbutton=tk.Button(frame, text="Quit", command=frame.quit)
		self.quitbutton.pack(side=tk.BOTTOM)
		
				
	def loadlist(self):
		itemlist = self.server.load_table()
		print(itemlist)
		for item in itemlist:
			self.lb.insert(tk.END, item)
		self.lb.pack(side=tk.TOP)
		
	def delete_all(self):
		self.server.delete_tables()
		
	def get_status(self):
		tablelist = ['td_CabecerasTicket', 'td_CobrosTicket', 'td_DescuentosTicket',
			'td_ImpuestosTicket', 'td_LineasTicket', 'td_LineasTicketImpuestos']
		prependstr = '[sg_v2].[dbo].'
		status = {}
		for table in tablelist:
			#db_string = prependstr + "[.%s]" % (table)
			status[table] = self.server.status(table)
			
		for table in tablelist:
			self.lb.insert(tk.END, table + ": " + str(status[table]))
		self.lb.pack(side=tk.TOP)
		
		


root=tk.Tk()
db=SQLServer()
app=App(root, db)
#app.loadlist()
app.get_status()
#app.loadlist(["one", "two", "three", "four", "five"])
root.mainloop()
root.destroy

