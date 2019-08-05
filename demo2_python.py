from flask import Flask,request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login')
def login():
    name = request.args.get('name')
    print(name)
    return '登录成功'

if __name__ == '__main__':
    app.run()
