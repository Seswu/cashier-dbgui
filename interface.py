import tkinter as tk

class App:
	def __init__(self, master):
		frame = tk.Frame(master)
		frame.pack()
		self.quitbutton=tk.Button(frame, text="Quit", command=frame.quit)
		self.quitbutton.pack(side=tk.BOTTOM)
		self.lb=tk.Listbox(frame)
		self.lb.pack(side=tk.TOP)
		
	def loadlist(self, itemlist):
		for item in itemlist:
			self.lb.insert(tk.END, item)
		
root=tk.Tk()
app=App(root)
app.loadlist(["one", "two", "three", "four", "five"])
root.mainloop()
root.destroy
