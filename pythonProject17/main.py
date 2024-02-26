import datetime

from flask import Flask, render_template, redirect

from data.jobs import Jobs
from data.user import User
from log_in_form import LoginForm
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def i():
    return "Hello, world!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success')
def success():
    return '<h1>Успешно!</h1>'


db_session.global_init("db/mars_explorer.db")


user2 = User()
user2.surname = 'Maria'
user2.name = "Isaeva"
user2.position = 'programmer'
user2.speciality = 'programmer'
user2.address = 'module_2'
user2.email = "maryisaeva@yandex.ru"
db_sess = db_session.create_session()
db_sess.add(user2)
db_sess.commit()

user3 = User()
user3.surname = 'Andrew'
user3.name = "Lesh"
user3.position = 'programmer'
user3.speciality = 'programmer'
user3.address = 'module_3'
user3.email = "andrew@yandex.ru"
db_sess = db_session.create_session()
db_sess.add(user3)
db_sess.commit()

user4 = User()
user4.surname = 'Ann'
user4.name = "Kovtun"
user4.position = 'programmer'
user4.speciality = 'programmer'
user4.address = 'module_5'
user4.email = "annkov@yandex.ru"
db_sess = db_session.create_session()
db_sess.add(user4)
db_sess.commit()


job = Jobs()
job.team_leader = 1
job.job = 'deployment of residential modules 1 and 2'
job.work_size = 15
job.collaborators = '2, 3'
job.is_finished = False
db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
