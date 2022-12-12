# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 09:54:48 2022

@author: teacher
"""

import requests

r = requests.get('https://tw.yahoo.com/?guccounter=1')

if r.status_code == 200:
    print(r.text)