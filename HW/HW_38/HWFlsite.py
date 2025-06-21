from flask import Flask, render_template

app = Flask(__name__)

menu = [
    {"name": "Главная", "url": "index"},
    {"name": "О нас", "url": "about"},
    {"name": "Обратная связь", "url": "contacts"}
]

@app.route('/')
@app.route('/index')
def home():
    return render_template('home.html', title='Главная страница', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title='О нас', menu=menu)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html', title='Контакты', menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu), 404


if __name__ == '__main__':
    app.run(debug=True)