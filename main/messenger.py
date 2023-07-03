import sqlite3
from sqlite3 import Error
import firebase_admin
from firebase_admin import credentials

from pyfcm import FCMNotification
fcm = FCMNotification(api_key="AAAAELqEgtA:APA91bHp3sEYR1_fdZOi-_xlAEEGZEUo-jHyLH3Tl8qXERWkGdVqcBeWGLVvtoF5dACWl6n1frMRSv5IPW4upcnZObY03VaA-5UDUp51zUwvQk5kiRSwMeq7ZeywXZkCOy50M4xqbLZs")

cred = credentials.Certificate("C:\school\main\key.json")
firebase_admin.initialize_app(cred)

def send_messages(data):
    registration_tokens = data["tokens"]
    message_title = data["title"]
    message_body = data["message"]
    result = fcm.notify_multiple_devices(registration_ids=registration_tokens, message_title=message_title, message_body=message_body)