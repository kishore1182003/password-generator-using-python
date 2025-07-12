from flask import Flask, render_template, jsonify, request, redirect, url_for, session
import random
import string

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this for production!

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session['logged_in'] = True
        return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/")
def index():
    if not session.get('logged_in'):
        return redirect(url_for("login"))
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    length = int(data.get("length", 12))
    password = generate_password(length)
    return jsonify({"password": password})

if __name__ == "__main__":
    app.run(debug=True)