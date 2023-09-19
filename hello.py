from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>' 

@app.route('/user/<Jioh>') 
def user(Jioh):
    return '<h1>Hello, %s!</h1>' % Jioh


if __name__ == '__main__':
    app.run(debug=True)