from flaskblog.secrets import Secrets

class Config:
    secretsObj = Secrets()
    SECRET_KEY = "hey"  # or use a random string
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"  # ✅ valid SQLite URL
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "jey"
    MAIL_PASSWORD = "jey"
