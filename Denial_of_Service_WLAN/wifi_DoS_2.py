import subprocess
import re
import csv
import os
import time
import shutil
from datetime import datetime

# all active wifi networks are saved in this list
active_wireless_networks = []

# checks if ESSID is already in the list. If not, it gets added to active_wireless_networks
def check_for_essid(essid, list):
    check_status = True

    if len(list) == 0:
        return check_status
    
    for item in list:
        if essid in item["ESSID"]:
            check_status = False

    return check_status


# sudo mode is required to run this script
if not 'SUDO_UID' in os.environ.keys():
    print("You must run this script in sudo mode")
    exit()


# backup all .csv files in the directory
for file_name in os.listdir():

    if ".csv" in file_name:

        # each time this script runs the .csv files will get deleted. There should only be one .csv file in the directory
        print("You have .csv files in your directory. Backing them up now")


        directory = os.getcwd()         # get the current working directory

        try:                            # make a new backup folder
            os.mkdir(directory + "/backup/")
        except:
            print("The backup folder already exists")

        timestamp = datetime.now()

        shutil.move(file_name, directory + "/backup/" + str(timestamp) + "-" + file_name)


# use regex to find all wireless interfaces (if they're wlan0 or higher)