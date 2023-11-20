import paramiko
import csv
import time

# Create log file
log_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
f = open(f'log_{log_time}.txt', 'x')

# Parse Device CSV
reader = csv.DictReader(open('device-list.csv'),delimiter='\t')
for row in reader:
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    device_ip = row["IP"]
    device_username = row["Username"]
    device_password = row["Password"]
    print(f'{timestamp} Connecting to IP: {row["IP"]} with username: {row["Username"]}')
    f = open(f'log_{log_time}.txt', 'a')
    f.write(f'{timestamp} Connecting to IP: {row["IP"]} with username: {row["Username"]}\n')
    f.close()
# Attempt SSH connection
    try:
        remote_conn_pre=paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(device_ip, port=22, username=device_username, password=device_password, look_for_keys=False, allow_agent=False)
        remote_conn = remote_conn_pre.invoke_shell()
        remote_conn.send("\n")
        remote_conn.send("\n")
        print("Connected. Sending commands now.")
        f = open(f'log_{log_time}.txt', 'a')
        f.write(f'{timestamp} Connected to IP: {row["IP"]} and sending commands\n')
        f.close()
        output = remote_conn.recv(65000)
# Send commands  !!! Don't forget to include the command to save config changes !!!
        command_file = open('command-list.txt', 'r').readlines()
        for command in command_file:
            remote_conn.send(f'{command}\n')
            time.sleep(.5)
        output = remote_conn.recv(65000)
        output_str = output.decode('utf-8')
        f = open(f'log_{log_time}.txt', 'a')
        f.write(f'{timestamp} Device IP: {row["IP"]} Commands output:\n')
        f.write(f'{output_str}\n')
        f.write(f'{timestamp} Device IP: {row["IP"]} All commands sent.\n')
        f.write(f'\n')
        f.close()
        print(f'Commands sent to {device_ip} successfully.')
        print('\n')
    except:
        print(f'Unable to connect to {row["IP"]} with username: {row["Username"]} and password: {row["Password"]}\n')
        f = open(f'log_{log_time}.txt', 'a')
        f.write(f'{timestamp} Device IP: {row["IP"]} Unable to connect with username: {row["Username"]} and password: {row["Password"]}\n')
        f.close()

