from bs4 import BeautifulSoup
from flask.templating import render_template
import requests
from flask import Flask


def source_albany():
        source_weather = requests.get('https://wnyt.com/weather/')
        soup = BeautifulSoup(source_weather.content, 'html.parser')
        title = soup.title.text

        locate_weather = soup.find('div', class_='col-xs-12 col-sm-4 text-center')
        weather_albany = locate_weather.text
        general_info = soup.find('div', class_='col-xs-6 col-sm-4')
        info = general_info.text

