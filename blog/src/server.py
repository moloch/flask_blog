__author__ = 'Dario Coco'


from sqlalchemy import create_engine
from blog.src.models import User
from blog.src.config import DATABASE_URI
from blog import app, db, login_manager
from flask_login import login_user, logout_user, login_required
from blog.src.forms import LoginForm
from flask import render_template, redirect


@app.route("/create")
def hello():
    dario = User('dario', 'dario.coco@gmail.com', 'test')
    db.session.add(dario)
    db.session.commit()
    return "dario created"

@app.route("/delete")
def delete():
    User.query.delete()
    db.session.commit()
    return "dario deleted"

@app.route("/admin")
@login_required
def admin():
    return "ADMIN SECTION"

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        username = form.username.data
        user = User.query.filter(User.username == username).first()
        login_user(user)
        return 'HELLO'
    return render_template("login_form.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect('login')

def create_app(database_uri, debug=False):
    app.debug = debug
    app.engine = create_engine(database_uri)
    return app

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

if __name__ == '__main__':
    app = create_app(DATABASE_URI, debug=False)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.secret_key ='123'
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    app.run()


