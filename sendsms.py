from twilio.rest import Client

# Access Twilio account using Account SID and Auth Token
client = Client("AC48bc55917ac176889839e430d151e0e4", "ab5b4c8d5f0835fc9e7a9a8aa50bd2db")


def sendsms():
	# Define to phone and from phone numbers and add body to send as text message
	client.messages.create(
						to="", 
						from_="", 
						body="",
						)
