from flask import Flask, render_template, request, flash, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    number1 = request.form["number1"]
    number2 = request.form["number2"]
    operation = request.form["operation"]

    if number1.isdigit() and number2.isdigit():
        num1 = int(number1)
        num2 = int(number2)

        if operation == "add":
            result = num1 + num2
            flash(f"Результат: {result}")
        elif operation == "multiply":
            result = num1 * num2
            flash(f"Результат: {result}")
        elif operation == "power":
            result = num1 ** num2
            flash(f"Результат: {result}")
        elif operation == "divide":
            if num2 != 0:
                result = num1 // num2
                flash(f"Результат: {result}")
            else:
                flash(f"Ошибка: деление на ноль!")
    else:
        flash("Ошибка, введите корректные числа")

    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)