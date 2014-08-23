# Unmanned System Caucus Members

#import sys
# sys.path.append('/usr/lib/python2.7/dist-packages/')
from bs4 import BeautifulSoup

import urllib2
import csv
#import os
import re

# os.chdir("/Users/marjorieroswell/Dropbox/python/caucuses")

f= csv.writer(open("drone_caucus_members.csv", "w"))
f.writerow(["caucus_name","name","district","website","photo_url"]) 

page = urllib2.urlopen("http://unmannedsystemscaucus.mckeon.house.gov/about/membership.shtml")

soup = BeautifulSoup(page)

caucus_name = "Unmanned Systems Caucus"

for row in soup.find_all("tr"):
	tds = row.find_all("td")
        for i in range(0,5):
		try:
			membertext = str(tds[i].get_text())
                        website = str(tds[i].a['href'])
                        photo_url = str(tds[i].img['src'])
                        photo_url = re.sub("http://unmannedsystemscaucus.mckeon.house.gov","",photo_url)
                        photo_url = "http://unmannedsystemscaucus.mckeon.house.gov" + photo_url
			m = re.search(r'(.*)\((.*)\)', membertext)
			if m:
				district = m.group(2)
				member = m.group(1).strip()
			else:
				district = ''
                                member = ''
                        
		except:
			print "bad string"
			continue

     		f.writerow([caucus_name, member, district, website, photo_url])
