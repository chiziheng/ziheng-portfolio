import os
import json

from flask import Flask, render_template, abort, request, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv

from portfolio.model.form import ContactForm

load_dotenv()

app = Flask(__name__)
mail = Mail(app)

SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY

# Configure flask mail
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = os.environ.get("SERVER_EMAIL")
app.config["MAIL_PASSWORD"] = os.environ.get("SERVER_PASSWORD")
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
mail = Mail(app)

projects_list = [
    {
        "name": "Personal Website",
        "thumb": "img/ziheng_web.png",
        "hero": "img/ziheng_nz_hero.jpg",
        "categories": ["Python", "Flask", "HTML", "CSS"],
        "slug": "ziheng-website",
        "prod": "https://joywebsite.herokuapp.com/",
    },
    {
        "name": "Online Kindle Book Store",
        "thumb": "img/database_big_data.jpg",
        "hero": "img/database_big_data_hero.png",
        "categories": ["python", "bash", "mysql", "mongodb"],
        "slug": "kindle-book-store",
        "source": "https://github.com/chiziheng/Database-and-Big-Data",
        "slides": "https://docs.google.com/presentation/d/1EGe92sxmQs03YbdXCRq2yzFKlqZGuchA/edit?usp=sharing&ouid=100745558896256792063&rtpof=true&sd=true",
    },
    {
        "name": "Tweet Sentiment Analysis",
        "thumb": "img/sentiment_analysis.png",
        "hero": "img/sentiment_analysis_hero.jpeg",
        "categories": ["R", "Kera", "Machine Learning"],
        "slug": "sentiment-analysis",
        "source": "https://github.com/chiziheng/Kaggle-Data-Competition",
        "report": "https://drive.google.com/file/d/18oKoGKipbb65vIHJ-CrJyH0MQnKSwkl0/view?usp=sharing",
    },
    {
        "name": "Time Series Forecasting",
        "thumb": "img/time_series_forecasting.jpg",
        "hero": "img/time_series_forecasting_hero.png",
        "categories": ["Python", "Pandas", "Matplotlib", "ARIMA"],
        "slug": "time-series-forecasting",
        "source": "https://github.com/chiziheng/Data-and-Business-Analytics",
        "poster": "https://drive.google.com/file/d/1-afOqqY6LBFnypQZ6rUor4RFJQe1EIzQ/view?usp=sharing",
    },
    {
        "name": "Joy Website",
        "thumb": "img/joy_web.png",
        "hero": "img/joy_website_hero.png",
        "categories": ["Python", "Flask", "HTML", "CSS"],
        "slug": "joy-website",
        "prod": "https://joywebsite.herokuapp.com/",
        "source": "https://github.com/chiziheng/joy-website",
    },
]

slug_to_project = {project["slug"]: project for project in projects_list}


@app.route("/")
def about():
    return render_template("about.html")


@app.route("/projects")
def projects():
    return render_template("projects.html", projects_list=projects_list)


@app.route("/resume")
def resume():
    return render_template("resume.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        res_json = json.dumps(
            {"name": name, "email": email, "subject": subject, "message": message}
        )

        try:
            print(os.environ.get("SERVER_EMAIL"))
            msg = Message(
                sender="JoyWebsiteServer@gmail.com", recipients=["zihengchi@gmail.com"]
            )
            msg.body = res_json
            mail.send(msg)
        except Exception as e:
            print(f"Failed to send email from contact form, the error message is : {e}")

        return redirect(url_for(".contact"))
    else:
        return render_template("contact.html", form=form)


@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])
