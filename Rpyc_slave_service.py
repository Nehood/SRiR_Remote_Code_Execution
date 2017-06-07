import rpyc
import ast
import os
from rpyc.utils.server import ThreadedServer

class MyService(rpyc.Service):
	
	code = None
	
	def on_connect(self):
		print('Hello new client!')
		return('Succesfully connected to server!')
	pass
	
	def on_disconnect(self):
		print('Goodbye client!')
		return('Succesfully disconnected from server!')
	pass
		
	def exposed_get_answer(self, code):
		self.code = code
		if self.is_valid_python() == True:
			return True
		else:
			return False
	pass
	
	def is_valid_python(self):
		print('Method is_valid_python. {}'.format(self))
		print('Code is: {}'.format(self.code))
		try:
			ast.parse(self.code)
		except SyntaxError:
			print('Code have errors')
			return False
		print('Code is valid')
		return True
	pass
	
	def exposed_execute_code(self):
		return(exec(self.code))
		self.code = None
	pass
	
if __name__ == "__main__":
	thread = ThreadedServer(MyService, hostname = "localhost", port = 18861) #hostname = "localhost" can be probably deleted
	thread.start()