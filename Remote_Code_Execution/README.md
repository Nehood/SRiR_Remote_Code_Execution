# SRiR_Remote_Code_Execution
Remote code executions using python library for RPC(Remote Procedure Call) - Python RPYC

Requirements:
	Python version 3.6.0
	pip version 9.0.1
	RPYC version 3.4.0
	nosetests 1.3.7 (for testing purposes)
	
How to install:
	Download latest version of python from https://www.python.org/
	Follow instructions from RPYC official website - https://rpyc.readthedocs.io/en/latest/#
	To install nosetests simply write in command line pip install nosetests
	
How to use:
	Run Rpyc_slave_service.py on server machine via command line -> python Rpyc_slave_service.py <IP_address_of_server_machine>
	On client(s) machine run from command line using: python Rpyc_client.py <IP_address_of_server_machine>
	
How it works:
	Client program sends code written in python_code.txt (must be written in similar fashion, i.e. must store result in
	temporary file) to the server, where it's checked for code errors. If none are found, code is executed and the result
	is sent back to the client. Additonally the server stores codes sent from all clients (within running session), and
	compares them with latest code being sent. As result, information whether codes are the same or have differences
	are sent back to the client.
	
How to run test campaign:
	while in main project folder (NOT THE tests FOLDER!) simply execute nosetests command.