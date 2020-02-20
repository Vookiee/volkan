from flask import Flask, render_template, jsonify, request
import requests
from random import randint
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def register():
    info = [
    request.form.get('fname'),
    request.form.get('ename'),
    request.form.get('address'),
    request.form.get('zipcode'),
    request.form.get('city'),
    request.form.get('cellphone'),
    request.form.get('email'),
    request.form.get('lösenord'),
    request.form.get('paymenttype'),
    request.form.get('offers'),
    request.form.get('format'),
    request.form.get('comment')]

    f_name = info[0]
    e_name = info[1]
    address = info[2]
    postnmr = info[3]
    stad = info[4]
    telnmr = info[5]
    email = info[6]
    losenord = info[7]
    betala = info[8]
    offer = info[9]
    form = info[10]
    kommentar = info[11]
    return render_template('index.html', fname = f_name, ename =e_name, 
                           address=address, postnmr =postnmr, stad=stad, tele=telnmr,
                           email=email,pw=losenord, pay=betala, offer=offer,
                           for_mat=form, kommentar=kommentar)
@app.route('/num')
def num():
    rng = randint(10,200)
    rng1 = randint(300,1000)
    rng2 = randint(5,10)
    return jsonify(rng, rng1, rng2)




# @app.route('/num')
# def num():
#     rng = randint(10,200)
#     rng1 = randint(300,1000)
#     rng2 = randint(5,10)
#     return jsonify(rng, rng1, rng2)

# def getnum():
#     svar = requests.get('http://localhost:5000/num')
#     data = svar.json()
    
#     conn = sqlite3.connect('databas.db')
#     c = conn.cursor()
#     c.execute("""CREATE TABLE volkan (rng,rgn1,rng2)""")
#     c.execute('INSERT INTO volkan (rng,rng1,rng2) VALUES (?,?,?)',data)
#     c.execute('SELECT * FROM volkan')
#     print(c.fetchall())
#     conn.commit()
#     conn.close()
# getnum()
# @app.route('/', ['GET'])
# def postdata():
#       #r = requests.post('https://en7w1brogvxyv.x.pipedream.net', json=data_dict)
#       conn = sqlite3.connect('databas.db')
#       c = conn.cursor()
#       c.execute('SELECT * FROM data')
#       data = c.fetchall()
#       return justify(data)


if __name__ == '__main__': 
    app.run()
    