import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/testurav')
def urav():
    return render_template('testurav.html')

@app.route('/testurav/otvet', methods=['POST','GET'])
def urav1():
    if request.method == 'POST':
        a = int(request.form['aaa'])
        b = int(request.form['bbb'])

    if request.method == 'GET':
        a = int(request.args.get('aaa'))
        b = int(request.args.get('bbb'))

    if a != 0:
        x = b / a
        x = "x= " + str(x)
    else:
        x = "нет корней"
    return render_template('testurav.html',otvet=x)


app.run()

# a = int(input("a = "))
# b = int(input("b = "))
# if a != 0:
#     x = b / a
#     x = "x= " + str(x)
# else:
#     x = "нет корней"
# print(x)
