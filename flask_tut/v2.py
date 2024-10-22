from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("v2.html", 
        content=f'What do you say! {name}', 
        r=2)

if __name__ == '__main__':
    app.run()
