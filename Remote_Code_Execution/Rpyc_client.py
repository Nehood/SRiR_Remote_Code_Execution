import rpyc
import sys
import time

PORT = 18861

try:
	arg = sys.argv[1]
except IndexError:
	print('Proper usage of script: python Rpyc_client.py IP_Address')
	sys.exit(1)
	
conn = rpyc.connect(sys.argv[1], PORT)
code = open('python_code.txt', 'r')
if conn.root.send_and_check_code(code.read()) == True:
	print('Code can be compiled successfully!')
	print('Result of executing sent code:')
	print(conn.root.execute_code())
	print(conn.root.compare_codes())
	conn.close()
else:
	print('Errors in Code!')
code.close()


