from flask import Flask
import logging
from send_gsm import send_push_notification
from test_mlab import get_fcm_token

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG, filename='flasklog.log')


@app.route('/device/<device_id>/<nfc_id>')
def give_greeting(device_id, nfc_id):
    fcm_token = get_fcm_token(device_id)
    send_push_notification(fcm_token, nfc_id)

    logging.info("Received data from device id " + device_id)
    logging.info("Received nfc id " + nfc_id)
    return 'Got device id ' + device_id + ' nfc id ' + nfc_id


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
