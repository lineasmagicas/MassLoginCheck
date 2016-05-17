#!/usr/bin/env python
# coding=utf-8
"""
Copyright (C) 2016, Alan Levy
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = "Alan Levy"
__email__ = "alevy@cintainfinita.com"
__license__ = "GPL"

try:
	import requests
	from BeautifulSoup import BeautifulSoup as Soup
except ImportError:
	print "Te faltan algunas dependencias, por favor instalá: 'requests', 'BeautifulSoup'"

#------- User/Pass
print("Escriba una dirección de email")
email = raw_input()
print("Escriba el password") 
password = raw_input()
print("Sus credenciales introducidas fueron: "+ email, password)
#----------------------------------

#Open Session
s = requests.Session()
#GET netflix and set User-Agent
s.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0'})
login = s.get("https://www.netflix.com/ar-en/Login")

soup=Soup(login.text)

#Search into the form.
authURL = soup.findAll('form')[0]('input')[-2]['value']

#Make the POST.
r2 = s.post("https://www.netflix.com:443/Login", headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://www.netflix.com/Login", "Connection": "close", "Content-Type": "application/x-www-form-urlencoded"}, data={"email": (email), "password": (password), "rememberMeCheckbox": "true", "flow": "websiteSignUp", "mode": "login", "action": "loginAction", "withFields": "email,password,rememberMe,nextPage", "authURL": (authURL), "nextPage": "https://www.netflix.com/browse"})
#---------end of POST ----------------------------------------------

#Go to browse into Netflix.
r1 = s.get("https://www.netflix.com/browse	")

#Check for valid user...
validado = r1.text.find('Please enter a valid email')
if validado == -1:
	print("Exito!!!")
else:
	print("No funciona =( ")
#End check-------------------------------------

