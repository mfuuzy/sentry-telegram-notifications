# @Time    : 2023/11/7 15:35
# @FileName: main.py
# @Software: PyCharm
# @author  : mfuuzy

import requests
from flask import Flask, request, abort

app = Flask(__name__)

apiToken = "123456:aaF2121afdsafda2MCfumyD00dVF9E"
chatID = 800000000
apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'


@app.route('/sentry-report', methods=['POST'])
def webhook():
    if request.method == 'POST':
        message = request.json
        # print(message.get('data').get('metric_alert').get('projects'))
        response = requests.post(apiURL, data={'chat_id': chatID,
                                               'text': f"<b>Sentry Alert</b> 🔥\n\nAction: {message.get('action')}\n"
                                                       f"Project: {message.get('data').get('event').get('project')}"
                                                       f"\nMessage: {message.get('data').get('event').get('message')}"
                                                       f"\nUrl: {message.get('data').get('event').get('web_url')}",
                                               'parse_mode': 'html'})

        # print(f'Telegram response - {response.text}')
        return 'Success', response.status_code
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
