from bs4 import BeautifulSoup
from flask.templating import render_template
import requests
from flask import Flask


def source_boston():
    source_boston = requests.get('https://www.bbc.com/weather/4930956')
    soup = BeautifulSoup(source_boston.content, 'html.parser')
    locate_weather = soup.find('div', class_='wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque')
    locate_weather1 = soup.find('span', class_='wr-value--temperature--c')

    weather = locate_weather.text
    temp = locate_weather1.text
    print(weather)
    print(temp)

source_boston()