import subprocess

from sendsms import sendsms

# Define server/host ip address
server = '8.8.8.8'

def check_ping(server):

	'''
	Function to ping the server/host.
	
	This uses the subprocess module, which allows you to spawn new processes, 
	connect to their input/output/error pipes, and obtain their return codes.
	'''

	# Define a command and convert it into list format
	command = ("ping -c 1 " + server).split()

	# Run external program (in this case, ping) using subprocess module and its Popen() function
	# FYI: The P stands for Process
	# We pipe the output of subprocess.Popen() to stdout or stderr (depending on the outcome of the ping command)
	process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	# And we use the communicate method to return both the stdout and stderr
	stdout, stderr = process.communicate()
	# The return code will either be 0 if there is a ping reply or 1 if there isn't
	# We store the return code (either 0 or 1) in 
	response = process.returncode

	# Set pingstatus to return a boolean based on the result of the returncode
	if response == 0:
		pingstatus = True
	else:
		pingstatus = False

	return pingstatus


def check_server_status(server):
	'''
		Function to check whether a server or host is available
		If not, this function will call sendsms defined in sendsms.py to send a text message notification
	'''

	server_status = check_ping(server)

	if server_status != True:
		sendsms()


check_server_status(server)






