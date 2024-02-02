from flask import Flask, render_template, make_response, jsonify
from data import db_session
from data.controllers import Controller


app = Flask(__name__)


def main():
    db_session.global_init("db/products.db")
    app.run(port='5000', host="127.0.0.1")


@app.route("/")
def main_page():
    return render_template("index.html", title="Учебник-справочник по конструкторам R:ED")


@app.route("/controllers")
def controllers():
    return render_template("controllers.html", title="Контроллеры конструкторов R:ED")


@app.route("/performers")
def performers():
    return render_template("base.html", title="Исполнители конструкторов R:ED")


@app.route("/sensors")
def sensors():
    return render_template("base.html", title="Датчики конструкторов R:ED")


@app.route("/software")
def software():
    return render_template("base.html", title="Программирование R:ED | Драйвера и ПО")


@app.route("/sets")
def sets():
    return render_template("base.html", title="Комплектации")


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


if __name__ == "__main__":
    main()