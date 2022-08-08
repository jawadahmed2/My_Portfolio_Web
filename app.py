from flask import Flask, render_template

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'asadlahorikhan@gmail.com'
app.config['MAIL_PASSWORD'] = 'Asad1990'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


def sendContactForm(result):
    msg = Message("Contact Form from my Portfolio Website",
                  sender="asadlahorikhan@gmail.com",
                  recipients=["jawad.kohat2002@gmail.com"])

    msg.body = """
    Hello there,
    You just received a contact form.
    Name: {}
    Email: {}
    Message: {}
    """.format(result['name'], result['email'], result['message'])

    mail.send(msg)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        result = {'name': request.form['name'], 'email': request.form['email'].replace(' ', '').lower()}

        result['message'] = request.form['message']
        sendContactForm(result)
        
        return render_template('contact.html', **locals())

    return render_template('contact.html', **locals())


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
