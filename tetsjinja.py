from jinja2 import Template

name = "Федя"

tm = Template("Привет {{fedya}}")
msg = tm.render(fedya=name)
print(msg)

age = 13
tm = Template("Меня зовут {{fedya}} мне {{let}} лет")
msg = tm.render(fedya=name, let=age)
print(msg)

per = {'name': 'Федя', 'age': 34}
tm = Template("Меня зовут {{p['name']}} мне {{p['age']}} лет")
# tm = Template("Меня зовут {{p.name}} мне {{p.age}} лет")
msg = tm.render(p=per)
print(msg)


data = '''{% raw %} 
Отображает все <a href=http://ya.ru> Иди на яндукс </a>        {{name}}
Вот так 
{% endraw %}'''
tm = Template(data)
msg = tm.render(name='Федя')
print(msg)


def fun(a):
    return a + "выполнена выполнена"


print(Template("{{ foo('5') }}").render(foo=fun))

slovar={'name': 'tom', 'age': 25, 'designation': 'Manager'}
print(slovar.get('name'))






from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def vas():
    mas=[0,1,2,3,4,5]
    # slovar = {'name': 'tom', 'age': 25, 'designation': 'Manager'}
    # print(slovar.get('name'))
    #
    sam=[[1,2,3],
         [4,5,6],
         [7,8,9]]

    # return render_template("jinja.html",rez=mas,slovar=slovar,sam=sam)
    return render_template("testjinja.html", rez=sam)

app.run()