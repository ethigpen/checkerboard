from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('index.html', row=8, column=8)

@app.route('/<int:rowx>')
def checkerboard2(rowx):
    return render_template('index.html', row=rowx, column=8)

@app.route('/<int:row>/<int:column>')
def checkerboard3(row,column):
    return render_template('index.html', row=row, column=column)





if __name__=="__main__":
    app.run(debug=True)