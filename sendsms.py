from twilio.rest import Client

# Access Twilio account using Account SID and Auth Token
client = Client("", "")


def sendsms():
	# Define to phone and from phone numbers and add body to send as text message
	client.messages.create(
						to="", 
						from_="", 
						body="",
						)
