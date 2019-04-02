#!/usr/bin/python
import requests
import json

api_key_public   = ""
api_key_private  = ""
api_entry_public = "https://api.mailgun.net/v3/address/validate"
api_entry_private= "https://api.mailgun.net/v3/address/private/validate"

list_file   = "./list_check4.txt"
result_file = "./list_check4.result"

def main():
	with open(list_file) as f:
		lines=f.read().splitlines()

	with open(result_file, "x") as output_file:
		num = 0
		for email_address in lines:
			num += 1
			my_dict=get_validate(email_address)

			u = my_dict.get('address', 0)
			r = my_dict.get('is_valid', 0)
			s = my_dict.get('mailbox_verification', 0)

			email_string = str(u) +' ' + str(r) + ' ' + str(s) + '\n'
			print(str(num) + ' ')
			print(email_string)
			output_file.write(email_string)

def get_validate(em):
		r=requests.get(api_entry_private, auth=("api", api_key_private), params={"address": em})
		return r.json()

if __name__ == '__main__':
	main()


