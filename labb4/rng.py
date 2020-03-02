
import requests
from random import randint
import time
import json

while True:
    time.sleep(5)
    rng = randint(10,200)
    rng1 = randint(300,1000)
    rng2 = randint(5,10)
    s = {'rng':rng,'rng1':rng1, 'rng2':rng2}

    r = requests.post('http://localhost:5050/rng', json = s)
    time.sleep(10)
