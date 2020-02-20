from flask import Flask, render_template, jsonify, request
import requests
from random import randint
import sqlite3
import time

app = Flask(__name__)
@app.route('/')
def getnum():
    while True:
        time.sleep(5)
        svar = requests.get('http://localhost:5000/num')
        data = svar.json()
        conn = sqlite3.connect('databas.db')
        c = conn.cursor()
        #c.execute("""CREATE TABLE volkan(rng, rng1, rng2)""")
        c.execute('INSERT INTO volkan (rng, rng1, rng2) VALUES (?,?,?)',data)
        #c.execute('SELECT * FROM volkan')
        c.execute('SELECT rng FROM volkan')
        rng = c.fetchall()
        c.execute('SELECT rng1 FROM volkan')
        rng1 = c.fetchall()
        c.execute('SELECT rng2 FROM volkan')
        rng2 = c.fetchall()
        #print(tables[0])
        conn.commit()
        conn.close()
        return render_template('databas.html', rng = rng, rng1 = rng1, rng2 = rng2)

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5050)
    
    
