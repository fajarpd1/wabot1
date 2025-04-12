from flask import Flask, request

app = Flask(__name__)
VERIFY_TOKEN = '1032752925455574|rfvm7KPBrMKMdydcdcKX4cTMbbE'  

@app.route('/')
def index():
    return 'Webhook is alive!'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return 'Verification failed', 403

    if request.method == 'POST':
        data = request.get_json()
        print("Pesan masuk:", data)
        return "OK", 200

if __name__ == '__main__':
    app.run()
