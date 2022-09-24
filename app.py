from flask import Flask, render_template, request, redirect
import hue
import logging


app = Flask(__name__)


# Connect to the latest used bridge
b = hue.connect_to_latest_bridge()


# Route for the home page
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="home")


# Route for the register page
@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html", title="Register")


# Route for the login page
@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html", title="Login")


# Route for the control page
@app.route("/control_page", methods=["GET"])
def control_page():
    return render_template(
        "control_page.html",
        title="Control page",
        lights_list=hue.get_lights(b),
        groups_list=hue.get_groups(b),
    )


# Route for the features page
@app.route("/features", methods=["GET"])
def features():
    return render_template("features.html", title="Features")


# Route for the about page
@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", title="About")


# Route for the settings page
@app.route("/settings", methods=["GET"])
def settings():
    return render_template(
        "settings.html",
        title="Settings",
        bridges_list=hue.get_bridges(),
        )


# Route update the bridge ip
@app.route("/settings/bridge/<bridge_ip>", methods=["POST"])
def update_bridge_ip(bridge_ip):
    hue.update_bridge_ip(bridge_ip)
    global b
    b = hue.connect_to_latest_bridge()
    return redirect("/settings")


# Route to turn on the lights
@app.route("/light/<light_id>/on", methods=["POST"])
def light_on(light_id):
    light_id = int(light_id)
    if request.method == 'POST':
        hue.light_on(b, light_id)

    return redirect('/control_page')


# Route to turn off the lights
@app.route("/light/<light_id>/off", methods=["POST"])
def light_off(light_id):
    light_id = int(light_id)
    if request.method == 'POST':
        hue.light_off(b, light_id)

    return redirect('/control_page')


# Route to change the brightness
@app.route("/light/<light_id>/brightness", methods=["POST"])
def light_brightness(light_id):
    light_id = int(light_id)
    if request.method == 'POST':
        brightness = request.form['brightness']
        brightness = int(brightness)
        hue.set_light_brightness(b, light_id, brightness)

    return redirect('/control_page')


# Route to change the color
@app.route("/light/<light_id>/color", methods=["POST"])
def light_color(light_id):
    light_id = int(light_id)
    if request.method == 'POST':
        hue.set_light_color(b, light_id, request.form['color'])

    return redirect('/control_page')


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=80)
