import requests
import json
from time import sleep


def client(URL):
    r = requests.get(url=URL)
    return r


if __name__ == "__main__":
    URL = "http://nginx"
    while(True):
        sleep(5)
        response = client(URL)
        data = json.loads(response.text)
        print(data)
