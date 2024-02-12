from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') #testactions2


@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact_page.html")

@app.route('/paris/')
def meteo():
    response = urlopen('https://api.openweathermap.org/data/2.5/forecast/daily?q=Paris,fr&cnt=16&appid=bd5e378503939ddaee76f12ad7a97608')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('temp', {}).get('day') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)


@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

@app.route("/histogramme/")
def mongraphique2():
    return render_template("histo.html")

@app.route('/fulljson/')
def fulljson ():
    response = urlopen('https://api.github.com/repos/AkarenLk/5MCSI_Metriques/commits')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for element in json_content:
        print("debut for")
        datepf = element['commit']['author']['date']
        date_object = datetime.strptime(datepf, '%Y-%m-%dT%H:%M:%SZ')
        minutes = date_object.minute
        heures = date_object.hour
        print("datepf :",datepf,";date_object:",date_object,";heure:",heures,";minute:",minutes)
        results.append({'heure':heures,'minute': minutes})
        print("fin for")
        print(results[:])

    minutes_count = {}
    for item in data["results"]:
      minute = item["minute"]
      if minute in minutes_count:
        minutes_count[minute] += 1
      else:
        minutes_count[minute] = 1
    #Créer un dictionnaire final avec toutes les minutes de 0 à 59
    final_count = {i: minutes_count.get(i, 0) for i in range(60)}
    print(final_count[:])

    return jsonify(final_count)

@app.route("/commits/")
def mongraphique3():
    return render_template("commits.html")
  
if __name__ == "__main__":
  app.run(debug=True)
