import sys
import requests
import subprocess
import os
import time


#GET request
URL = sys.argv[1] + "/commands"
PARAMS = {'aim': 'python_developer_job'}
r = requests.get(url = URL, params = PARAMS)
info = r.json()
command = info['data']


#processing
if command == 'wrong_command':
    result = 'error'
else:
    result = subprocess.check_output(command.split())


#logging
if not os.path.isfile('/usr/local/bin/requests_log.txt'):
    filehandle = open('/usr/local/bin/requests_log.txt', 'w')
else:
    filehandle = open('/usr/local/bin/requests_log.txt', 'a')
filehandle.write(time.asctime() + ' : ')
filehandle.write(command + ' : ' + str(result) + '\n')
filehandle.close()


#POST request
API_ENDPOINT = sys.argv[1] + "/commands"
DATA = {'command': command, 'result': str(result)}
requests.post(url = API_ENDPOINT, data = DATA)

