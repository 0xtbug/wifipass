#!/usr/bin/python
# coding=utf-8

import os, re, time

def this_banner():
    print('''
 __      __.__  _____.__                            
/  \    /  \__|/ ____\__|__________    ______ ______
\   \/\/   /  \   __\|  \____ \__  \  /  ___//  ___/
 \        /|  ||  |  |  |  |_> > __ \_\___ \ \___ \  Created By TubagusNM
  \__/\  / |__||__|  |__|   __(____  /____  >____  >
       \/               |__|       \/     \/     \/ 
    A tool to view saved wifi passwords in windows
    ''')

this_banner()

#Get all saved wifi networks names
def get_wlans():
    data = os.popen("netsh wlan show profiles").read()
    wifi = re.compile("All User Profile\s*:.(.*)")
    return wifi.findall(data)

#Get a password for a network
def get_pass(network):
    try:
        wlan = os.popen("netsh wlan show profile "+str(network.replace(" ","*"))+" key=clear").read()
        pass_regex = re.compile("Key Content\s*:.(.*)")
        return pass_regex.search(wlan).group(1)
    except:
        return " "

if get_wlans == get_wlans:
    time.sleep(2)
    f = open("gotcha.txt","w")
    for wlan in get_wlans():
        f.write("\n-----------\n"+" SSID : "+wlan + "\n Password : " + get_pass(wlan))
    print("[INFO]Loading!")

    f.close()
    time.sleep(5)

    file_size = os.stat('gotcha.txt').st_size

if file_size == 0:
    print("[FAIL]The file is empty: " + str(file_size))
    time.sleep(3)
else:
    print("[SUCCESS]Saved to gotcha.txt")
    time.sleep(3)
