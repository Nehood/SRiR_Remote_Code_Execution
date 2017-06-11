from nose.tools import *
from Remote_Code_Execution.Rpyc_slave_service import MyService
import rpyc
import os
import time
import sys

FILE_PATH = 'Received_codes'
SERVER_DIRECTORY = os.getcwd() + '\Remote_Code_Execution\Rpyc_slave_service localhost'
SERVER_IP_ADDRESS = 'localhost'
PORT = 18861

def setup():
	os.system('start cmd /c {}'.format(SERVER_DIRECTORY)) #if server won't start, no tests will pass
	time.sleep(1)
	print('SETUP!')

def teardown():
	print('TEAR DOWN!')
	
def test_bad_code():
	conn = rpyc.connect(SERVER_IP_ADDRESS, PORT)
	res = conn.root.send_and_check_code('print "hello world!"')
	assert_equal(res, False)
	
def test_good_code():
	conn = rpyc.connect(SERVER_IP_ADDRESS, PORT)
	res = conn.root.send_and_check_code('print(\'hello world!\')')
	assert_equal(res, True)
	
def test_code_return():
	code = open("tests/python_code1.txt", 'r')
	conn = rpyc.connect(SERVER_IP_ADDRESS, PORT)
	conn.root.send_and_check_code(code.read())
	res = conn.root.execute_code()
	code.close()
	assert_equal(res, 'Wielki sukces!')