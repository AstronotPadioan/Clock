from time import sleep, strftime, time
from datetime import datetime
import sys
import os
import time

task = input('What do you want to do? Type a if set a clock, b if set an alarm: ')

class clock:
	def auto_clock(self):
		os.system('clear')
		clock_type = input('12hr or 24hr-clock?: ')
		if clock_type == '12':
			mer = input('am/pm?: ')
		os.system('clear')
		if clock_type == '24':
			while True:
				now = datetime.now()
				print(now.strftime("%H:%M­:%S"), end = "\r", flush=True)
				sleep(1)
		else:
			while True:
				now = datetime.now()
				print(now.strftime("\r%I:%M­:%S "), end= mer, flush=True)
			
				sleep(1)
	def set_clock(self):
		os.system('clear')
		clock_type = input('12hr or 24hr?: ')
		if clock_type == '12':
			ap = input(('am or pm?: '))
		else:
			ap = ''
		h = int(input('Hour: '))
		m = int(input('Minute: '))
		s = int(input('Second: '))
		os.system('clear')
		while True:
			sys.stdout.write(f'\r{h:0>2}:{m:0>2}:{s:0>2}' + ' ' + ap)
			sleep(1)
			sys.stdout.flush()
			s += 1
			if s >= 60:
				m += 1
				s = 0
			if m >= 60:
				h += 1
				m = 0
			if clock_type == '24':
				if h >= 24:
					h = 0
			else:
				if h >= 12:
					h = 0
	def ready(self):
		os.system('clear')
		set_up = input('automatic or not?: ')
		os.system('clear')
		if set_up == 'a':
			vae.auto_clock()
		if set_up == 'n':
			vae.set_clock()
  

def alarm_clock():
  os.system('clear')
  h = int(input('Set an alam hour: '))
  m = int(input('Set an alarm minute: '))
  os.system('clear')
  q = datetime.now()
  while True:
    if h == q.hour and m == q.minute:
    	print('Wake up now!')
    	break
  print('You woke up.')
  
vae = clock()

if task == 'a':
	vae.ready()
if task == 'b':
	alarm_clock()