from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1 style='color:red'>大家好，我是Flask!</h1>"

@app.route('/student/<name>/<int:age>')
def weclcome(name,age):
    return "<h1 style='color:red'>大家好，我是%s,今年%d岁!</h1>"%(name,age)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)

