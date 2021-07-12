from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('index.html', row=8, column=8, color1='red', color2='black')

@app.route('/<int:rowx>')
def checkerboard2(rowx):
    return render_template('index.html', row=rowx, column=8, color1='red', color2='black')


@app.route('/<int:row>/<int:column>')
def checkerboard3(row,column):
    return render_template('index.html', row=row, column=column, color1='red', color2='black')

@app.route('/<int:rowc>/<int:columnc>/<string:color1>/<string:color2>')
def checkerboard4(rowc,columnc,color1,color2):
    return render_template('index.html', row=rowc, column=columnc, color1=color1,color2=color2)

if __name__=="__main__":
    app.run(debug=True)