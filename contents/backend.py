
from bs4 import BeautifulSoup
from flask.templating import render_template
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/albany')
@app.route('/')
def source_albany():
        source_weather = requests.get('https://wnyt.com/weather/')
        soup = BeautifulSoup(source_weather.content, 'html.parser')
        title = soup.title.text

        locate_weather = soup.find('div', class_='col-xs-12 col-sm-4 text-center')
        weather_albany = locate_weather.text
        general_info = soup.find('div', class_='col-xs-6 col-sm-4')
        info = general_info.text


        return render_template('index.html', title=title, weather_albany=weather_albany, info=info)

@app.route('/tokyo')
@app.route('/japan')
def source_toyo():
    source_tokyo = requests.get('https://www.yahoo.com/news/weather/japan/tokyo-prefecture/tokyo-1118370/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAMOhGc8KvrFl8yvh3kQcEvuUd7rF7iPiYjK_1N3eE04WkIow5UwWRPwdsoEUthZmK6jzlgKdKkhfVZ8ywrQUHvbromsGoUIUiKLkoXQtxd_VkNyNY9pkKA-oON7yL_18wj93DjEq4RFPZZgrq7FYTceb27nQ1g4oZ8Fx0dhY476c')
    soup = BeautifulSoup(source_tokyo.content, 'html.parser')
    locate_weather = soup.find('span', class_='Va(t)')
    weather =  locate_weather.text



    source_tokyo = requests.get('https://www.qweather.com/en/weather30d/tokyo-65E77.html')
    soup = BeautifulSoup(source_tokyo.content, 'html.parser')
    locate_weather1 = soup.find('p', class_='weather30d-calendar__abstract text-center')
    weather1 =  locate_weather1.text

    return render_template('tokyo.html', weather=weather, weather1=weather1)


@app.route('/wa')
@app.route('/seattle')
def source_seattle():
    source_seattle = requests.get('https://www.bbc.com/weather/5809844')
    soup = BeautifulSoup(source_seattle.content, 'html.parser')
    locate_weather = soup.find('div', class_='wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque')
    locate_weather1 = soup.find('span', class_='wr-value--temperature--c')

    weather = locate_weather.text
    temp = locate_weather1.text

    return render_template('seattle.html', weather=weather, temp=temp)




@app.route('/ca')    
@app.route('/la')
def source_la():
    source_la = requests.get('https://www.bbc.com/weather/5368361')
    soup = BeautifulSoup(source_la.content, 'html.parser')
    locate_weather = soup.find('div', class_='wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque')
    locate_weather1 = soup.find('span', class_='wr-value--temperature--c')

    weather = locate_weather.text
    temp = locate_weather1.text
    return render_template('la.html', weather=weather, temp=temp)



@app.route('/ma')
@app.route('/boston')
def source_boston():
    source_boston = requests.get('https://www.bbc.com/weather/4930956')
    soup = BeautifulSoup(source_boston.content, 'html.parser')
    locate_weather = soup.find('div', class_='wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque')
    locate_weather1 = soup.find('span', class_='wr-value--temperature--c')

    weather = locate_weather.text
    temp = locate_weather1.text
    return render_template('boston.html', weather=weather, temp=temp)

@app.route('/ru')
@app.route('/moscow')


def source_moscow():
    source_moscow = requests.get('https://www.bbc.com/weather/524901')
    soup = BeautifulSoup(source_moscow.content, 'html.parser')
    locate_weather = soup.find('div', class_='wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque')
    locate_weather1 = soup.find('span', class_='wr-value--temperature--c')

    weather = locate_weather.text
    temp = locate_weather1.text
    return render_template('moscow.html', weather=weather, temp=temp)


@app.errorhandler(404)    
def error_page(error):
    return  render_template('error.html'), 404




if __name__ == "__main__":
    app.run(debug=True)

