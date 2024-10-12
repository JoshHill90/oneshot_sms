import email, smtplib, ssl
from providers import PROVIDERS, level_1_providers
from keys import EmailAuth
import re
from time import sleep
from email.message import EmailMessage
import csv
import random
from bounce_scopper import read_valid_list, update_list

carri = [
	"AT&T",
	"Boost Mobile",
	"Cricket Wireless",
	"Consumer Cellular",
	"Metro PCS",
	"Mint Mobile",
	"T-Mobile",
	"Verizon",
]

class SMSSender:
	def __init__(self) -> None:
		self.subject: str = "Furniture Distributors Goldsboro"
		self.smtp_server: str = EmailAuth.email_host
		self.smtp_port: int = EmailAuth.email_port

		self.email_list = [
			"furniture-distributors-goldsboro-nc@threadedmessage.com",
			"furniture-distributors-nc@threadedmessage.com",
			"furniture-distributors-greenville@threadedmessage.com",
			"furniture-distributors-252@threadedmessage.com",
			"furniture-distributors-eastern-nc@threadedmessage.com",
			"furniture-distributors-enc@threadedmessage.com",
			"furniture-distributors-pitt@threadedmessage.com"
		]

  
	def send_sms_via_email(self, number: str, message: str, provider: str, email_counter):

			
		try:
			# Create the email message
			email_message = EmailMessage()
			email_message['Subject'] = self.subject
			email_message['From'] = self.email_list[email_counter]
			email_message.set_content(message)
			print("from :", self.email_list[email_counter])
			# For BCC, recipients are added here
			email_message['To'] = f"{number}@{PROVIDERS.get(provider)['sms']}"
			
			# Send the email via SMTP
			context = ssl.create_default_context()
			with smtplib.SMTP(self.smtp_server, self.smtp_port) as email:
				email.ehlo()
				email.starttls(context=context)
				email.login(self.email_list[email_counter], EmailAuth.email_passwd)
				email.send_message(email_message)
				email.quit()
			email_counter +=1
			print(email_counter)
		except Exception as e:
			print("error",e)

		return

message = r"""***𝐏𝐔𝐁𝐋𝐈𝐂 𝐍𝐎𝐓𝐈𝐂𝐄***
𝐀𝐓 𝐅𝐔𝐑𝐍𝐈𝐓𝐔𝐑𝐄 𝐃𝐈𝐒𝐓𝐑𝐈𝐁𝐔𝐓𝐎𝐑𝐒 𝐈𝐍 𝐆𝐑𝐄𝐄𝐍𝐕𝐈𝐋𝐋𝐄, 𝐍𝐂— Join us as our 𝐕𝐈𝐏 𝐠𝐮𝐞𝐬𝐭𝐬 for incredible 
savings! With up to $𝟏 𝐌𝐈𝐋𝐋𝐈𝐎𝐍 𝐃𝐎𝐋𝐋𝐀𝐑𝐒 in inventory that 
must be 𝐈𝐌𝐌𝐄𝐃𝐈𝐀𝐓𝐄𝐋𝐘 𝐄𝐋𝐈𝐌𝐈𝐍𝐀𝐓𝐄𝐃, we’re slashing prices STOREWIDE! 
Don’t miss out on these 𝐌𝐀𝐒𝐒𝐈𝐕𝐄 𝐃𝐈𝐒𝐂𝐎𝐔𝐍𝐓𝐒 — tell your friends and family, 
and bring your trucks and trailers. 𝐖𝐞'𝐫𝐞 𝐨𝐟𝐟𝐞𝐫𝐢𝐧𝐠 𝟐𝟒 𝐦𝐨𝐧𝐭𝐡𝐬 𝐝𝐞𝐟𝐞𝐫𝐫𝐞𝐝 𝐢𝐧𝐭𝐞𝐫𝐞𝐬𝐭 
(no interest if paid in full within 24 months) and we pay your delivery. Act fast, this offer won’t last
long! Deals on through the 14th. Credit approval and minimum purchase required.

reply stop be removed from the list

"""

def main():

	number_listing = read_valid_list()
	modded_number_listing = number_listing.copy()
	print(len(modded_number_listing))
	counter = 0
	index = 0
	email_counter = 0	
	while counter < 200:
		random_seconds = random.randint(60, 150)

		
		if email_counter == 7:
			email_counter = 0
		if number_listing[index]["provider"] != None and number_listing[index]["used"] == False:
			
			number = number_listing[index]["phone"]
			provider = number_listing[index]["provider"]
   
			SMSSender().send_sms_via_email(number=number, provider=provider, message=message, email_counter=email_counter)
			
			print('sent to', number, ", with Provider as", provider)
			sleep(20)
			modded_number_listing[index]["used"] = True
			counter +=1
			sleep(random_seconds)
		index += 1
		email_counter += 1
		
	update_list(modded_number_listing)
if __name__ == "__main__":
	main()

#number_listing = [{
#     'id': 1884, 
#     'name': 'Josh Hill', 
#     'phone': '2523679568', 
#     'providers': [
#         	"T-Mobile USA Inc."
#		], 
#     'email': '', 
#     'silk_id': 'FDGB01', 
#     'level': 1, 
#     'checked_this_month': False
#	}, {
#     'id': 1882, 
#     'name': 'Cass Hill', 
#     'phone': '9195200383', 
#     'providers': [
#         	"T-Mobile USA Inc."
#		], 
#     'email': '', 
#     'silk_id': 'FDGB01', 
#     'level': 1, 
#     'checked_this_month': False
#	},]