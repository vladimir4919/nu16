from flask import Flask, render_template, request
from class_hh import Parser_HH

app = Flask(__name__)


@app.route("/")
def index():
    # Возвращаем главную страницу
    return render_template('index.html', name='ПарсерFlask')


@app.route('/contacts/')
def contacts():
    #запись в страницу контактов
    context = {
        'name': 'Владимир Воробьев',
        'mail': "bfine@mail.ru",
        'phone': +79009990747,
        'phone_university': '8(495) 223-32-22'
    }
    return render_template('contacts.html', context=context)


@app.route('/run/', methods=['GET'])
def run_get():
    text = 'Ищем вакансию в одном из городов России'
    return render_template('forma.html', text=text)


@app.route('/run/', methods=['POST'])
def run_post():
    """Запросы в парсер по названию города и вакансии"""
    QUESTIONS = request.form['QUESTIONS']
    CITY = request.form['CITY']
    vacancy = Parser_HH(QUESTIONS, CITY)
    return render_template('results.html',
                           vacancy=vacancy.vacancies_found(),
                           list_salary_mean=vacancy.list_salary_mean(),
                           CITY=CITY,
                           QUESTIONS=QUESTIONS,
                           #key_skills=vacancy.key_skills(),

                           )


if __name__ == "__main__":
    app.run(debug=True)