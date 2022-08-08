from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

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
        read_csv = pd.read_csv('static/contact_data.csv')

        if (record['email'].to_numpy())[0] not in read_csv['email'].to_numpy():
            record_to_csv = record.to_csv(
                'static/contact_data.csv', mode='a', index=False, header=False)
            
        return render_template('index.html', to_csv=record_to_csv)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
