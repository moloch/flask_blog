__author__ = 'Dario Coco'


from sqlalchemy import create_engine
from blog.src.models import User
from blog.src.config import DATABASE_URI
from blog import app, db
from blog.src.forms import LoginForm
from flask import render_template


@app.route("/create")
def hello():
    dario = User('dario', 'dario.coco@gmail.com')
    db.session.add(dario)
    db.session.commit()
    return "dario created"

@app.route("/delete")
def delete():
    User.query.delete()
    db.session.commit()
    return "dario deleted"

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate():
        print("HELLO")
    return render_template("login_form.html", form=form)

def create_app(database_uri, debug=False):
    app.debug = debug
    app.engine = create_engine(database_uri)
    return app

if __name__ == '__main__':
    app = create_app(DATABASE_URI, debug=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    db.init_app(app)
    app.run()


