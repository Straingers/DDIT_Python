from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=['get', 'post'])
def hello():
    a = request.args.get("a", "")
    if request.method == 'post':
        a = request.form.get("a", "")
    return "Hello! {}".format(a)

if __name__ == '__main__':
    app.run(debug=True)