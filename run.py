#BING HUNTER V1
#Change Or Edit Author COPYRIGHT Never Make You Coder, Don't Be A Bastard Dude!
#Coded By Wissem Mahfoud
#I Accept All Responsibility For Any Illegal Usage.
#Owner-TN
import threading
from multiprocessing.dummy import Pool
import os,sys,time
from bs4 import BeautifulSoup
from platform import system
import random
import datetime
import cookielib
import os
import re
from colorama import Fore								
from colorama import Style								
from colorama import init												
import requests, re, os, base64;
import urllib, httplib, urllib2
from multiprocessing.dummy import Pool as ThreadPool
try:
    os.system('title BING HUNTER V1')
except:
    pass
def clean():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
    else:
        pass
########### COLOR ############ 
fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE	
fy  =   Fore.YELLOW										
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT										
##############################  

print ('''{}{}
 

   _____ ______      _______ _____        __  ___  
  / ____/ __ \ \    / /_   _|  __ \      /_ |/ _ \ 
 | |   | |  | \ \  / /  | | | |  | |______| | (_) |
 | |   | |  | |\ \/ /   | | | |  | |______| |\__, |    BING HUNTER V1
 | |___| |__| | \  /   _| |_| |__| |      | |  / /     CODED BY WISSEM MAHFOUD
  \_____\____/   \/   |_____|_____/       |_| /_/      THINK TWICE, CODE ONCE 
                                                    
''').format(fr,sb)
now = datetime.datetime.now()
print('\n\033[92m                        STARTED AT: ' + str(now))
print('\n\033[92m ./Select:')
print ('''{}{}
[1] BING DORKER
[2] BING GRABBER
[3] IP RANGE
''').format(fy,sb)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
lucifer = raw_input((('{}{}[!] Number: ').format(fr,sb)))
if str(os.path.exists('COVID-19')) == 'False':
    os.system('mkdir COVID-19')

if lucifer =='1':
	dorks = raw_input("\n\033[92m[!]\033[91m WELCOME TO HELL ENTER LIST OF DORKS : ")
	dorks = open(dorks, 'r')
	for louis in dorks:
		ch = []
		page = 1
		while page < 2000:
			bing = "http://www.bing.com/search?q="+louis+"+&count=50&first="+str(page)
			select = requests.get(bing,verify=False,headers=headers)
			fwd = select.content
			doork = re.findall('<h2><a href="(.*?)"', fwd)
			for i in doork:
				o = i.split('/')
				if (o[0]+'//'+o[2]) in ch:
					print '\n\033[92m[DORK]: \033[91m',(louis)
					pass
				else:
					ch.append(o[0]+'//'+o[2])
					print '\033[00m',(o[0]+'//'+o[2])
					with open('COVID-19/From-Dorks.txt', 'a') as s:
						s.writelines((o[0]+'//'+o[2])+'\n')
			page = page+50
if lucifer =='2':
	ips = raw_input("\n\033[92m[!]\033[91m WELCOME TO HELL ENTER LIST OF IPS : ")
	ips = open(ips, 'r')
	for louis in ips:
		ch = []
		page = 1
		while page < 2000:
			bing = "http://www.bing.com/search?q="+louis+"+&count=50&first="+str(page)
			select = requests.get(bing,verify=False,headers=headers)
			fwd = select.content
			ip = re.findall('<h2><a href="(.*?)"', fwd)
			for i in ip:
				o = i.split('/')
				if (o[0]+'//'+o[2]) in ch:
					print '\n\033[92m[IP]: \033[91m',(louis)
					pass
				else:
					ch.append(o[0]+'//'+o[2])
					print '\033[00m',(o[0]+'//'+o[2])
					with open('COVID-19/From-Ips.txt', 'a') as s:
						s.writelines((o[0]+'//'+o[2])+'\n')
			page = page+50
if lucifer =='3':
    ips = raw_input("\n\033[92m[!]\033[91m WELCOME TO HELL ENTER LIST OF IPS : ")
    ips = open(ips, 'r')
    for site in ips:
        ur = site.rstrip()
        ch = site.split('\n')[0].split('.')
        ip1 = ch[0]
        ip2 = ch[1]
        louis = str(ip1) + '.' + str(ip2) + '.'
        i = 0
        while i <= 255:
            i += 1
            c = 0
        while c <= 255:
            c += 1
            print "\033[92m[IP RANGE]: \033[91m" + str(louis) + str(c) + '.' + str(i)
            open('COVID-19/From-Range.txt', 'a').write(str(louis) + str(c) + '.' + str(i) + '\n')