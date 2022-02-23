import math
from flask import Flask, render_template,request

app = Flask (__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pitagoras', methods=['GET','POST'])
def pitagoras():
    if request.method == 'POST':
        a = request.form['front']
        b = request.form['side']
        result=math.sqrt(int(a)**2+int(b)**2)

        return render_template('pitagoras_view.html',num1=int(a),num2=int(b),result=int(result))
    return render_template('pitagoras.html')

@app.route('/squareroot',methods=['GET','POST'])
def squareroot():
    if request.method == 'POST':
        num = request.form ['a']
        result = math.sqrt(int(num))
        return render_template('squareroot_view.html',num = int(num),result=int(result))
    return render_template('squareroot.html')


@app.route('/convert_number')
def convert():
    return render_template('convert_number.html')

if __name__ == '__main__':

    app.run(debug=True)