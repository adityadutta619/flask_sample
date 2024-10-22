from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Boomsiyaaaa!!</h1> The webpage is working"


@app.route('/<name>')
def user(name):
    return f"Mama miyaan! {name}"


@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))

if __name__ == '__main__':
    app.run()
