from flask import Flask, render_template, request, redirect, url_for, jsonify
from mcstatus import MinecraftServer

app = Flask(__name__)

# IP и порт твоего сервера
server = MinecraftServer.lookup("5.9.235.227:25657")

# Получаем статус
status = server.status()
online_players = status.players.online
max_players = status.players.max

# Методы оплаты
payments = [
    {'name': 'СБП', 'min': '10 ₽', 'img': 'sbp.png'},
    {'name': 'МИР', 'min': '10 ₽', 'img': 'mir.png'},
    {'name': 'Visa', 'min': '10 ₽', 'img': 'visa.png'},
    {'name': 'MasterCard', 'min': '10 ₽', 'img': 'master.png'},
]


@app.route('/')
def index():
    from mcstatus import MinecraftServer
    server = MinecraftServer.lookup("mc.example.com:25565")
    status = server.status()
    stats = {
        'online': status.players.online,
        'max_players': status.players.max,
        'balance': '999 ₽'
    }
    return render_template('index.html', stats=stats)


@app.route('/shop')
def shop():
    return render_template('shop.html', payments=payments, stats=fake_stats)

@app.route('/success')
def success():
    return render_template('success.html', stats=fake_stats)

@app.route('/fail')
def fail():
    return render_template('fail.html', stats=fake_stats)

@app.route('/result')
def result():
    return render_template('result.html', stats=fake_stats)

@app.route('/refund')
def refund():
    return render_template('refund.html', stats=fake_stats)

@app.route('/chargeback')
def chargeback():
    return render_template('chargeback.html', stats=fake_stats)

if __name__ == '__main__':
    app.run(debug=True)
