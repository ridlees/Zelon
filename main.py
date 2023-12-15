#!/bin/python3

from flask import Flask, render_template,request, send_from_directory
#pip install asgiref
import asyncio
from scraper import Main as PSPscraper
from sender import send_email
from dotenv import load_dotenv
import os
from os.path import join, dirname
import time

app = Flask(__name__, template_folder='./conf/templates')

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

port = os.environ.get("PORT")
smtp_server = os.environ.get("SMTP_SERVER")
sender_email = os.environ.get("SENDER_EMAIL")
app.config['SECURITY_EMAIL_SENDER'] = os.environ.get("SENDER_EMAIL")
password = os.environ.get("PASSWORD")

#emails = PSPscraper()
#emails = ("martinkodada@icloud.com", "martin.kodada@applifting.cz", "martinkodada@icloud.com", "martin.kodada@applifting.cz")
emails = ['adameci@psp.cz', 'adamkovav@psp.cz', 'babisa@psp.cz', 'babisovaa@psp.cz', 'babkao@psp.cz', 'bacikovaj@psp.cz', 'balasv@psp.cz', 'balastikovam@psp.cz', 'bartosi@psp.cz', 'bartosekj@psp.cz', 'bastaj@psp.cz', 'bauerj@psp.cz', 'baxam@psp.cz', 'beitlp@psp.cz', 'belicaj@psp.cz', 'belobradekp@psp.cz', 'belohlavkovar@psp.cz', 'belorr@psp.cz', 'bendam@psp.cz', 'bendlp@psp.cz', 'benesiko@psp.cz', 'berkij@psp.cz', 'berkovcovaj@psp.cz', 'berkovecs@psp.cz', 'bernardj@psp.cz', 'blahas@psp.cz', 'blazekp@psp.cz', 'brabecr@psp.cz', 'brazdilm@psp.cz', 'brozl@psp.cz', 'buresj@psp.cz', 'bzochj@psp.cz', 'carbolj@psp.cz', 'coganj@psp.cz', 'cernochovaj@psp.cz', 'cernyo@psp.cz', 'decroixe@psp.cz', 'dostalovak@psp.cz', 'draziloval@psp.cz', 'dubskyt@psp.cz', 'dufeka@psp.cz', 'dvorakj@psp.cz', 'exnerm@psp.cz', 'faltynekj@psp.cz', 'farhank@psp.cz', 'feranecm@psp.cz', 'fialap@psp.cz', 'fialar@psp.cz', 'fialovae@psp.cz', 'fifkap@psp.cz', 'fischerovar@psp.cz', 'flekj@psp.cz', 'foldynaj@psp.cz', 'fridrichs@psp.cz', 'gazdikp@psp.cz', 'golasowskap@psp.cz', 'haask@psp.cz', 'hajekji@psp.cz', 'hajekm@psp.cz', 'hanzlikovaj@psp.cz', 'havelm@psp.cz', 'havlicekk@psp.cz', 'havranekj@psp.cz', 'helebrantt@psp.cz', 'hellers@psp.cz', 'hendrychi@psp.cz', 'hofmannj@psp.cz', 'horakj@psp.cz', 'hrncirj@psp.cz', 'jaci@psp.cz', 'jakobj@psp.cz', 'jandaj@psp.cz', 'janulikm@psp.cz', 'jilkovam@psp.cz', 'juchelkaa@psp.cz', 'jureckam@psp.cz', 'kankovskyv@psp.cz', 'kasald@psp.cz', 'kasnikp@psp.cz', 'kettnerz@psp.cz', 'klimap@psp.cz', 'knechtoval@psp.cz', 'kobzaj@psp.cz', 'kocmanovak@psp.cz', 'kohajdam@psp.cz', 'kohoutekt@psp.cz', 'kolaro@psp.cz', 'kolovratnikm@psp.cz', 'kotenr@psp.cz', 'kottj@psp.cz', 'kovarovav@psp.cz', 'kralv@psp.cz', 'kralicekr@psp.cz', 'krejzak@psp.cz', 'krutakovaj@psp.cz', 'kubicekr@psp.cz', 'kubikj@psp.cz', 'kuceram@psp.cz', 'kucharj@psp.cz', 'kuklam@psp.cz', 'kupkam@psp.cz', 'lacinaj@psp.cz', 'langh@psp.cz', 'langsadlovah@psp.cz', 'lesenskav@psp.cz', 'letochap@psp.cz', 'levkoj@psp.cz', 'liskap@psp.cz', 'lochmano@psp.cz', 'madlovai@psp.cz', 'majorm@psp.cz', 'malat@psp.cz', 'marikovak@psp.cz', 'masekj@psp.cz', 'metnarl@psp.cz', 'michalekj@psp.cz', 'vildumetzovaj@psp.cz', 'mullert@psp.cz', 'munzarv@psp.cz', 'nacherp@psp.cz', 'naiclerovah@psp.cz', 'navratilj@psp.cz', 'crkvenjasz@psp.cz', 'novakm@psp.cz', 'novakovan@psp.cz', 'novym@psp.cz', 'obornam@psp.cz', 'ochodnickam@psp.cz', 'okamurah@psp.cz', 'okamurat@psp.cz', 'oklestekl@psp.cz', 'olsakovae@psp.cz', 'opltovam@psp.cz', 'oulehlovar@psp.cz', 'ozanovaz@psp.cz', 'pastuchovaj@psp.cz', 'adamovam@psp.cz', 'pestovab@psp.cz', 'petrtylf@psp.cz', 'philippt@psp.cz', 'pivonkap@psp.cz', 'pokornajer@psp.cz', 'posarovam@psp.cz', 'potuckoval@psp.cz', 'prazakd@psp.cz', 'quittovap@psp.cz', 'raisk@psp.cz', 'rakusanv@psp.cz', 'ratajm@psp.cz', 'ratiborskym@psp.cz', 'richterj@psp.cz', 'richterovao@psp.cz', 'rozvoralr@psp.cz', 'ruzickap@psp.cz', 'rybad@psp.cz', 'sadovskyp@psp.cz', 'salvetrr@psp.cz', 'schillerovaa@psp.cz', 'silaj@psp.cz', 'skopecekj@psp.cz', 'sladecekk@psp.cz', 'slavikj@psp.cz', 'smetanak@psp.cz', 'stanekpa@psp.cz', 'stanjuraz@psp.cz', 'strycekj@psp.cz', 'strzinekr@psp.cz', 'svobodab@psp.cz', 'svobodap@psp.cz', 'safrankoval@psp.cz', 'sebelovam@psp.cz', 'simekd@psp.cz', 'spicakj@psp.cz', 'stefanovai@psp.cz', 'stolpad@psp.cz', 'telekyr@psp.cz', 'tesarika@psp.cz', 'turecekk@psp.cz', 'turekl@psp.cz', 'urbanovab@psp.cz', 'valekv@psp.cz', 'valkovah@psp.cz', 'vichr@psp.cz', 'vlcekl@psp.cz', 'voborskam@psp.cz', 'vojtkov@psp.cz', 'volnyj@psp.cz', 'vomackav@psp.cz', 'vondracekr@psp.cz', 'vondraki@psp.cz', 'vranap@psp.cz', 'vybornym@psp.cz', 'wenzll@psp.cz', 'wenzlm@psp.cz', 'zajickovar@psp.cz', 'zborovskym@psp.cz', 'zlinskyv@psp.cz', 'zunam@psp.cz', 'zacekp@psp.cz', 'zenisekm@psp.cz']
emails.reverse()
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sender", methods=['POST', "GET"])
def send():

    if request.method == "GET":
        return "USE POST", 403

    if request.method == 'POST':
        subject = request.form.get("subject")
        text = request.form.get("message")
        for email in emails:
            message = f"From: {sender_email}\r\nTo: {email}\r\nSubject:{subject}\r\n{text}"
            send_email(port, smtp_server, sender_email, password, email, message)
            time.sleep(1.5)
        return render_template("index.html", text="Odesláno!"), 201

app.run(host="0.0.0.0",port=80)
