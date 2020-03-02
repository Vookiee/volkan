from flask import Flask, render_template, jsonify, request
#import request
from random import randint
import sqlite3
import time




app = Flask(__name__)


@app.route('/rng', methods=['POST'])
def postJsonHandler():
    print(f'request.is_json: {request.is_json}')
    content=request.get_json()
    print(f'content: {content}')
    conn = sqlite3.connect('dats.db')
    c = conn.cursor()
    #c.execute("""CREATE TABLE volkan(rng, rng1, rng2)""")
    c.execute('INSERT INTO volkan (rng, rng1, rng2) VALUES (?,?,?)',(content['rng'],content['rng1'],content['rng2']))
    conn.commit()
    conn.close()
    return '{"message":"JSON post success"}'


@app.route('/hej')
def getnum():
    conn = sqlite3.connect('dats.db')
    c = conn.cursor()
    c.execute('SELECT rng FROM volkan')
    rng = c.fetchall()
    c.execute('SELECT rng1 FROM volkan')
    rng1 = c.fetchall()
    c.execute('SELECT rng2 FROM volkan')
    rng2 = c.fetchall()
    
    conn.commit()
    conn.close()
    return render_template('databas.html',rng = rng, rng1 = rng1, rng2=rng2)


if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5050)
    
    
