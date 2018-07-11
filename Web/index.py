from flask import Flask, render_template, request
from flask import jsonify

app = Flask(__name__, )
app.config['SECRET_KEY'] = "dfdfdffdad"


@app.route('/')
def login():
    return render_template('untitled.html')

@app.route('/main')
def main1():
    return render_template('main.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/mystring')
def mystring():
    return 'my string'


@app.route('/dataFromAjax')
def dataFromAjax():
    test = request.args.get('mydata')
    print(test)
    return 'dataFromAjax'


@app.route('/mydict', methods=['GET', 'POST'])
def mydict():
    d = {'name': 'xmr', 'age': 18}
    return jsonify(d)


@app.route('/mylist')
def mylist():
    l = ['xmr', 18]
    return jsonify(l)


@app.route('/js_call')
def js_call():
    username = request.args.get('email')
    password = request.args.get('password')
    print(username)
    print(password)
    # to send the command by ssh : os.system("ssh user@host \' restart(command) \' ")
    if username == "123" and password == "test":
        return "loginsuccess"
    else:
        return "login failed"


if __name__ == '__main__':
    app.run()
