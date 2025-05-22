from flask import Flask, request

app = Flask(__name__)

PERSONAL_DATA = {
    "Прізвище": "Хоменко",
    "Ім'я": "Дарія",
    "Курс": "2",
    "Група": "ІС-33"
}

MY_LOGIN = "dariikhom"

@app.route('/<login>')
def index(login):
    if login == MY_LOGIN:
        response = (
            f"<h1>Особисті дані студента</h1>"
            f"<p>Прізвище: {PERSONAL_DATA['Прізвище']}</p>"
            f"<p>Ім'я: {PERSONAL_DATA['Ім\'я']}</p>"
            f"<p>Курс: {PERSONAL_DATA['Курс']}</p>"
            f"<p>Група: {PERSONAL_DATA['Група']}</p>"
        )
    else:
        response = f"<h2>Помилка: Невідомий логін '{login}'</h2>"
    return response

if __name__ == '__main__':
    app.run(debug=True)
