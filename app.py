from flask import Flask, render_template, request
import socket
import requests

app = Flask(__name__)

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=3)
        return response.json().get('ip', 'Tidak terdeteksi')
    except:
        return "Tidak terdeteksi"

def get_local_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except:
        return "127.0.0.1"

@app.route('/')
def show_ip():
    client_ip = request.remote_addr
    return render_template('index.html',
        public_ip=get_public_ip(),
        local_ip=get_local_ip(),
        client_ip=client_ip
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
