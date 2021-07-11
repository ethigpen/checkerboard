from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('index.html', row=8, column=8)

@app.route('/<int:rowx>')
def checkerboard2(rowx):
    boxxes= rowx*8
    sizex=8*75
    if(boxxes%2==0):
        boxxes=int(boxxes/2)
        return render_template('index.html', boxes=boxxes, extrabox=0, size=sizex)
    elif(boxxes%2!=0):
        boxxes -=1
        boxxes=int(boxxes/2)
        extraboxx=1
        return render_template('index.html', boxes=boxxes, extrabox=extraboxx, size=sizex)


@app.route('/<int:row>/<int:column>')
def checkerboard3(row,column):
    boxes= row*column
    size=column*75
    if(boxes%2==0):
        boxes=int(boxes/2)
        return render_template('index.html', boxes=boxes, extrabox=0, size=size)
    elif(boxes%2!=0):
        boxes -=1
        boxes=int(boxes/2)
        extrabox=1
        return render_template('index.html', boxes=boxes, extrabox=extrabox, size=size)





if __name__=="__main__":
    app.run(debug=True)