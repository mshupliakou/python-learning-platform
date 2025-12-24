from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def base():  # put application's code here
    return render_template('base.html')

@app.route('/login')
def login():  # put application's code here
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
