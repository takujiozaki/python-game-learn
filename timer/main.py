import datetime

class Timer:
	
	def __init__(self):
		self.timers1 = ''
		self.timers2 = ''
		
	def start_timer(self):
		self.timers1 = datetime.datetime.now()
		
	def end_timer(self):
		self.timers2= datetime.datetime.now()
	
	def get_diff_timer(self):
		diff =self.timers2 - self.timers1
		return diff.seconds
		

# nw1 = datetime.datetime.now()
t = Timer()
t.start_timer()
input('何か入力してください')
t.end_timer()

# nw2 = datetime.datetime.now()
# print((nw2 - nw1).seconds)

print('{}秒でした'.format(t.get_diff_timer()))
