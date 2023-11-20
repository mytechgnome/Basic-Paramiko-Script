# Basic-Paramiko-Script
 Simple script to query CSV for list of devices, then run a provided list of commands

How to use the script:
1) Update device-list.csv with the IP, username, and password to log into devices
2) Update command-list.txt with the commands to be run against all devices (Make sure you include lines to get to the correct configuration mode as well as lines to save/apply/commit changes)
3) Run Paramiko-SSH.py

If you don't know the correct username and password, you can add the same IP to the device-list.csv with a different username/password for each instance. The log file will display the result of each attempt.
