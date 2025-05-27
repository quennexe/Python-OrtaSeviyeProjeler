from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import json
import os

app = Flask(__name__)
USER_FILE = "users.json"

# Kullanıcı verisini oku veya oluştur
if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w") as f:
        json.dump({}, f)

def load_users():
    with open(USER_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    users = load_users()
    username = data.get("username")
    password = data.get("password")

    if username in users:
        return jsonify({"message": "Kullanıcı zaten var!"}), 400

    users[username] = generate_password_hash(password)
    save_users(users)
    return jsonify({"message": "Kayıt başarılı!"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    users = load_users()
    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"message": "Kullanıcı bulunamadı!"}), 404

    if check_password_hash(users[username], password):
        return jsonify({"message": "Giriş başarılı!"})
    else:
        return jsonify({"message": "Hatalı şifre!"}), 401

if __name__ == '__main__':
    app.run(debug=True)
