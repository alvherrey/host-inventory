import argparse
import pandas as pd
import time
import utils.connection as connection

# Create dataframe from json
df = pd.read_csv("host-inventory.csv")
# Set headers
df = df[['host', 'ip', 'os']]
# Filter by column value
df = df[df['os'].str.contains('linux')]

# Test conection (for loop, better with apply; see add_ssh_key or ssh_key functions)
def connection_test_iteration():
    for ip in df['ip']:
        connection.test(ip)

# Test conection and save result to new column connection_test
def connection_test():
    df['connection_test'] = df['ip'].apply(connection.test)

# Add ssh public key
def add_ssh_key():
    df['ip'].apply(connection.add_ssh_key)

# Connect with ssh key
def ssh_key():
    df['ip'].apply(connection.ssh_key)

def default():
    print("Try '--help' for more information.")

# Create switch_options dictionary
switch_options = {
    "connection_test_iteration": connection_test_iteration,
    "connection_test": connection_test,
    "add_ssh_key": add_ssh_key,
    "ssh_key": ssh_key,
}

# Switch function
def switch(option):
    switch_options.get(option, default)()

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-e", "--execute", required=True, help="connection_test_iteration, connection_test, add_ssh_key, ssh_key")
args = vars(ap.parse_args())

# Execute switch case
option = args['execute']
switch(option)