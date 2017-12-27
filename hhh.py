#!/usr/bin/env python2
import argparse
import requests

parser = argparse.ArgumentParser(description='Check headers for target web site.')
parser.add_argument('-t','--target',dest='target',type=str,help='target')
args = parser.parse_args()

def CheckHeader(headers,search):
    if search in headers:
        return search+": "+headers[search]
    return False

def RetrieveHeader(target):
    headers = requests.get(target).headers
    return headers
    
searchlist = ['X-Frame-Options','Content-Security-Policy','Strict-Transport-Security','X-Content-Type-Options','X-XSS-Protection','Referrer-Policy']
try:
    headers = RetrieveHeader(args.target)
    print "Getting Headers for: "+args.target+"\n"
except:
    raise ValueError('Error retrieving URL, verify your URL is valid')
for search in searchlist:
    c = CheckHeader(headers,search)
    if c:
        print "\033[1m\033[32m[+] \033[0m"+c.strip()+"\033[1m\033[32m (OK)"
    else:
        print "\033[1m\033[31m[-] \033[0m"+search+":\033[1m\033[31m (Missing)"

print "\n\033[0mDone."