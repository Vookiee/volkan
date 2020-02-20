from flask import Flask, render_template, jsonify, request
import requests
from random import randint
import sqlite3

app = Flask(__name__)

@app.route('/num')
def num():
    rng = randint(10,200)
    rng1 = randint(300,1000)
    rng2 = randint(5,10)
    return jsonify(rng, rng1, rng2)

def getnum():
    svar = requests.get('http://localhost:5000/num')
    data = svar.json()
    
    conn = sqlite3.connect('databas.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE volkan (rng,rgn1,rng2)""")
    c.execute('INSERT INTO volkan (rng,rng1,rng2) VALUES (?,?,?)',data)
    c.execute('SELECT * FROM volkan')
    print(c.fetchall())
    conn.commit()
    conn.close()
getnum()
