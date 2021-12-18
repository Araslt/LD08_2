# Python3
import random
from time import sleep
import urllib.request


def thingspek_post():
    write_api_key = 'IRMPN4OE1F447726'
    baseURL = 'http://api.thingspeak.com/update?api_key=' + write_api_key + '&field1='
    a = 0
    c = 0
    print(baseURL)
    while a < 10:
        c = int(random.random() * 100)
        print(c)
        f = urllib.request.urlopen(baseURL + str(c))
        f.read()
        f.close()

        sleep(20)
        a = a + 1
    print("Program has ended")


if __name__ == "__main__":
    thingspek_post()
