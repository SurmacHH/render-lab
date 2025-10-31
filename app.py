from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Изменённая версия приложения на Render!"

if __name__ == "__main__":
    app.run()
