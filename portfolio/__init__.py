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
        'categories': ['python', 'bash', 'mysql', 'mongodb'],
        'slug': 'kindle-book-store',
        'source':'https://github.com/chiziheng/Database-and-Big-Data',
        'slides':'https://docs.google.com/presentation/d/1EGe92sxmQs03YbdXCRq2yzFKlqZGuchA/edit?usp=sharing&ouid=100745558896256792063&rtpof=true&sd=true'
    },
    {
        'name': 'Tweet Sentiment Analysis',
        'thumb': 'img/sentiment_analysis.png',
        'hero': 'img/sentiment_analysis_hero.jpeg',
        'categories': ['R', 'Kera', 'Machine Learning'],
        'slug': 'sentiment-analysis',
        'source': 'https://github.com/chiziheng/Kaggle-Data-Competition',
        'report': 'https://drive.google.com/file/d/18oKoGKipbb65vIHJ-CrJyH0MQnKSwkl0/view?usp=sharing'
    },
    {
        'name': 'Time Series Forecasting',
        'thumb': 'img/time_series_forecasting.jpg',
        'hero': 'img/time_series_forecasting_hero.png',
        'categories': ['Python', 'Pandas', 'Matplotlib', 'ARIMA'],
        'slug': 'time-series-forecasting',
        'report': 'https://drive.google.com/file/d/1-bhPJ8F3Mo7CIIH1EogzHLxSoccx4que/view?usp=sharing',
        'poster': 'https://drive.google.com/file/d/1-afOqqY6LBFnypQZ6rUor4RFJQe1EIzQ/view?usp=sharing'
    },
    {
        'name': 'Joy Website',
        'thumb': 'img/joy_web.png',
        'hero': 'img/joy_website_hero.png',
        'categories': ['Python', 'Flask', 'HTML', 'CSS'],
        'slug': 'joy-website',
        'prod':'https://joywebsite.herokuapp.com/',
        'source': 'https://github.com/chiziheng/joy-website'
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