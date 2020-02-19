from flask import Flask, render_template, request, send_from_directory
from Database import Data

application = Flask(__name__, static_url_path='/static')


@application.route("/cart")
def cart():
    pizza_data = Data()
    data_list = pizza_data.get_data("pizza")
    return render_template("cart.html", orders=data_list)


@application.route("/")
@application.route("/htmlkode", methods=('get', 'POST'))
def htmlkode():
    if request.method == "POST":

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

        pizza_data = Data(list)
        pizza_data.add_data()

    return render_template("htmlkode.html")


if __name__ == "__main__":
    application.run(debug=True)
