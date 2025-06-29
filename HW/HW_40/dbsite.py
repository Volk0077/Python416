import sqlite3, os
from flask import Flask, render_template, request, g, flash, redirect, url_for

from fdatabase import FDataBase

DATABASE = os.path.join(os.path.dirname(__file__), "kurs.db")
SECRET_KEY = "devkey"

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = SECRET_KEY


def init_db():
    sql_file = os.path.join(os.path.dirname(__file__), "sq_db.sql")
    with open(sql_file, "r", encoding="utf-8") as f:
        sql = f.read()
    conn = sqlite3.connect(DATABASE)
    conn.executescript(sql)
    conn.commit()
    conn.close()
    print("База данных создана!")


def connect_db():
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    return con

def get_db():
    if not hasattr(g, "link_db"):
        g.link_db = connect_db()
    return g.link_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "link_db"):
        g.link_db.close()

@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template("index.html", menu=dbase.get_menu(), courses=dbase.get_all_courses())

@app.route("/add_kurs", methods=["GET", "POST"])
def add_kurs():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["short_description"]
        price = request.form["price"]
        dbase.add_course(title, desc, price)
        flash("Курс добавлен!", "success")
        return redirect(url_for("index"))
    return render_template("add_kurs.html", menu=dbase.get_menu())

@app.route("/contacts")
def contacts():
    db = get_db()
    dbase = FDataBase(db)
    return render_template("contacts.html", menu=dbase.get_menu())

@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return (
        render_template(
            "page404.html", title="Страница не найдена", menu=dbase.get_menu()
        ),
        404,
    )

if __name__ == "__main__":
    # Проверяем, существует ли база данных
    if not os.path.exists(DATABASE):
        print("Создаю базу данных...")
        init_db()
    app.run(debug=True)