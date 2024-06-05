from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Jeziel Gonzalez Antonio 9no A"

if __name__ == '__main__':
    app.run(debug=True)

