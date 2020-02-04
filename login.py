#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################################
# Web scraper ASP authetication
# Feb 04 2020
################################################################################################
import requests
from bs4 import BeautifulSoup
#
# Using the session mode
session = requests.Session()
#
# Imitating a browser
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
session.headers.update(headers)
#
# Getting an initial page
url = 'http://72.211.52.152/axisjob/'
response =session.get(url)
soup=BeautifulSoup(response.content, 'html.parser')
#
# Extracting the session tokens
viewstate = soup.find('input' , id ='__VIEWSTATE')['value']
eventvalidation=soup.find('input' , id ='__EVENTVALIDATION')['value']
viewstategenerator=soup.find('input' , id ='__VIEWSTATEGENERATOR')['value']
#
# Making the post parameters
params={'__EVENTTARGET':'', '__EVENTARGUMENT':'', '__VIEWSTATE':viewstate,
        '__VIEWSTATEGENERATOR':viewstategenerator,
        '__EVENTVALIDATION':eventvalidation, 'Login1$UserName':'1234567',
        'Login1$Password':'1234567', 'Login1$LoginButton':'Login'}
#
# Login to a website
r=session.post(url, headers=headers, data=params)
print(r.text)
