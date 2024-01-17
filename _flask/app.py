from flask import Flask, render_template, request, session

# configuration
DEBUG = True
SECRET_KEY = 'sdfjm3453ejkhl345h34ljfl4j32gfh4jg5l'

# application
app = Flask(__name__)


@app.route('/')
def index_text():
    return ('Hello')


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return 'Hello World'


@app.route('/hellouser')
def hellouser():
    username = 'Bill'

    return render_template('hellouser.html', username=username)


@app.route('/path/<order_id>') #http://127.0.0.1:5000//path/23456
def path_function(order_id):

    return render_template('order_id.html', order_id=order_id)


@app.route('/query')  #http://127.0.0.1:5000/query?a=1&b=2&c=3
def query_function():
    query_args = dict(request.args)

    username = 'Artem'
    return render_template('query.html', username=username, data=query_args)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form.get('uname')
        psw = request.form.get('psw')
        print(f'USER: {user}, PSW: {psw}')
        return render_template('login.html')
    return render_template('login.html',
                           mess='first_login')


if __name__ == '__main__':
    app.run('0.0.0.0')
