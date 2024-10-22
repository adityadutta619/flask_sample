from flask import Flask, redirect, url_for, render_template, request
import pandas as pd

app = Flask(__name__)

# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]
for i in range(5):
    data+=data

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])


@app.route("/<name>", methods=['GET', 'POST'])
def home(name):
    global df
    if request.method == 'POST':
        text = request.form['checkk']
        # Do something with the text, like saving it to a database

        df = df.sample(frac=1)

        df_html = df.to_html(classes='table table-dark table-striped table-hover', index=False)

        return render_template(
            "v4_bootstrap.html",
            contenttt=text,
            table=df_html)
    
    #return render_template('index.html')
    else:
        return render_template("v4_bootstrap.html", 
        contenttt=name)

if __name__ == '__main__':
    app.run(debug=True)
