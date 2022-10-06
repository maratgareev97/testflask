import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/<a>&<b>')
def vas(a, b):
    x = str(int(a, int(b)))
    f = "6"
    return render_template("index.html", otevet=x,f=f)

@app.route('/urav')
def urav():
    return render_template('urav.html')

@app.route('/urav/get',methods=['POST','GET'])
def urav1():
    if request.method == 'POST':
        a = int(request.form['a'])
        b = int(request.form['b'])

    if request.method == 'GET':
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))

    print(a,b)
    if a!=0:
        x=b/a
        print(x)
    else:
        x='Нет корней'
        print('нет корней')
    return render_template('urav.html', x=x)


app.run()
