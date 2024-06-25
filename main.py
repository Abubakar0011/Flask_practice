from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    rslt_dict = {'score': score, 'result': res}
    return render_template('result.html',result=rslt_dict)


@app.route('/fail/<int:score>')
def fail(score):
    rslt = ""
    if score < 50:
        rslt = "Fail"
    else:
        rslt = 'success'

    rslt_dict = {'score': score, 'result': rslt}
    return render_template('result.html', result=rslt_dict)
    # return f'The student is failed and got {score} marks.'


    
### Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))

### Result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    res=""
    if total_score>50:
        res = "success"
    else:
        res = "fail"

    return redirect(url_for(res ,score=total_score))


if __name__=='__main__':
    app.run(debug=True)