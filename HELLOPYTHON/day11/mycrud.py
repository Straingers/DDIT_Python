from flask import Flask, render_template, request, jsonify
from day11.mydao_emp import DaoEmp

app = Flask(__name__, static_url_path='')

@app.route('/')
@app.route('/list')
def list():
    de = DaoEmp()
    mylist = de.myselect()
    return render_template('list.html', mylist=mylist) 

@app.route('/add.ajax')
def ajax_add():
    p = request.get_json()
    de = DaoEmp()
    cnt = de.myinsert(p['e_id'], p['e_name'], p['birth'])
    msg = "ng"
    if cnt == 1:
        msg = "ok"
    return jsonify(msg = msg)

@app.route('/upd.ajax')
def ajax_upd():
    p = request.get_json()
    de = DaoEmp()
    cnt = de.myupdate(p['e_id'], p['e_name'], p['birth'])
    msg = "ng"
    if cnt == 1:
        msg = "ok"
    return jsonify(msg = msg)

@app.route('/del.ajax', methods=['POST'])
def ajax_del():
    p = request.get_json()
    de = DaoEmp()
    cnt = de.mydelete(p['e_id'])
    msg = "ng"
    if cnt == 1:
        msg = "ok"
    return jsonify(msg = msg)

if __name__ == '__main__':
    app.run(debug=True)