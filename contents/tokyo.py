from bs4 import BeautifulSoup
from flask.templating import render_template
import requests
from flask import Flask


def source_toyo():
    source_tokyo = requests.get('https://www.yahoo.com/news/weather/japan/tokyo-prefecture/tokyo-1118370/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAMOhGc8KvrFl8yvh3kQcEvuUd7rF7iPiYjK_1N3eE04WkIow5UwWRPwdsoEUthZmK6jzlgKdKkhfVZ8ywrQUHvbromsGoUIUiKLkoXQtxd_VkNyNY9pkKA-oON7yL_18wj93DjEq4RFPZZgrq7FYTceb27nQ1g4oZ8Fx0dhY476c')
    soup = BeautifulSoup(source_tokyo.content, 'html.parser')
    locate_weather = soup.find('span', class_='Va(t)')
    weather =  locate_weather.text
    print(weather)


source_toyo()


