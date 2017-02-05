from flask import Flask, render_template
from flask import request

from algorithm_1 import Sudoku

app = Flask(__name__)
TREND_LENGTH_THRESHOLD = 2
CATID_PAR = 'cat_id'
USER_ID = 'user_name'
CATID_ALL = range(1, 14)


@app.route('/sudoku_main')
def sudoku_main():
    return render_template("sudoku.html")


@app.route('/sudoku', methods=["POST"])
def sudoku():
    text = request.form['su11']
    data = list()
    for i in range(9):
        d = list()
        for j in range(9):
            text = request.form['su%s%s' % (i, j)]
            print text
            # text=""
            if text.isdigit():
                text = int(text)
                if 0 < text <= 9:
                    d.append(text)
                else:
                    d.append(0)
            else:
                d.append(0)
        data.append(d)
    print data
    su = Sudoku(data)
    su.resolve()
    result = [su.data[i * 9: (i+1) * 9] for i in range(9)]
    print result
    print text
    print "Hello"
    return render_template("sudoku_result.html", data=result)
    pass


if __name__ == '__main__':
    app.run(host="localhost", port=12345, debug=True)
