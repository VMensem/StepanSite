from flask import Flask, render_template, url_for, request, jsonify
import requests
import os
app = Flask(__name__)

# 🔑 EasyDonateAPI
EASYDONATE_API_KEY = os.getenv("EASYDONATE_API_KEY")


# Пример данных — можно заменить на реальные запросы к БД
fake_stats = {
    'online': 999,
    'players_now': 999,
    'balance': '999 ₽'
}


# ------------------ Главная ------------------
@app.route('/')
def index():
    return render_template('index.html', stats=fake_stats)


# ------------------ Магазин ------------------
@app.route('/shop')
def shop():
    # Список платёжных методов для отображения
    payments = [
        {'name': 'СБП', 'min': '10 ₽', 'img': 'sbp.png'},
        {'name': 'МИР', 'min': '10 ₽', 'img': 'mir.png'},
        {'name': 'Visa', 'min': '10 ₽', 'img': 'visa.png'},
        {'name': 'MasterCard', 'min': '10 ₽', 'img': 'master.png'},
    ]
    return render_template('shop.html', payments=payments, stats=fake_stats)


# ------------------ Проверка донатов ------------------
@app.route('/donate-check/<nickname>')
def check_donations(nickname):
    """Позволяет проверить донаты игрока по нику"""
    url = "https://easydonate.ru/api/v3/shop/donates"
    headers = {"Authorization": f"Bearer {EASYDONATE_API_KEY}"}
    params = {"nickname": nickname}

    response = requests.get(url, headers=headers, params=params)
    return jsonify(response.json())


# ------------------ Webhook EasyDonate ------------------
@app.route('/webhook', methods=['POST'])
def easydonate_webhook():
    """Обработчик уведомлений EasyDonate"""
    data = request.json
    if not data:
        return jsonify({"error": "no data"}), 400

    nickname = data.get("nickname")
    product = data.get("product")
    amount = data.get("amount")

    print(f"✅ Новый донат: {nickname} купил {product} x{amount}")

    # 💾 Здесь можно:
    # - записывать донаты в базу данных
    # - выдавать донат через RCON или API сервера
    # - отправлять уведомление в Discord / Telegram

    return jsonify({"status": "success"}), 200


# ------------------ Запуск ------------------
if __name__ == '__main__':
    app.run(debug=True)
