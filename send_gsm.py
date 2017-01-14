from pyfcm import FCMNotification
import os

def send_push_notification(fcm_token, nfc_id):
    push_service = FCMNotification(api_key=os.environ['FCM_KEY'])
    registration_id = fcm_token
    message_title = "ThoughtWorks"
    message_body = nfc_id
    push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                               message_body=message_body)


