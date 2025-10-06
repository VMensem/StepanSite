from flask import Flask, render_template, request, redirect, url_for, jsonify
from mcstatus import JavaServer

app = Flask(__name__)

# Методы оплаты
payments = [
    {'name': 'СБП', 'min': '10 ₽', 'img': 'sbp.png'},
    {'name': 'МИР', 'min': '10 ₽', 'img': 'mir.png'},
    {'name': 'Visa', 'min': '10 ₽', 'img': 'visa.png'},
    {'name': 'MasterCard', 'min': '10 ₽', 'img': 'master.png'},
]

MINECRAFT_IP = "5.9.235.227"
MINECRAFT_PORT = 25657

def get_minecraft_status():
    try:
        server = JavaServer.lookup(f"{MINECRAFT_IP}:{MINECRAFT_PORT}")
        status = server.status()
        return status.players.online, status.players.max
    except Exception as e:
        print("Ошибка получения статуса:", e)
        return 0, 0

@app.route('/')
def index():
    online, max_players = get_minecraft_status()
    stats = {
        'online': online,
        'max_players': max_players,
        'balance': '999 ₽'
    }
    return render_template('index.html', stats=stats)

@app.route('/shop')
def shop():
    return render_template('shop.html', payments=payments, stats=stats)

@app.route('/success')
def success():
    return render_template('success.html', stats=stats)

@app.route('/fail')
def fail():
    return render_template('fail.html', stats=stats)

@app.route('/result')
def result():
    return render_template('result.html', stats=stats)

@app.route('/refund')
def refund():
    return render_template('refund.html', stats=stats)

@app.route('/chargeback')
def chargeback():
    return render_template('chargeback.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True)
