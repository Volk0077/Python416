import sqlite3, os
from flask import Flask, render_template, flash, request, g

from fdatabase import FDataBase


DATABASE = "/tmp/feedback.db"
DEBUG = True
SECRET_KEY = "Development key"

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, "feedback.db")))


def connect_db():
    con = sqlite3.connect(app.config["DATABASE"])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource("sq_db.sql", "r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, "link_db"):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template("index.html", menu=dbase.get_menu())

@app.route("/about")
def about():
    db = get_db()
    dbase = FDataBase(db)
    return render_template("about.html", menu=dbase.get_menu())


@app.route('/contacts', methods=["POST", "GET"])
def contacts():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == "POST":
        if len(request.form['username']) > 2:
            flash("Сообщение отправлено успешно!", category="success")
        else:
            flash("Ошибка отправки", category="error")
    return render_template('contacts.html', menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "link_db"):
        g.link_db.close()


if __name__ == "__main__":
    app.run()
