from flask import Flask, render_template, request, jsonify
from day10.mydao_exam import DaoExam

app = Flask(__name__, static_url_path='')

@app.route('/')
@app.route('/examlist')
def examlist():
    de = DaoExam()
    mylist = de.myselect()
    return render_template('examcrud.html', mylist=mylist) 

@app.route('/add.exam', methods=['post'])
def exam_add():
    param = request.get_json()
    de = DaoExam()
    cnt = de.myinsert(param['e_id'], param['kor'], param['eng'], param['math'])
    msg = 'ng'
    if cnt == 1:
        msg = 'ok'
    return jsonify(msg = msg)

@app.route('/upd.exam', methods=['post'])
def exam_upd():
    param = request.get_json()
    de = DaoExam()
    cnt = de.myupdate(param['e_id'], param['kor'], param['eng'], param['math'])
    msg = 'ng'
    if cnt == 1:
        msg = 'ok'
    return jsonify(msg = msg)

@app.route('/del.exam', methods=['post'])
def exam_del():
    param = request.get_json()
    de = DaoExam()
    cnt = de.mydelete(param['e_id'])
    msg = 'ng'
    if cnt == 1:
        msg = 'ok'
    return jsonify(msg = msg)

if __name__ == '__main__':
    app.run(debug=True)