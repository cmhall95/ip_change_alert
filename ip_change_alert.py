import pandas as pd
import os.path as path
from requests import get

# Flag to indicate if the IP address has changed and variable to store the last observed IP address
ip_changed = False
last_observed_ip = ''

# Load or create file for ip address history
if path.exists('ip_address_history.csv'):
   ip_address_history = pd.read_csv('ip_address_history.csv', header=0)
   # Find the last observed IP address
   last_observed_ip = ip_address_history[ip_address_history['is_current'] == True]['ip_address'].values[0]
else:
   columns = ['ip_address','first_observed','last_observed','is_current']
   ip_address_history = pd.DataFrame(columns=columns)
   ip_changed = True

# Get current IP address
current_ip = get('https://api.ipify.org').content.decode('utf8')

# Check if the current IP address is different from the last observed IP address
if last_observed_ip == '' or current_ip != last_observed_ip:
    ip_changed = True

# Search for current IP address in ip_address_history
if current_ip in ip_address_history['ip_address'].values:
    # Update last_observed and is_current for existing IP address
    ip_address_history.loc[ip_address_history['ip_address'] == current_ip, 'last_observed'] = pd.Timestamp.now()
    ip_address_history.loc[ip_address_history['ip_address'] == current_ip, 'is_current'] = True
else:
    # Add new IP address to ip_address_history
    new_entry = pd.DataFrame({
        'ip_address': [current_ip],
        'first_observed': [pd.Timestamp.now()],
        'last_observed': [pd.Timestamp.now()],
        'is_current': [True]
    })
    ip_address_history = pd.concat([ip_address_history, new_entry], ignore_index=True)

# Set is_current to False for all other IP addresses
ip_address_history.loc[ip_address_history['ip_address'] != current_ip, 'is_current'] = False

# Save ip_address_history to csv
ip_address_history.to_csv('ip_address_history.csv', index=False)