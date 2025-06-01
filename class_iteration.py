class my_iter ():
	def __init__(self,start,end):
		self.start=start
		self.end=end
		
	def __iter__(self):
		return self
		
	def __next__(self):
		while self.start<self.end:
			if self.start%7==0:
				result=self.start
				self.start+=1
				return result
			self.start+=1
		raise StopIteration
		
		
for a in my_iter(1,189):
	print(a)
			
for j in range(5):
	print(5)