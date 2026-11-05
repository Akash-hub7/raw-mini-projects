from flask import Flask, render_template, request, redirect, url_for

from contact import (
    initialize_database,
    add_contact,
    get_contacts,
    delete_contact
)

app = Flask(__name__)

# Initialize Database
initialize_database()


# HOME / DASHBOARD
@app.route("/")
def home():
    contacts = get_contacts()
    return render_template("front.html", contacts=contacts)


# ALL CONTACTS
@app.route("/contacts")
def all_contacts():
    contacts = get_contacts()
    return render_template("contacts.html", contacts=contacts)


# ADD CONTACT
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":

        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form.get("email", "")

        add_contact(name, phone, email)

        return redirect(url_for("home"))

    return render_template("add_contact.html")


# DELETE CONTACT
@app.route("/delete/<int:contact_id>", methods=["POST"])
def delete(contact_id):
    delete_contact(contact_id)
    return redirect(url_for("home"))


# RUN APPLICATION
if __name__ == "__main__":
    app.run(debug=True)
