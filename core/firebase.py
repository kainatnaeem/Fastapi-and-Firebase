import firebase_admin
from firebase_admin import credentials, auth
import pyrebase
from dotenv import load_dotenv
import os
load_dotenv()
# ---------- Admin SDK (for create user, verify token, firestore etc) ----------
if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

firebase_auth_admin = auth


# ---------- Pyrebase (for login/password auth) ----------
firebaseConfig = {
   "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
  "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
firebase_auth = firebase.auth()