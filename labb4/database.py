import requests, time
from flask import Flask, render_template, jsonify
from flask import request
import sqlite3
import random



data_dict = {keys: random.random() for keys in range (10)}
r = requests.post('https://en7w1brogvxyv.x.pipedream.net', json=data_dict)
#print(r.status_code)
hej = requests.get('https://en7w1brogvxyv.x.pipedream.net')
volle = hej.json()
print(r.json())
print(volle)
#print(r.headers)
volkan = sqlite3.connect('databas.db')
boi = volkan.cursor()
#boi.execute("""CREATE TABLE vookie (data_dict)""")
#boi.execute('INSERT INTO vookie (data_dict) VALUES (?)',volle)
volkan.commit()
#print(volkan)

