import pyrebase
import pickle
import os
import firebase_admin
from firebase_admin import auth as firebase_auth
from firebase_admin import credentials


cred = credentials.Certificate("service_account.json")
firebase_admin.initialize_app(cred)

firebaseConfig = {
    "apiKey": "AIzaSyCqf4NiF5AeaJADg944J-I1AMHq95GpZgg",
    "authDomain": "fletauth2-57a9c.firebaseapp.com",
    "projectId": "fletauth2-57a9c",
    "storageBucket": "fletauth2-57a9c.appspot.com",
    "messagingSenderId": "800924007682",
    "appId": "1:800924007682:web:037c87109647dbd5c2d61b",
    "measurementId": "G-1TNKMVCBJG",
    "databaseURL": "https://fletauth2-57a9c-default-rtdb.firebaseio.com/",
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


def create_user(name, email, password):
    try:
        user = firebase_auth.create_user(
            email=email, password=password, display_name=name
        )
        return user.uid
    except:
        return None


def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user["idToken"]
    except:
        return None


def store_session(token):
    if os.path.exists("token.pickle"):
        os.remove("token.pickle")
    with open("token.pickle", "wb") as f:
        pickle.dump(token, f)
