from flask import Flask
from flask import request
from flask import render_template
import requests

app = Flask(__name__)
idInstance = ''
apiTokenInstance = ''

@app.route("/", methods=['GET', 'POST'])


def contact():
    if request.method == 'POST':
        dict_temp = request.form.to_dict()
        #print(dict_temp)
        try:
            idInstance = dict_temp['idInstance']
            apiTokenInstance = dict_temp['apiTokenInstance']
            apiUrl = dict_temp['apiUrl']
            if apiUrl[-1] != "/":
                apiUrl += "/"
            chatId1 = dict_temp['chatId1']
            message = dict_temp['message']
            chatId2 = dict_temp['chatId2']
            urlFile = dict_temp['urlFile']

        except KeyError:
            idInstance = ''
            apiTokenInstance = ''
            apiUrl = ''
            chatId1 = ''
            message = ''
            chatId2 = ''
            urlFile = ''
        
        if request.form['submit_button'] == 'getSettings':
            url = apiUrl + 'waInstance' + idInstance + '/getSettings/' + apiTokenInstance
            req = requests.get(url)
            #print(req.text)
            return render_template("index.html", output=req.text)
        
        elif request.form['submit_button'] == 'getStateInstance':
            url = apiUrl + 'waInstance' + idInstance + '/getStateInstance/' + apiTokenInstance
            req = requests.get(url)
            #print(req.text)
            return render_template("index.html", output=req.text) 

        elif request.form['submit_button'] == 'SendMessage':
            url = apiUrl + 'waInstance' + idInstance + '/sendMessage/' + apiTokenInstance
            payload = {"chatId": chatId1, "message": message}
            req = requests.post(url, json=payload)
            #print(req.text)
            return render_template("index.html", output=req.text) 

        elif request.form['submit_button'] == 'SendFileByUrl':
            url = apiUrl + 'waInstance' + idInstance + '/sendFileByUrl/' + apiTokenInstance
            payload = {"chatId": chatId2, "urlFile": urlFile, "fileName": urlFile.split("/")[-1], "caption": "N/A"}
            req = requests.post(url, json=payload)
            #print(req.text)
            return render_template("index.html", output=req.text) 

    elif request.method == 'GET':
        return render_template("index.html", output='Select request')
