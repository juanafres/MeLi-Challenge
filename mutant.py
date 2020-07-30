import json
import re
from pymongo import MongoClient

clientdb = MongoClient('mongodb+srv://user_app_mongo:xxxxxxxxxxxxx@cluster0.22ato.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority')
mydb = clientdb["MutantAPI"] 


COMPA = 'AAAA'
COMPT = 'TTTT'
COMPC = 'CCCC'
COMPG = 'GGGG'
REGEX_VAL = "[^¨\\'\[\],CATG ]"

class Mutant: 
    def __init__(self):
        self.data = []
       
    
    def is_mutant(self, dna):
        
        for documentos in mydb.humansRepository.find({"dna":dna},{"mutante":1}):
            return documentos["mutante"]

        if es_horizontal(dna) or es_oblicuo(dna) or es_vertical(dna):
            database_entry = {}
            database_entry['dna'] = dna
            database_entry['mutante'] = 'true'
            mydb.humansRepository.insert(database_entry)
            return True
        else: 
            database_entry = {}
            database_entry['dna'] = dna
            database_entry['mutante'] = 'false'
            mydb.humansRepository.insert(database_entry)
            return False

    def validate_dna(self, dna):
        data_error = re.findall(REGEX_VAL, str(dna))
        if data_error:
            return True
        else: 
            return False

class Stats:
    def __init__(self):
        self.data = []
       
    
    def get_stats_dna(self):
        
        result_mutants = mydb.humansRepository.find({"mutante":"true"})
        count_mutant_dna = result_mutants.count()
        result_humans = mydb.humansRepository.find({})
        count_human_dna = result_humans.count()
        ratio = count_mutant_dna / count_human_dna
        data = {
            "count_mutant_dna":count_mutant_dna,
            "count_human_dna":count_human_dna,
            "ratio":ratio
        }
        return data



def es_horizontal(dna):
    for row in dna:
        if row.find(COMPA) != -1 or row.find(COMPT) != -1 or row.find(COMPC) != -1 or row.find(COMPG) != -1:
            return True
    return False


def es_vertical(dna):
    row = ''
    for j in range(len(dna)):
        for x in range(len(dna)):
            row += dna[x][j]
        if row.find(COMPA) != -1 or row.find(COMPT) != -1 or row.find(COMPC) != -1 or row.find(COMPG) != -1:
            return True
        row = ''

    return False

def es_oblicuo(dna):
    oblicua = ''
    oblicua_reverse = ''
    for index in range(len(dna)):
        oblicua += dna[index][index]   
        oblicua_reverse += dna[index][len(dna)-1-index]
    
    if oblicua.find(COMPA) != -1 or oblicua.find(COMPT) != -1 or oblicua.find(COMPC) != -1 or oblicua.find(COMPG) != -1:
        return True
    if oblicua_reverse.find(COMPA) != -1 or oblicua_reverse.find(COMPT) != -1 or oblicua_reverse.find(COMPC) != -1 or oblicua_reverse.find(COMPG) != -1:
        return True


    if right_diagonal(dna) or left_diagonal(dna):
        return True

    return False 

def right_diagonal(dna):
    row = ''
    row_botton = ''
    indej = 0
    for j in range(len(dna)-4): 
        for x in range(j+1,len(dna)):
            row += dna[x-1-indej][x]
            if row.find(COMPA) != -1 or row.find(COMPT) != -1 or row.find(COMPC) != -1 or row.find(COMPG) != -1:
                return True
            row_botton += dna[x][x-1-indej]  
            if row_botton.find(COMPA) != -1 or row_botton.find(COMPT) != -1 or row_botton.find(COMPC) != -1 or row_botton.find(COMPG) != -1:
                return True

        indej += 1
        row = ''
        row_botton = ''

    return False

def left_diagonal(dna):
    column = ''
    column_botton = ''
    indej = 0
    for j in range(len(dna)-4): 
        for x in range(j+1,len(dna)):
            column += dna[x-1-indej][len(dna)-x-1]
            if column.find(COMPA) != -1 or column.find(COMPT) != -1 or column.find(COMPC) != -1 or column.find(COMPG) != -1:
                return True
            
            column_botton += dna[x][len(dna)-x+indej] 
            if column_botton.find(COMPA) != -1 or column_botton.find(COMPT) != -1 or column_botton.find(COMPC) != -1 or column_botton.find(COMPG) != -1:
                return True
        indej += 1
        column = ''
        column_botton = ''

    return False

