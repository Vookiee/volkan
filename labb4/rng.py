from flask import Flask, render_template, jsonify, request
import requests
from random import randint
import sqlite3
import time


def num():
    while True:
        time.sleep(5)
        rng = randint(10,200)
        rng1 = randint(300,1000)
        rng2 = randint(5,10)
        return jsonify(rng, rng1, rng2)
num()

send = requests.post('localhost:5050', json = num())
print(send.status_code)