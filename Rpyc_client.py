import rpyc
import sys

try:
	arg = sys.argv[1]
except IndexError:
	print('Proper usage of script: python Rpyc_client.py IP_Address')
	sys.exit(1)
	
conn = rpyc.connect(sys.argv[1], 18861)
code = open('python_code.txt', 'r')
if conn.root.get_answer(code.read()) == True:
	print('Code can be compiled successfully!')
	print('Result of executing sent code:')
	print(conn.root.execute_code())
else:
	print('Errors in Code!')