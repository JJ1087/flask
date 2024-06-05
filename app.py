from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return'''
        <html>
            <body>
                <h1>Jeziel Gonzalez Antonio 9no A</h1>
                <img src="/static/saludo.webp" alt="Saludos">
            </body>
        </html>"
    '''

if __name__ == '__main__':
    app.run(debug=True)

