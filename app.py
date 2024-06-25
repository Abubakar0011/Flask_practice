from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def Welcome():
    return 'welcome to the flask practice, hello D.'

@app.route('/pass/<int:score>')
def Pass(score):
    return f'The student is passed and got {score} marks.'

@app.route('/fail/<int:score>')
def fail(score):
    return f'The student is failed and got {score} marks.'

### lets create a function which chek for the condition
@app.route('/result/<int:marks>')
def result(marks):
    rslt = " "
    if marks < 50:
        rslt = 'fail'
    else:
        rslt = 'Pass'
    return redirect(url_for(rslt, score=marks))


if __name__ == '__main__':
    app.run(debug=True)




