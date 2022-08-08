from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# @app.route("/contact", methods=["GET", "POST"])
# def contact():  # sourcery skip: last-if-guard
#     if request.method == 'POST':
#         result = {'name': request.json['name'], 'email': request.json['email'].replace(
#             ' ', '').lower()}

#         result['message'] = request.json['message']
#         record = pd.DataFrame([result])
#         sheet_id = '12dE0RkoPrnbK5CQax6oWjDjz_I6ijUEjnvk68nC8yeA'
#         read_csv = pd.read_csv(
#             f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv')
#         if (record['email'].to_numpy())[0] not in read_csv['email'].to_numpy():
#             credential = ServiceAccountCredentials.from_json_keyfile_name("static/inlaid-tribute-358817-f455c0373ef9.json",
#                                                                           ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file",  "https://www.googleapis.com/auth/drive"])

#             client = gspread.authorize(credential)
#             gsheet = client.open("contact_data").sheet1
#             new_row = gsheet.append_row(
#                 list(result.values()), table_range="A1")
#             # record_to_csv = record.to_csv(
#             #     f'https://docs.google.com/spreadsheets/d/{sheet_id}/edit?format=csv', mode='a', index=False, header=False)
#             # print('yes')

#         return render_template('index.html', to_gsheet=new_row)
#     return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
