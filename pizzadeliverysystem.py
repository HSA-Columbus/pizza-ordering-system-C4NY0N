from flask import Flask, render_template, request, send_from_directory
import sqlite3

application = Flask(__name__, static_url_path='/static')


@application.route("/cart")
def index():
    with sqlite3.connect(("data")) as conn:
        command = "Select * From pizza"
        table = conn.execute(command)
        assignment_list = table.fetchall()
        return render_template("cart.html", orders=assignment_list)


@application.route("/")
@application.route("/htmlkode", methods=('get', 'POST'))
def htmlkode():
    if request.method == "POST":
        with sqlite3.connect("data") as conn:
            command = "INSERT INTO pizza VALUES (?, ?, ?, ?, ?)"
        list = []
        additions = ""
        additions += request.form['Green_Pepper'] if request.form.get("Green_Pepper", None) is not None else " "
        additions += request.form['Mushroom'] if request.form.get("Mushroom", None) is not None else " "
        additions += request.form['Tomato'] if request.form.get("Tomato", None) is not None else " "
        additions += request.form['Pickles'] if request.form.get("Pickles", None) is not None else " "
        additions += request.form['Olives'] if request.form.get("Olives", None) is not None else " "
        list.append(request.form['radio1'])
        list.append(additions)
        list.append(request.form['UnitNumber'])
        list.append(request.form['UnitPrice'])
        list.append(request.form['Totals'])
        conn.execute(command, list)
        conn.commit()
    return render_template("htmlkode.html")


if __name__ == "__main__":
    application.run(debug=True)
