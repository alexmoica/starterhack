import tkinter as tk
import re

class AutoComplete(tk.Entry):	
	def __init__(self, entries, *args, **kwargs):
		tk.Entry.__init__(self, *args, **kwargs)
		self.entries = entries
		self.var = self['textvariable']
		
		#define text input variable
		if self.var == '':
			self.var = self['textvariable'] = tk.StringVar()
		
		self.var.set("What is your university?")
		self.var.trace('w', self.update) #update on write
		self.bind('<Return>', self.select)
		self.bind('<Up>', self.up)
		self.bind('<Down>', self.down)
		
		self.lb_up = False
		self.lb = tk.Listbox()
	
	#define button functions, remove listbox if entry is empty
	def update(self, name, index, mode):
		if self.var.get() == '':
			self.lb_up = False
			self.lb.destroy()
		else:
			words = self.compare()
			if words:
				if not self.lb_up:
					self.lb = tk.Listbox(width=100)
					self.lb.bind('<Double-Button-1>', self.select)
					self.lb.bind('<Return>', self.select)
					self.lb.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height())
					self.lb_up = True
				
				self.lb.delete(0, 'end')
				for i in words:
					self.lb.insert('end', i)
			else:
				if self.lb_up: #if the word being typed does not match any entries
					self.var.set('University Not Listed')
					self.lb.focus()
					self.lb.destroy()
					self.lb_up = False
	
	def select(self, event):
		if self.lb_up:
			self.var.set(self.lb.get('active'))
			self.lb.destroy()
			self.lb_up = False
			self.icursor('end')
			
	def up(self, event):
		if self.lb_up:
			#if no entry is selected and up is called, index is last entry
			if self.lb.curselection() == () or self.lb.curselection() == (0,):
				index = str(self.lb.size()-1)
			else:
				index = str(int(self.lb.curselection()[0])-1) #otherwise index is entry above the selected entry
				
			#when index is not last, activate the entry at the index and inactivate the entry below it
			if index != str(self.lb.size()-1):
				self.lb.selection_clear(first=str(int(index)+1))
				self.lb.selection_set(first=index)
				self.lb.activate(index)
				index = str(int(index)-1)
			#if the index is the last one, inactivate the first entry and activate the last entry
			else:
				self.lb.selection_clear(first='0')
				self.lb.selection_set(first=index)
				self.lb.activate(index)
				index = str(int(index)-1)
				
	def down(self, event):
		if self.lb_up:
			#if no entry is selected or the last entry is selected and down is called, index is first entry
			if self.lb.curselection() == () or self.lb.curselection() == (self.lb.size()-1,):
				index = '0'
			else:
				index = str(int(self.lb.curselection()[0])+1) #otherwise index is entry below the selected entry 
			
			#when index is the first entry, inactivate the last entry and activate the first entry
			if index == '0':
				self.lb.selection_clear(first=str(self.lb.size()-1))
				self.lb.selection_set(first=index)
				self.lb.activate(index)
				index = str(int(index)+1)
			#otherwise inactivate previous entry and activate index entry
			else:
				self.lb.selection_clear(first=str(int(index)-1))
				self.lb.selection_set(first=index)
				self.lb.activate(index)
				index = str(int(index)+1)
	
	#compare written characters to previous options
	def compare(self):
		pattern = re.compile('.*' + self.var.get().upper() + '.*') #compile re to re object allowing for match to be used on its elements
		return [i for i in self.entries if re.match(pattern, i)] #takes each character in the string entry and compares it to each character in each note option