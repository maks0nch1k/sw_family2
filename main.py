from flask import Flask, render_template

app = Flask(__name__)


def main():
    app.run(port='5000', host="127.0.0.1")


@app.route("/")
def main_page():
    return render_template("index.html", title="Учебник-справочник по конструкторам R:ED")


if __name__ == "__main__":
    main()