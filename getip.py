from flask import request,Flask
import time

app = Flask(__name__)

@app.route('/ip', methods=['GET']) 

def get():
    ip = request.headers['X-Real-Ip']
    with open ("/getip/log", 'a+') as f:
        f.write(time.strftime('[%Y-%m-%d %H:%M:%S]') + " IP: %s\n" % ip)
    f.close()

    return ip

if __name__=='__main__':
    app.run("0.0.0.0", 8000)
