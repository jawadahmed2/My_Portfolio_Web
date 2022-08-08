from flask import Flask, render_template, request
import pandas as pd
# from flask_mail import Mail,Message
app = Flask(__name__)

# app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'asadlahorikhan@gmail.com'
# app.config['MAIL_DEFAULT_SENDER'] = 'asadlahorikhan@gmail.com'
# app.config['MAIL_PASSWORD'] = 'Asad1990'


# mail = Mail(app)


# def sendContactForm(result):
#     msg = Message("Contact Form from my Portfolio Website",
#                   sender="asadlahorikhan@gmail.com",
#                   recipients=["jawad.kohat2002@gmail.com"])

#     msg.body = """
#     Hello there,
#     You just received a contact form.
#     Name: {}
#     Email: {}
#     Message: {}
#     """.format(result['name'], result['email'], result['message'])

#     mail.send(msg)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        result = {'name': request.json['name'], 'email': request.json['email'].replace(
            ' ', '').lower()}

        result['message'] = request.json['message']
        record = pd.DataFrame([result])
        read_csv = pd.read_csv('contact_data.csv')

        if (record['email'].to_numpy())[0] not in read_csv['email'].to_numpy():
            record_to_csv = record.to_csv(
                'contact_data.csv', mode='a', index=False, header=False)
        # sendContactForm(result)
        return render_template('index.html')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
