import urllib.request
msg = str(input('Enter your message : '))
msg = msg.replace(' ', "%20")
msg = msg.replace('\n', "%0A")

write_api_key = 'IRMPN4OE1F447726'
baseURL = 'http://api.thingspeak.com/update?api_key=' + write_api_key + '&field3='

f = urllib.request.urlopen(baseURL + str(msg))
f.read()
f.close()

print("\nYour message has successfully been sent!")

# b=urllib.request.urlopen('https://api.thingspeak.com/update?api_key=M0EFAIMXXCZPY7T8&field1='+msg)