import os
import re
import sys
import time
import requests
from modules import VooCode
from modules.Sublist3r import sublist3r
from beautifultable import BeautifulTable

global version, use, load, b, outputFile, domain, domainOutput, inputFile

version = 'v1.0'

def banner():

	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
	print('''

	
\t \033[1;32;40m『\033[0m\033[1;34;40mV\033[0m\033[1;33;40m』\033[0m\033[1;32;40m『\033[0m\033[1;34;40mo\033[0m\033[1;33;40m』\033[0m\033[1;32;40m『\033[0m\033[1;34;40mo\033[0m\033[1;33;40m』\033[0m\033[1;32;40m『\033[0m\033[1;34;40mB\033[0m\033[1;33;40m』\033[0m\033[1;32;40m『\033[0m\033[1;34;40ma\033[0m\033[1;33;40m』\033[0m\033[1;32;40m『\033[0m\033[1;34;40mr\033[0m\033[1;33;40m』\033[0m {}
		'''.format(version))

def menu():
	while True:
		try:
		
			cmd = input('\033[1;31;40mvoobar\033[0m>').lower()

			if cmd == 'help':
				print('''<USAGE>  subdomain\t-- Use it to find vaild subdomain\n\t scanner\t-- Use it to find vulnerability\n\t exit\t\t-- Use it to exit VooBar''')
			elif cmd == 'subdomain':
				subdomain()
			elif cmd == 'scanner':
				scanner()
			elif cmd == 'exit' or cmd == 'quit':
				sys.exit()
			elif cmd == 'clean' or cmd == 'clear':
					if os.name == 'nt':
						os.system('cls')
						banner()
					else:
						os.system('clear')
						banner()
			else:
				print('[+] \033[1;31;40mCommand is not defined\033[0m [+]')
		except KeyboardInterrupt as e:
			print('\n[+] Type \'\033[1;32;40mexit\033[0m\' or \'\033[1;32;40mquit\033[0m\' to exit [+]')

def subdomain():

		load = None
		inputFile = None
		outputFile = None

		while True:
			try:
				path = input('\033[1;31;40mvoobar\033[0m>\033[1;33;40mmodule\033[0m(\033[1;31;40msubdomain\033[0m)>').lower()
				if path == 'help':
					print('''<USAGE>  show options\t-- Use it to show options\n\t load\t\t-- Use it to load input\n\t output\t\t-- Use it to save output\n\t run\t\t-- Use it to start this tool\n\t back\t\t-- Use to go back menu\n\t find\t\t-- Use it for subdomain enumeration ''')
				elif path == 'run':
					try:
						
						if inputFile != None and outputFile != None:

							with open(inputFile, 'r') as f:
								fill = f.read().rstrip('\n')

							with open('temp.txt', 'w') as f:
								f.write(re.sub(r'(?m)$', r'/', fill))
								f.close()


							f = open('temp.txt', 'r')

							try:
								for i in f:
									if '://' in i:
										try:
											s = i.split('/')
											load = s[2]

										except:
											load = i
									elif '/' in i:
										try:
											a = i.split('/')
											load = a[0]
										except:
											try:
												s = i.split('/')
												load = s[2]

											except:
												load = i
									else:
										load = i

									VooCode.VooCode('http://'+load,outputFile)
								f.close()
								time.sleep(3)
								os.remove('temp.txt')
							except:
								print('error')
							

							
						else:
							print('[+] \033[1;31;40mBoth parameter is required\033[0m [+] ')

					except:
						print('[+] \033[1;32;40mSet valid file to start\033[0m [+]')

					
				

					
				elif 'load' in path:
					a = path.split(' ')
					inputFile = a[1]
					print('Load > '+inputFile)
				elif 'output ' in path:
					c = path.split(' ')
					outputFile = c[1]
					print('Output > '+outputFile)

				elif 'find' in path:
						
					try:
						d = path.split(' ')
						domain = d[1]
						try:
							domainOutput = d[2]
						except:
							domainOutput = None
						if domainOutput!= None:
							
							subdomains = sublist3r.main(domain, None, domainOutput, ports= None, silent=False, verbose= False, enable_bruteforce= False, engines=None)
						else:
							print('[+] Both parameter is required [+]')
					except:
							print('[+] \033[1;32;40mfind <domain> <output>\033[0m [+] \n[+] \033[1;32;40mEG: find google.com google.txt\033[0m [+]')
				

				elif path == 'show options':
					table = BeautifulTable()
					table.append_row(['Load', inputFile])
					table.append_row(['Output',outputFile])
					print(table)
				elif path == 'back':
					menu()
				elif path == 'clean' or path == 'clear':
					if os.name == 'nt':
						os.system('cls')
						banner()
					else:
						os.system('clear')
						banner()
				else:
					print('[+] \033[1;31;40mCommand not defined\033[0m [+]')
			except KeyboardInterrupt as e:
				print('\n[+] use \'\033[1;32;40mback\033[0m\' to enter in menu [+]')

def scanner():
	while True:
		try:
			cmd = input('\033[1;31;40mvoobar\033[0m>\033[1;33;40mmodule\033[0m(\033[1;31;40mscanner\033[0m)>').lower()

			if cmd == 'back':
				menu()
			elif cmd == 'help':
				print('<Modules>\t back\t\t -- Use it go back in menu\n\t\t corsfinder\t -- Use it to find cors vulnerability [ \033[1;32;40mAutomatic\033[0m ]\n\t\t clickjacker\t -- Use it to find clickjacking vulnerability [ \033[1;32;40mAutomatic\033[0m ]')
			elif cmd == 'clickjacker':
				clickjacker()
			elif cmd == 'corsfinder':
				corsfinder()
			elif cmd == 'clean' or cmd == 'clear':
				if os.name == 'nt':
					os.system('cls')
					banner()
				else:
					os.system('clear')
					banner()
			else:
				print('[+] \033[1;31;40mCommand not defined\033[0m [+]')


		except KeyboardInterrupt as e:
			print('\n[+] use \'\033[1;32;40mback\033[0m\' to enter in menu ')

def clickjacker():

	use  = None
	load = None

	while True:
		try:
			cmd =  input('\033[1;31;40mvoobar\033[0m>\033[1;33;40mmodule\033[0m(\033[1;31;40mscanner\033[0m)[\033[1;33;40mclickjacker\033[0m]>').lower()
			if cmd == 'back':
				scanner()
			elif cmd == 'help':
				print('\033[1;31;40m[+]\033[0m load\t-- Use it load URL list to find vulnerability \n\033[1;31;40m[+]\033[0m use\t\t-- Use it to find vulnerability in sigle URL\n\033[1;31;40m[+]\033[0m run\t\t-- Use it to start finding')
			elif 'load' in cmd:
				try:
					load = cmd.split(' ')
					load = load[1]
					print('Load > '+load)
				except:
					print('[+] <USAGE> load <filename> [+]\n[+] EG: load URL.txt [+]')
			elif cmd == 'show options':

				table = BeautifulTable()
				table.append_row(['load', load])
				table.append_row(['use',use])
				print(table)

			elif 'use' in cmd:
				try:
					use = cmd.split(' ')
					use = use[1]
					print('Use > '+use)
				except:
					print('[+] <USAGE> use <URL> [+]\n[+] EG: use google.com [+]')
			elif cmd == 'run':
				if use != None and load != None:
					print('[+] You can\'t use both options together [+]')
				elif load != None:

					col_width = 40

					with open(load, 'r') as f:
						fill = f.read().rstrip('\n')

					with open('temp.txt', 'w') as f:
						f.write(re.sub(r'(?m)$', r'/', fill))
						f.close()


					f = open('temp.txt', 'r')

					try:
						for i in f:
							if '://' in i:
								try:
									s = i.split('/')
									load = s[2]

								except:
									load = i
							elif '/' in i:
								try:
									a = i.split('/')
									load = a[0]
								except:
									try:
										s = i.split('/')
										load = s[2]

									except:
										load = i
							else:
								load = i
							x = requests.get('http://'+load)
							if 'x-frame-options' not in str(x.headers).lower():

								print("+"+"-"*col_width+"-"+"-"*col_width+"+")
								
								print("|"+'\033[1;32;40mvulnerable\033[0m'.center(col_width)+" >> "+load.center(col_width))

								print("+"+"-"*col_width+"-"+"-"*col_width+"+")

							else:
								print("+"+"-"*col_width+"-"+"-"*col_width+"+")
								print("|"+'\033[1;31;40mnot vulnerable\033[0m'.center(col_width)+" >> "+load.center(col_width))
								print("+"+"-"*col_width+"-"+"-"*col_width+"+")

					except:
						print('[+] Something went wrong [+]')
						sys.exit()

					load = None
					f.close()
					time.sleep(3)
					os.remove('temp.txt')
					
				elif use != None:
					if '://' in use:
						a = use.split('://')
						a = a[1]
						
					else:
						a = use
					x = requests.get('http://'+a)
					if 'x-frame-options' not in str(x.headers).lower():

						print('[+] \033[1;32;40mWebsite is vulnerable\033[0m [+]')
					else:

						print('[+] \033[1;31;40mWebsite is not vulnerable\033[0m [+]')
				else:
					print('someting went wrong')
				

			elif cmd == 'clean' or cmd == 'clear':
				if os.name == 'nt':
					os.system('cls')
					banner()
				else:
					os.system('clear')
					banner()
			else:
				print('[+] \033[1;31;40mCommand not defined\033[0m [+]')


		except KeyboardInterrupt as e:
			print('\n[+] use \'\033[1;32;40mback\033[0m\' to enter in menu ')

def corsfinder():
	
	load = None
	use = None

	while True:
		try:
			cmd = input('\033[1;31;40mvoobar\033[0m>\033[1;33;40mmodule\033[0m(\033[1;31;40mscanner\033[0m)[\033[1;33;40mcorsfinder\033[0m]>').lower()

			if cmd == 'back':
				scanner()
			elif cmd == 'help':
				print('\033[1;31;40m[+]\033[0m load\t-- Use it load URL list to find vulnerability \n\033[1;31;40m[+]\033[0m use\t\t-- Use it to find vulnerability in sigle URL\n\033[1;31;40m[+]\033[0m run\t\t-- Use it to start finding')
			elif 'load' in cmd:
				try:
					a = cmd.split(' ')
					load = a[1]
					print('Load > '+load)
				except:
					print('[+] <USAGE> load <filename> [+]\n[+] EG: load URL.txt [+]')

			elif 'use' in cmd:
				try:
					b = cmd.split(' ')
					use = b[1]
					print('Use > '+use)
				except:
					print('[+] <USAGE> use <URL> [+]\n[+] EG: use google.com [+]')

			elif cmd == 'show options':

				table = BeautifulTable()
				table.append_row(['load', load])
				table.append_row(['use',use])
				print(table)

			elif cmd == 'run':
				if load != None and use != None:
					print('[+] You can\'t use both options together [+]')

				elif load != None:

					with open(load, 'r') as f:
						fill = f.read().rstrip('\n')

					with open('temp.txt', 'w') as f:
						f.write(re.sub(r'(?m)$', r'/', fill))
						f.close()


					f = open('temp.txt', 'r')

					try:
						for i in f:
							if '://' in i:
								try:
									s = i.split('/')
									load = s[2]

								except:
									load = i
							elif '/' in i:
								try:
									a = i.split('/')
									load = a[0]
								except:
									try:
										s = i.split('/')
										load = s[2]

									except:
										load = i
							else:
								load = i

							payload = 'https://'+load+'.evil.com'
							header = {'Origin':payload}
							try:
								col_width = 40 
								x = requests.get('http://'+load+'/', headers=header)
								if '\\\'access-control-allow-origin\\\': '+'\\\''+payload+'\\\'' and  'access-control-allow-credentials' in str(x.headers).lower():

									msg = '\033[1;32;40mtarget is vulnerable\033[0m'
									print("+"+"-"*col_width+"+"+"-"*col_width+"+")
									print("|"+load.center(col_width)+"|"+msg.center(col_width))
									print("+"+"-"*col_width+"+"+"-"*col_width+"+")
								else:
									msg = '\033[1;31;40mtarget is not vulnerable\033[0m'
									print("+"+"-"*col_width+"+"+"-"*col_width+"+")
									print("|"+load.center(col_width)+"|"+msg.center(col_width))
									print("+"+"-"*col_width+"+"+"-"*col_width+"+")
							except Exception as e:
									print('[+] Someting went wrong [+]')
									sys.exit()
					except KeyboardInterrupt:
							print('[+] aborted by user [+] ')

					load = None

					f.close()
					time.sleep(3)
					os.remove('temp.txt')
				
				elif use != None:
					#Access-Control-Allow-Origin: https://attacker.com Access-Control-Allow-Credentials: true
					if '://' in use:
						s = use.split('/')
						use = s[2]
					else:
						s = use.split('/')
						use = s[0]

					payload = 'http://'+use+'.evil.com'
					header = {'Origin': payload}
					try:
						x = requests.get('http://'+use, headers=header)
						if '\\\'access-control-allow-origin\\\': '+'\\\''+payload+'\\\'' and  'access-control-allow-credentials' in str(x.headers).lower():
							print('[+] \033[1;32;40mtarget is vulnerable\033[0m [+]')
						else:
							print('[+] \033[1;31;40mtarget is not vulnerable\033[0m [+]')
					except:
						print('[+] Someting went wrong try again [+]')

				else:
					print('[+] You should set at least one parameter i.e : \033[1;32;40mload\033[0m or \033[1;32;40muse\033[0m [+] ')
				

			elif cmd == 'clean' or cmd == 'clear':
				if os.name == 'nt':
					os.system('cls')
					banner()
				else:
					os.system('clear')
					banner()
			else:
				print('[+] \033[1;31;40mCommand not defined\033[0m [+]')


		except KeyboardInterrupt as e:
			print('\n[+] use \'\033[1;32;40mback\033[0m\' to enter in menu ')

def checkingUpdate():

	url = 'http://amanrawat.000webhostapp.com/voobar/check.php'

	try:
		print('\t \033[1;32;40mChecking for update, please wait... \033[0m  ')
		time.sleep(3)
		x = requests.get(url).text
	except:
		print('[+] \033[1;31;40mFailed to connect \033[0m [+]')
		sys.exit()

	if version == x:
		pass
		if os.name == 'nt':
			os.system('cls')
			banner()
	
		else:
			os.system('clear')
			banner()

	else:
		print('\033[1;31;40mvoobar\033[0m>  [+] \033[1;32;40mYeah! voobar {} is available. \033[0m ( \033[1;31;40mUpdate required!\033[0m )\n\t [+] \033[1;32;40mUpdate to latest version for more features.\033[0m'.format(x))
		sys.exit()

banner()

checkingUpdate()

menu()


	