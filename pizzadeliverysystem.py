from flask import Flask, render_template, request, send_from_directory
import sqlite3

application = Flask(__name__, static_url_path='/static')


@application.route("/")
def index():
    with sqlite3.connect(("data.db")) as conn:
        command = "Select * From table"
        conn.execute(command)
        table = conn.execute(command)
        assignment_list = table.fetchall()
        return render_template("htmlkode.html")


@application.route("/htmlkode", methods=('get', 'POST'))
def htmlkode():
    if request.method == "POST":
        with sqlite3.connect("data.db") as conn:
            command = "INSERT INTO pizza VALUES (?, ?, ?,)"
        list = []
        list.append(request.form['radio1'])
        list.append(request.form['Green Pepper'])
        list.append(request.form['Mushroom'])
        list.append(request.form['Tomato'])
        list.append(request.form['Pickles'])
        list.append(request.form['Olives'])
        list.append(request.form['UnitPrice'])
        list.append(request.form['UnitNumber'])
        list.append(request.form['Totals'])
    conn.execute(command, list)
    conn.commit()
    return render_template(htmlkode.html)


   if __name__ == "__main__":
    application.run(debug=True)
