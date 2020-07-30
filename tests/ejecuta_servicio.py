import json
import string
import random
import requests
from datetime import datetime

def main():
    for i in range(100):
        body = armar_json()
        consumir_mutant(body)
        consumir_stats()

def consumir_stats():
    r = requests.get("https://warm-river-14812.herokuapp.com/stats")
    escribir_respuesta(r.url, r.json)
    

def consumir_mutant(body_json):
    r = requests.post("https://warm-river-14812.herokuapp.com/mutant/", body=body_json)
    escribir_respuesta(r.url, r.status_code)

def escribir_respuesta(servicio, estado):
    archivo = open("prueba.txt", "w")
    archivo.writelines(datetime.now() + ' - Servicio: ' + servicio + ' - Estado: ' + estado)

def armar_json():
    dna1 = ''
    dna2 = ''
    dna3 = ''
    dna4 = ''
    dna5 = ''
    dna6 = ''
    for i in range(6):
        dna1 += random.choice("ACGT")
        dna2 += random.choice("ACGT")
        dna3 += random.choice("ACGT")
        dna4 += random.choice("ACGT")
        dna5 += random.choice("ACGT")
        dna6 += random.choice("ACGT")

    data = {
        "dna":[dna1,dna2,dna3,dna4,dna5,dna6]
    }
    return data