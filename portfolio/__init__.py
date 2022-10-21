from flask import Flask, render_template, abort

app = Flask(__name__)

projects_list = [
    {
        'name': 'Personal Website',
        'thumb': 'img/ziheng_web.png',
        'hero': 'img/ziheng_nz_hero.jpg',
        'categories': ['Python', 'Flask', 'HTML', 'CSS'],
        'slug': 'ziheng-website',
        'prod':'https://joywebsite.herokuapp.com/'
    },
    {
        'name': 'Online Kindle Book Store',
        'thumb': 'img/database_big_data.jpg',
        'hero': 'img/database_big_data_hero.png',
        'categories': ['python', 'spark', 'mysql', 'mongodb'],
        'slug': 'kindle-book-store',
        'prod':''
    },
    {
        'name': 'Tweet Sentiment Analysis',
        'thumb': 'img/sentiment_analysis.png',
        'hero': 'img/sentiment_analysis_hero.png',
        'categories': ['R', 'Kera', 'Tensorflow'],
        'slug': 'sentiment-analysis',
        'prod':''
    },
    {
        'name': 'Time Series Forecasting',
        'thumb': 'img/time_series_forecasting.jpg',
        'hero': 'img/time_series_forecast_hero.png',
        'categories': ['Python', 'Pandas', 'Matplotlib', 'ARIMA'],
        'slug': 'time-series-forecasting',
        'prod':''
    },
    {
        'name': 'Joy Website',
        'thumb': 'img/joy_web.png',
        'hero': 'img/joy_website_hero.png',
        'categories': ['Python', 'Flask', 'HTML', 'CSS'],
        'slug': 'joy-website',
        'prod':'https://joywebsite.herokuapp.com/'
    },
]

slug_to_project = {project['slug']: project for project in projects_list}

@app.route('/')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    return render_template('projects.html', projects_list=projects_list)

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project/<string:slug>')
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f'project_{slug}.html', project=slug_to_project[slug])