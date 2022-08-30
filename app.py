from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'asadlahorikhan@gmail.com'  # enter your email here
app.config['MAIL_DEFAULT_SENDER'] = 'john.rory2002@gmail.com' # enter your email here
app.config['MAIL_PASSWORD'] = 'oqhexhptbzcgokrh' # enter your password here

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        name = request.json['name']
        email = request.json['email'].replace(' ', '').lower()
        message = request.json['message']
        try:
            msg = Message('MyPortfolio', sender = 'asadlahorikhan@gmail.com', recipients = ['john.rory2002@gmail.com'])
            msg.body = f"Here is the email send from my portfolio website: \n Name: {name}, \n Email: {email}, \n Message: {message}"
            mail.send(msg)
            return jsonify({'name': 'Message Send Successfully!'})
        except Exception:
            return jsonify({'error': 'Message Not Send, Sorry'})

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
