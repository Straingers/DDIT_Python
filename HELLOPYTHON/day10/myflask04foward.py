from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    title = "리스트 보기"
    mylist = ["최윤성", "김이현", "공슬기", "김민지"]
    objlist = []
    objlist.append({"e_id" : "1", "e_name" : "1", "birth" : "1"})
    objlist.append({"e_id" : "2", "e_name" : "2", "birth" : "2"})
    
    return render_template('index.html', title=title, mylist=mylist, objlist=objlist)

if __name__ == '__main__':
    app.run(debug=True)