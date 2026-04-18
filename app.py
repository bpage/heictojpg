import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/dmca")
def dmca():
    return render_template("dmca.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory(
        os.path.dirname(__file__), "sitemap.xml", mimetype="application/xml"
    )


@app.route("/robots.txt")
def robots():
    return send_from_directory(
        os.path.dirname(__file__), "robots.txt", mimetype="text/plain"
    )


@app.route("/ads.txt")
def ads_txt():
    return send_from_directory("static", "ads.txt")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
