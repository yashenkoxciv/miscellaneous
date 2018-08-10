import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango

import random

class TicTacToeWindow(Gtk.Window):
	def __init__(self, n=3, m=3):
		super().__init__(title='Xs and Os')
		
		self.pane = Gtk.Grid()
		
		self.n, self.m = n, m
		
		self.bs = []
		#self.vs = [-1]*(n*m)
		c = 0
		for i in range(n):
			for j in range(m):
				b = Gtk.Button(label=' ')
				#b.connect('clicked', self.set_stone, {'id': c})
				b.connect('clicked', self.set_stone, c)
				b.modify_font(Pango.FontDescription('Consolas 20'))
				
				self.bs.append(b)
				self.pane.attach(b, i, j, 1, 1)
				
				c += 1
		
		self.add(self.pane)
		
		random.seed()
		
	def set_stone(self, w, data):
		print(data)
		w.set_label('X')
		w.set_sensitive(False)
		
		s = []
		for i in range(self.n*self.m):
			if self.bs[i].get_label() == ' ':
				s.append(i)
		
		rows = []
		c = 0
		for i in range(self.n):
			cr = []
			for j in range(self.m):
				cr.append(self.bs[c].get_label())
				c += 1
			rows.append(''.join(cr))
		
		cols = []
		c = 0
		for i in range(self.m):
			cr = []
			for j in range(self.n):
				cr.append(self.bs[self.m*j+i].get_label())
				c += 1
			cols.append(''.join(cr))
		
		#print('cols:', rows)
		#print('rows:', cols)
		#print(rows.extend(cols))
		is_done = False
		for v in rows:
			if v == 'X'*(self.n) or v == 'X'*(self.m) or v == 'O'*(self.m) or v == 'O'*(self.n):
				print('Done')
				for i in range(self.n*self.m):
					self.bs[i].set_sensitive(False)
				is_done = True
				break
		
		if not is_done:
			if len(s) == 0:
				print('Done [draw]')
			else:
				c = random.choice(s)
				self.bs[c].set_label('O')
				self.bs[c].set_sensitive(False)
			
		
		

w = TicTacToeWindow()
w.connect('destroy', Gtk.main_quit)
w.show_all()
Gtk.main()


