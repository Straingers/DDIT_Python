from flask import Flask, jsonify, render_template, request
import urllib.request

app = Flask(__name__, static_url_path='')

@app.route('/')
def call_API():
    return render_template('capcha.html') 
    
@app.route('/image', methods=['post'])
def getImage():
    client_id = "8n5HNgptJo80fs1ro_xK"
    client_secret = "jXwfwq4hXt"
    code = "0"
    url = "https://openapi.naver.com/v1/captcha/nkey?code=" + code
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        key = response_body.decode('utf-8').split(":")[1].replace('"', "").replace("}","")
    else:
        print("Error Code:" + rescode)
    url = "https://openapi.naver.com/v1/captcha/ncaptcha.bin?key=" + key
    return jsonify(url = url, key = key)

@app.route('/compare')  
def compare():
    client_id = "8n5HNgptJo80fs1ro_xK"
    client_secret = "jXwfwq4hXt"
    code = "1"
    key = request.args.get('imgkey')
    value = request.args.get('value')
    url = "https://openapi.naver.com/v1/captcha/nkey?code=" + code + "&key=" + key + "&value=" + value
    nrequest = urllib.request.Request(url)
    nrequest.add_header("X-Naver-Client-Id",client_id)
    nrequest.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(nrequest)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        return response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)

if __name__ == '__main__':
        app.run(debug=True)