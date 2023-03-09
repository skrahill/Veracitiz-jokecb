from flask import Flask,render_template,request,jsonify
import pyjokes,python_weather
import asyncio,requests
from bs4 import BeautifulSoup


def get_jok():
    new_joke=pyjokes.get_joke()

    

    return new_joke

def weather(city):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    #print("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()



    return weather+"°C"



app=Flask(__name__)





@app.route("/",methods=['POST','GET'])
def webhook():
    return "Received"

@app.route("/joke",methods=['GET'])
def jokes():

    myjoke=get_jok()
    return jsonify(myjoke)


@app.route('/tempurature',methods=['POST'])
def temp():
    if request.method=='POST':
        # input_json=request.get_json(force=True)
        input_json=request.form
        loc=input_json['location']+' weather'

        teemp=weather(loc)

        res=teemp

        return jsonify(res)



# if __name__ == '__main__':
app.run(debug=True)