import configparser
import getpass
import cx_Oracle # requirement
import typing

def connect(connection_name: str) -> cx_Oracle.Connection:
	"""returns an Oracle connection by reading a config file in your F drive"""
	config = configparser.ConfigParser()
	config.read(f'F:/{connection_name}.ini')
	details = config['details']
	dsn_tns = cx_Oracle.makedsn(details['hostname'], details['port'], service_name=details['service_name'])
	return cx_Oracle.connect(user=details['username'], password=details['password'], dsn=dsn_tns)

def create_config(connection_name:str,username:str='prompt',password:str='prompt') -> None:
	""" creates a config file and saves to F drive with connection_name specified (first arg) and prompts for a username and password by default
		paramaters:
			connection_name: str (required)
				the name of the resulting config file saved to F
			username: str (optional)
				the user's exadw username
				if "prompt" will prompt for username
				if empty str, will write without that parameter specified
				if any other str, will use that as the username
			password: str (optional)
				the user's exadw password
				if "prompt" will prompt for password
				if empty str, will write without that parameter specified
				if any other str, will use that as the password
	"""
	config = configparser.ConfigParser()
	config.read(r'H:\Common\ExadataExampleConfig\EXADW_example.ini')

	if username == 'prompt':
		username = input('Exadw username (with proxy): ')
	if password == 'prompt':
		password = getpass.getpass('Exadw password: ')

	config['details']['username'] = username
	config['details']['password'] = password

	config.write(open(f'F:/{connection_name}.ini','w'))
	print(f'successfully wrote {connection_name} to F drive')
