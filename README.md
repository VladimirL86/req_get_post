# Sending http requests
* This program sends GET request to URL.  
* Processes recieved data.  
* Logs the results in file.  
* Sends the results in POST request to URL.

## Requirements
* OS: Linux  
* Pytnon 3 with libraries:  
    * sys  
    * requests  
    * subprocess  
    * os  
    * time  
    * setuptools


## Make sdist
1. Download files from repository and unzip.  
1. Run `python3 setup.py sdist` in directory with files. 


## Install
1. Go to /dist in directory with files.   
1. Extract files from `*.tar.gz` in this directory.  
1. Go to directory with extracted files.  
1. Run `python3 setup.py install`.


## Usage
Run `req_get_post.py https:// ... /api`.  

Log will be saved in `/usr/local/bin/requests_log.txt`  
Examples of log format:  
`Sun Mar  3 19:29:31 2019 : whoami : b'root\n'`  
`Mon Mar  4 10:21:58 2019 : wrong_command : error`  
