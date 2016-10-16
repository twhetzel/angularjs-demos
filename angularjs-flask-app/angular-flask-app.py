from flask import Flask, render_template


app = Flask(__name__)


@app.route('/angular-home')
def angular_test():
    return render_template('angular-flask-template.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=8080)
