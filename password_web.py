from bottle import route, run, template, request, get, post, redirect, response
import templates
import sqlite3
import json
from actions import PasswordHolder

main = templates.main_if_not_login

password_holder = PasswordHolder()
login_password = dict()

def check(login, password):
    with open('users.json', 'r') as file:
        users = json.load(file)
    if tuple((login, password),) in users.items():
        response.set_cookie('user','yes')
        redirect('/main')
    else:
        response.set_cookie('user','no')
        redirect('/main')
            
@get('/main')
def hello():
    if request.get_cookie('user') == 'yes':
        login_password = password_holder.take()
        return template(templates.main_if_login, login_password = login_password)
    else:

        return template(templates.main_if_not_login)

@post('/main')
def do_login():
    if request.get_cookie('user') != 'yes':
        print(request.action)
        check(*dict(request.forms).values())
    else:
        print(dict(request.forms))
        password_holder.incert(password=request.forms['password'], from_what = request.forms['name'])
        redirect('/main')

@get('/main/<name>')
def get_one_site(name):
    login_password = password_holder.take()
    password = login_password[name]
    return template(templates.one_site, name = name, password = password)

@post('/main/<name>')
def del_one_site(name):
    if request.get_cookie('user') == 'yes':
        print(dict(request.forms))
        if request.forms.action == 'Delete':
            password_holder.dell_one(name)
            redirect('/main')
        elif request.forms.action == 'Update':
            password_holder.update_one(name, request.forms.password)
            redirect('/main')
            
    
run(host='localhost', port=8080, debug=True)
