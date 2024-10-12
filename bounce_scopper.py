from keys import EmailAuth, CloudFlareR2
from imap_tools import MailBox
from CFR2.CFR2API import CloudflareR2API as r2_api
from providers import look_up
from number_carrier import phone_carrier
import random
from helpers.csv_helper import grab_numbers_and_emails
from time import sleep
# Initialize Cloudflare R2 API
r2 = r2_api(
	CloudFlareR2.r2_token,
	CloudFlareR2.r2_id,
	CloudFlareR2.r2_key,
	CloudFlareR2.r2_endpoint,
	CloudFlareR2.r2_bucket
)

def check_progress(phone_listings):
	"""
	Prints the count of phone listings with fewer than 3 providers.
	"""
	counter = 0
	for i in range(len(phone_listings)):
		counter += 1
	print(counter)

def check_progress_2(phone_listings):
	vw = 0
	tmb = 0
	uscel = 0
	att = 0
	unknow = 0
	used = 0
	total_w_p = 0

	print(vw, tmb, uscel, att, unknow, " used this month", used)
	print(total_w_p, "total with providers")

	
def read_emails():
	"""
	Reads emails to find numbers to remove emails with stop, also delets read emails.
	Returns a list: numbers to remove and bad numbers found.
	"""
	remove_from_list = []
	delete_read_list = []
	email_list = [
		"furniture-distributors-goldsboro-nc@threadedmessage.com",
		"furniture-distributors-nc@threadedmessage.com",
		"furniture-distributors-greenville@threadedmessage.com",
		"furniture-distributors-252@threadedmessage.com",
		"furniture-distributors-eastern-nc@threadedmessage.com",
		"furniture-distributors-enc@threadedmessage.com",
		"furniture-distributors-pitt@threadedmessage.com"
	]
	for email in email_list:
     
		with MailBox(EmailAuth.email_imap_host).login(email, EmailAuth.email_passwd, "INBOX") as mb:
			for msg in mb.fetch(limit=5000, reverse=True, mark_seen=False):
				stop_check = msg.text[:10]

				if "re:" in msg.subject.lower():
					print("stop", stop_check)
					if "stop" in stop_check.lower():
						number_to_remove = msg.from_.split("@")[0]
						remove_from_list.append(number_to_remove)
						print("stop", number_to_remove)

				elif "Undelivered" in msg.subject:
					number_starting_point = msg.text.split("<")[1]
					number_choped = number_starting_point.split("@")[0]
					remove_from_list.append(number_choped)
					print("Undelivered",number_choped)
				elif "" == msg.subject and "Message" in stop_check:
					number_starting_point = msg.text.split("Message to")[1]
					number_choped = number_starting_point.split("@")[0]
					remove_from_list.append(number_choped)
					print("Undelivered-2", number_choped)
				delete_read_list.append(msg.uid)

			mb.delete(delete_read_list)

	return remove_from_list


def restructure_list(modded_list: list, current_list: list, stop_remove_list: list):
	for listed_number in current_list:
		if listed_number not in modded_list and listed_number["phone"] not in stop_remove_list:
			modded_list.append(listed_number)
			
	return modded_list
	# restrures the list, so any 
	

def read_valid_list():
	"""
	Reads the list of valid phone numbers from Cloudflare R2.
	Returns the list of valid phone numbers.
	"""
	return r2.read_r2_object("phone-list/gv-list")["results"]

def update_list(modded_list):
	"""
	Updates the list of valid phone numbers in Cloudflare R2.
	"""
	r2.put_json_object(modded_list, "phone-list/gv-list")

def validate_number(current_list, stop_remove_list: list = []):
	"""
	Validates and updates the list of phone numbers based on found bad providers and stop requests.
	Returns the modified list of phone numbers.
	"""
	modded_list: list = current_list.copy()

	for listed_number in current_list:
		# check if the provider
		if listed_number["provider"] == None:
			listed_number_index = modded_list.index(listed_number)
			phone_number = listed_number["phone"]

			if len(phone_number) == 10:

				responce = phone_carrier(phone_number)

				if responce["status"] == "success" and responce["results"]["line_type"] == "mobile":
					provider_named= responce["results"]["carrier"]

					modded_list[listed_number_index]["provider"] = (provider_named)
					sleep(.5)
				else:
					print("bad number")
					modded_list.remove(listed_number)
			else:
				print("bad number")
				modded_list.remove(listed_number)
		else:
			print("prvoder for number exist")
		

	for entry in current_list:
		if entry['phone'] in stop_remove_list:
			modded_list.remove(entry)

	return modded_list

if __name__ == '__main__':
	#json_list = grab_numbers_and_emails()
	#print(len(json_list))
	#modded_list = validate_number(json_list)
	#print(len(modded_list))
	#update_list(modded_list)
	
	get_list = read_valid_list()
	current_list = get_list
	check_progress(current_list)
	check_progress_2(current_list)
	print(len(current_list), "total numbers")
	stop_remove_list = read_emails()
	modded_list = validate_number(current_list, stop_remove_list)
	restruc_luist = restructure_list(modded_list, current_list, stop_remove_list)
	print(len(restruc_luist),"new", len(current_list), "old")
	
	update_list(restruc_luist)
