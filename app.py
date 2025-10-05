from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Пример данных
fake_stats = {
    'online': 999,
    'players_now': 999,
    'balance': '999 ₽'
}

# Пример товаров
products = [
    {'id': 1, 'name': 'Привилегия VIP', 'desc': 'Доступ к командам и бонусам.', 'img': 'item1.png', 'price': 99},
    {'id': 2, 'name': 'Привилегия Premium', 'desc': 'Больше возможностей и прав.', 'img': 'item2.png', 'price': 199},
    {'id': 3, 'name': 'Монеты', 'desc': 'Валюта для покупок в игре.', 'img': 'item3.png', 'price': 50},
    {'id': 4, 'name': 'Питомец', 'desc': 'Уникальный спутник на сервере.', 'img': 'item4.png', 'price': 149},
    {'id': 5, 'name': 'Титул "Легенда"', 'desc': 'Редкий титул на сервере.', 'img': 'item5.png', 'price': 249},
]

# Методы оплаты
payments = [
    {'name': 'СБП', 'min': '10 ₽', 'img': 'sbp.png'},
    {'name': 'МИР', 'min': '10 ₽', 'img': 'mir.png'},
    {'name': 'Visa', 'min': '10 ₽', 'img': 'visa.png'},
    {'name': 'MasterCard', 'min': '10 ₽', 'img': 'master.png'},
]


@app.route('/')
def index():
    return render_template('index.html', stats=fake_stats, products=products)


@app.route('/shop')
def shop():
    return render_template('shop.html', payments=payments, stats=fake_stats)


# === PAYMENTS CALLBACKS ===

@app.route('/success')
def success():
    return render_template('success.html', stats=fake_stats)

@app.route('/fail')
def fail():
    return render_template('fail.html', stats=fake_stats)

@app.route('/refund')
def refund():
    return render_template('refund.html', stats=fake_stats)

@app.route('/chargeback')
def chargeback():
    return render_template('chargeback.html', stats=fake_stats)


if __name__ == '__main__':
    app.run(debug=True)