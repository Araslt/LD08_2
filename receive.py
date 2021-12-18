import urllib.request

import requests

read_api_key = 'B56BF9I7H9M9BCH7'

msg = requests.get('https://api.thingspeak.com/channels/1602871/fields/3.json?api_key='+read_api_key+'&results=2')
msg = msg.json()['feeds'][1]['field3']
print("\nThe Message sent was: \n\n" + str(msg))
