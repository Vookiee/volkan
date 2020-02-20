from flask import Flask, render_template, jsonify, request
import requests
from random import randint
import sqlite3
import time

app = Flask(__name__)

def getnum():
    while True:
        time.sleep(10)
        svar = requests.get('http://localhost:5000/num')
        data = svar.json()
        conn = sqlite3.connect('databas.db')
        c = conn.cursor()
        #c.execute("""CREATE TABLE volkan(rng, rng1, rng2)""")
        c.execute('INSERT INTO volkan (rng, rng1, rng2) VALUES (?,?,?)',data)
        c.execute('SELECT * FROM volkan')
        #rows = c.fetchall()
        conn.commit()
        conn.close()
getnum()

@app.route('/')
def showdatabas():
    conn = sqlite3.connect('databas.db')
    c = conn.cursor()
    c.execute('SELECT rng,rng1,rng2 FROM volkan')
    tables = [
        v[0] for v in c.fetchall()
        ]
    print(tables)
    return render_template('databas.html', rng = tables)

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5050)
    
    
