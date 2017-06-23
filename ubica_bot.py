# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 00:19:04 2017

@author: Ignasi Dev
"""

import json
import requests
import time
import urllib
import csv

from dbhelper import DBHelper

db = DBHelper()

TOKEN = "insertTokenHere"
# connect with the telegram api
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates(offset = None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

# analyze the input data and determine what to say based in the folowing conditions
def handle_updates(updates):
    startmode = True
    for update in updates["result"]:
        text = update["message"]["text"] # text sent by the user
        chat = update["message"]["chat"]["id"]
        items = db.get_items(chat)
        if text == "/historial":
            keyboard = build_keyboard(items)
            send_message("Historial: (para seguir buscando información, dime más localidades colombianas)", chat, keyboard)
        elif text == "/start":
            send_message("Hola! Soy UbicaBot, un chatbot diseñado por Ignasi Oliver para Hack4Good. Te daré información de toda Colombia y la guardaré en una lista personal. Para verla, dime /historial.\nDónde te gustaría ir (Colombia)?", chat)
            db.add_item(text, chat)
        elif startmode == True and check_departamento(text) == True:
            send_message('Ok, en qué municipio?', chat)
        elif startmode == True and check_municipio(text) == False:
            send_message("Por favor, vuelve a introducir el municipio", chat)
        elif startmode == True and check_municipio(text) == True:
            startmode = False
            id_municipio = get_id_municipio(text)
            send_message("De acuerdo", chat)
            # in that case let's save it
            db.add_item(text, chat)
            # people NOW
            gente = get_people_by_municipio(id_municipio)
            mensaje_gente = "En " + text + " se encuentran " + str(gente) + " personas"
            send_message(mensaje_gente, chat)
            # average people in the area
            gente_average = get_all_people_by_municipio(id_municipio)
            if gente > gente_average:
              mensaje_all_gente = "Hay más gente de lo habitual. De media, en los últimos 2 meses, cada día había " + str(gente_average) + " personas"
            else:
              mensaje_all_gente = "Es un momento para ir tranquilo. Hay menos gente de lo habitual. En los últimos 2 meses de media había " + str(gente_average) + " personas cada día"
            send_message(mensaje_all_gente, chat)
            # start recommendations here
            """ Doesn't work
            id_departamento = get_id_departamento_by_municipio(id_municipio)
            id_municipio_gente_recomendada = get_id_gente_recomendada(id_departamento, id_municipio, gente)
            nombre_municipio_recomendado = get_name_by_id_municipio(id_municipio_gente_recomendada)
            gente_recomendada = get_people_by_municipio(id_municipio_gente_recomendada)
            print("ID")
            print(id_departamento)
            print("ID MUNICIPIO")
            print(id_municipio_gente_recomendada)
            print("ID NOMBRE")
            print(nombre_municipio_recomendado)
            print("I GENTE")
            print(gente_recomendada)
            if gente_recomendada <= gente:
              mensaje_recomendacion = "Te recomiendo que visites " + nombre_municipio_recomendado + ", donde ahora hay " + str(gente_recomendada) + " personas, y está en el mismo departamento"
              send_message(mensaje_recomendacion, chat)
            """
        # recopilaion of data ended
            send_message("Dónde más quieres ir?", chat)
        elif text.startswith("/"):
            continue
        elif text in items:
            db.delete_item(text, chat)
            items = db.get_items(chat)
            keyboard = build_keyboard(items)
            send_message("Muestra el teclado", chat, keyboard)
        else:
            db.add_item(text, chat)
            items = db.get_items(chat)
            message = "\n".join(items)
            send_message(message, chat)

def check_departamento(nombre):
    nombre = nombre.upper()
    id_departamento = ''
    with open('CO_ids_nombres.csv', 'r') as f:
      reader = csv.reader(f, delimiter=';')
      for row in reader:
        if row[3] == nombre:
          id_departamento = row[2]
          print(id_departamento)
          print(nombre)
          return(True)
    return False

def check_municipio(nombre):
    nombre = nombre.upper()
    id_municipio = ''
    with open('CO_ids_nombres.csv', 'r') as f:
      reader = csv.reader(f, delimiter=';')
      for row in reader:
        if row[1] == nombre:
          id_municipio = row[0]
          print(id_municipio)
          print(nombre)
          return(True)
    return False

def get_id_municipio(nombre):
    nombre = nombre.upper()
    id_municipio = 0
    with open('CO_ids_nombres.csv', 'r') as f:
      reader = csv.reader(f, delimiter=';')
      for row in reader:
        if row[1] == nombre:
          id_municipio = row[0]
    return(id_municipio)

def get_people_by_municipio(municipio):
    # municipio = id_municipio
    people = 0
    with open('hack4good_dwells.csv', 'r') as f:
      reader = csv.reader(f, delimiter=',')
      for row in reader:
        if row[2] == municipio:
          people = int(row[4])
          return(people)
    return(people)

def get_all_people_by_municipio(municipio):
    # municipio = id_municipio
    people = 0
    contador = 1
    with open('hack4good_dwells.csv', 'r') as f:
      reader = csv.reader(f, delimiter=',')
      for row in reader:
        if row[3] == municipio:
          contador = contador + 1
          people = int(people) + int(row[4])
    # average people
    people = int(people/contador)
    return(people)

def get_id_departamento_by_municipio(id_municipio):
    id_departamento = 0
    with open('CO_ids_nombres.csv', 'r') as f:
      reader = csv.reader(f, delimiter=';')
      for row in reader:
        if row[0] == id_municipio:
          id_departamento = int(row[2])
          return(id_departamento)
    return(id_departamento)

def get_id_gente_recomendada(id_departamento, id_municipio, gente):
    municipio_gente_recomendada = gente
    with open('hack4good_dwells.csv', 'r') as f:
      reader = csv.reader(f, delimiter=',')
      for row in reader:
        if row[1] == id_departamento:
          if row[2] != id_municipio:
            if row[4] < gente:
              municipio_gente_recomendada = int(row[2])
              return(municipio_gente_recomendada)
    return(municipio_gente_recomendada)

def get_name_by_id_municipio(municipio):
    # municipio = id_municipio
    name = ""
    with open('CO_ids_nombres.csv', 'r') as f:
      reader = csv.reader(f, delimiter=';')
      for row in reader:
        if row[0] == municipio:
          return(row[1])
    return(name)


def get_last_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    # chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    print(text)
    return (text)

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def build_keyboard(items):
    keyboard = [[item] for item in items]
    reply_markup = {"keyboard":keyboard, "one_time_keyboard": True}
    return json.dumps(reply_markup)

# initial fixed keyboard: the three possible options NOT APPLIED
def initial_fixed_keyboard():
    keyboard = [['1'], ['2'], ['3']]
    reply_markup = {"keyboard":keyboard, "hide_keyboard" : True}
    return json.dumps(reply_markup)

def send_message(text, chat_id, reply_markup=None):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    get_url(url)

def main():
    db.setup()
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.5)

if __name__ == '__main__':
  main()
