from project_files import app
from flask import Flask, render_template, url_for, redirect, flash
from project_files.form import City
from project_files.translator import translator
from project_files.key import Key
import os
import requests


@app.route('/', methods=['GET', 'POST'])
def forecast():
  form = City()
  list_to_send = ()
  if form.validate_on_submit():
    city = form.name.data
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+ city + Key
    response = requests.get(url).json()
    state = response['weather'][0]['main']
    icon = response['weather'][0]['icon']
    icon = icon[0] + icon[1] + 'd.png'
    description = response['weather'][0]['description']
    # translation = translator.translate(description)
    # description = translation
    temperature = round(int(response['main']['temp']) -  273,15)
    humidity = response['main']['humidity']
    wind = response['wind']['speed']
    short_name = response['sys']['country']
    city_name = response['name']
    icon = os.path.join(app.config['UPLOAD_FOLDER'],icon)
    list_to_send = state, description , temperature, wind, short_name, city_name, icon, humidity
    return render_template('weather.html', list_to_send=list_to_send, city_name=city_name, icon=icon, description=description)
  return render_template('form.html', form=form)



@app.errorhandler(404)
def handle_404(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def handle_500(e):
    return render_template('500.html'), 500