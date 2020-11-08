import os
import time

from sendsms import sendsms

# Define server/host ip address
server = '8.8.8.8'

def check_ping(server):

	'''
	Function to ping the server/host and return the result.
	
	'''

	# create a variable that 

	response = os.system("ping -c 1 " + server)

	# Set pingstatus to return a boolean based on the value of response
	if response == 0:
		pingstatus = True
	else:
		pingstatus = False

	return pingstatus


def check_server_status(server):
	'''
		Function to check whether a server or host is available.
		If not, this function will call sendsms defined in sendsms.py to send a text message notification.
		The process will pause for 30 minutes and send another notification if the host is still unreachable.
	'''

	server_status = check_ping(server)

	if server_status != True:
		sendsms()
		while server_status == False: 
			time.sleep(1800)
			if server_status == True:
				break
			else:
				sendsms()



check_server_status(server)


