from flask import Flask, render_template, url_for


app = Flask(__name__)


# Простой пример данных — можно заменить реальными запросами к БД
fake_stats = {
'online': 999,
'players_now': 999,
'balance': '999 ₽'
}


@app.route('/')
def index():
    return render_template('index.html', stats=fake_stats)


@app.route('/shop')
def shop():
# Список платежных методов для отображения
    payments = [
{'name': 'СБП', 'min': '10 ₽', 'img': 'sbp.png'},
{'name': 'МИР', 'min': '10 ₽', 'img': 'mir.png'},
{'name': 'Visa', 'min': '10 ₽', 'img': 'visa.png'},
{'name': 'MasterCard', 'min': '10 ₽', 'img': 'master.png'},
]
    return render_template('shop.html', payments=payments, stats=fake_stats)


if __name__ == '__main__':
    app.run(debug=True)
