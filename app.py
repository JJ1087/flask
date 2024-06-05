from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return'''
        <html>
            <body>
                <h1>Jeziel Gonzalez Antonio 9no A</h1>
                <img src="/static/saludo.webp" alt="Saludos">
                <form id="greetForm" method="post">
                    <label for="first_name">¿Cual es tu nombre?</label>
                    <input type="text" id="first_name" name="first_name"><br>
                    <label for="last_name">¿Cual es tu apellido?</label>
                    <input type="text" id="last_name" name="last_name"><br><br>
                    <input type="button" value="Enviar" onclick="submitForm()">
                </form>
                <label id="greetingLabel"></label>
            </body>
            <script>
                function submitForm() {
                    var firstName = document.getElementById('first_name').value;
                    var lastName = document.getElementById('last_name').value;
                    document.getElementById('greetingLabel').innerText = `Hola ${firstName} ${lastName}!`;
                }
            </script>
        </html>"
    '''


if __name__ == '__main__':
    app.run(debug=True)

