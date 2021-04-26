from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'f509a688-46b1-492f-911e-a20939a0a875'


@app.route('/')
def work():
    db_session.global_init('db/blogs.db')
    db_sess = db_session.create_session()
    all_data = []
    for job in db_sess.query(Jobs).all():
        user = job.team_leader
        for getting in db_sess.query(User).filter(User.id == user):
            user = getting.surname + ' ' + getting.name
            break
        title = job.job
        time = job.work_size
        people = job.collaborators
        is_finished = job.is_finished
        all_data.append((title, user, time, people, is_finished))
    return render_template("work.html", all_data=all_data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
