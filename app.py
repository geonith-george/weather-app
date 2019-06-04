from flask import Flask,jsonify,render_template,request
import requests
import json,time

app = Flask(__name__)
@app.route("/")
def homepage():
    return render_template("main.html")

@app.route("/location", methods=["POST"])
def location():
    name = request.form.get("name")
    if not name:
        return render_template("location.html",name="Enter valid location")
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={name}&appid=001e2945294f12d900be61fdb7f6ff0c')
    name=name.upper()
    temp2=json.loads(r.text)['main']['temp']
    temp2 = temp2 - 273.15
    temp2 = round(temp2,2)
    return render_template("location.html",name=name, lat=json.loads(r.text)['coord']['lat'], lon=json.loads(r.text)['coord']['lon'], temp2=temp2, w2=json.loads(r.text)['main']['humidity'])

@app.route("/location2", methods=["POST"])
def location2():    
    name = request.form.get("name2")
    if not name:
        return render_template("location.html",name="Enter valid location")
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?zip={name}&appid=001e2945294f12d900be61fdb7f6ff0c')
    name=name.upper()
    temp2=json.loads(r.text)['main']['temp']
    temp2 = temp2 - 273.15
    temp2 = round(temp2,2)

    return render_template("location.html",name=name, lat=json.loads(r.text)['coord']['lat'], lon=json.loads(r.text)['coord']['lon'], temp2=temp2, w2=json.loads(r.text)['main']['humidity'])
    
if __name__ == "__main__":
    app.run()

