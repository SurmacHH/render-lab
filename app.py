from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Привет, Render! Это моё первое PaaS-приложение."

if __name__ == "__main__":
    app.run()
