from tkinter import messagebox
import json
import pymysql
import xml.etree.ElementTree as ET
import os

def extraerdatosdelxml():
    string = ""
    userandmeasInfoId = []
    measObjLdn = []
    measResults = []

    base_path = os.path.dirname(os.path.realpath(__file__))
    file_xml = os.path.join(base_path,"XML.xml")
    tree = ET.parse(file_xml)
    root = tree.getroot()

    for child in root:
        for secondchild in child:
            userandmeasInfoId.append(secondchild.attrib)

    for child in root:
        for secondchild in child:
            for threechild in secondchild:
                measObjLdn.append(threechild.attrib)

    for child in root:
        for secondchild in child:
            for threechild in secondchild:
                for fourchild in threechild:
                    measResults.append(fourchild.text)


    string = ET.tostring(root).decode(encoding='UTF-8',errors='strict')
    datos = userandmeasInfoId, measObjLdn, measResults, string
    return datos

#generando las tuplas
def generandotuplas(datostupla1, datostupla2, datostupla3, tabla, tupladatos):
    tupla1 = [tupladatos[0][0].get("userLabel"),
    tupladatos[1][1].get("measObjLdn"),datostupla1]
    tabla.append(tupla1)
    tupla2 = [tupladatos[0][0].get("userLabel"),
    tupladatos[1][2].get("measObjLdn"),datostupla2]
    tabla.append(tupla2)
    tupla3 = [tupladatos[0][0].get("userLabel"),
    tupladatos[1][3].get("measObjLdn"),datostupla3]
    tabla.append(tupla3)

        
def creandotablas():
    tupladatos = extraerdatosdelxml()
    print(tupladatos[3])
    TABLA12345 = []
    TABLA45687 = []
#cabecera de la tabla. Es copiada del ejercicio. 
    TABLA12345.append(('RNC', 'CELL','C67194793', 'C67194794', 'C67194795', 'C67194796'))

#extrayendo datos numericos. 
    datostupla1 = [int(numero) for numero in tupladatos[2][0].split(" ",3)]
    datostupla2 = [int(numero) for numero in tupladatos[2][1].split(" ",3)]
    datostupla3 = [int(numero) for numero in tupladatos[2][2].split(" ",3)]
    generandotuplas(datostupla1,datostupla2,datostupla3,TABLA12345, tupladatos)

    TABLA45687.append(('RNC', 'CELL','C125458785', 'C125458786', 'C125458787'))
    datostupla1 = [int(numero) for numero in tupladatos[2][3].split(" ",2)]
    datostupla2 = [int(numero) for numero in tupladatos[2][4].split(" ",2)]
    datostupla3 = [int(numero) for numero in tupladatos[2][5].split(" ",2)]
    generandotuplas(datostupla1,datostupla2,datostupla3,TABLA45687, tupladatos)
    return TABLA12345, TABLA45687

def insertardatos(tabla12345, tabla45687):
    
    db = pymysql.connect(host="localhost",   
                     user="root",        
                     passwd="", 
                     db="wdna_test") 

    cursor = db.cursor()

    c = 1
    while c<len(tabla12345):
        datos = tabla12345[c][0],tabla12345[c][1],tabla12345[c][2][0],tabla12345[c][2][1],tabla12345[c][2][2],tabla12345[c][2][3]
        cursor.execute("INSERT INTO T12345 VALUES(%s, %s, %s, %s, %s,%s)",(datos))
        db.commit()

        datos = tabla45687[c][0],tabla45687[c][1],tabla45687[c][2][0],tabla45687[c][2][1],tabla45687[c][2][2]
        cursor.execute("INSERT INTO T45687 VALUES(%s, %s, %s, %s, %s)",(datos))
        db.commit()
        c += 1

    db.close()

def creandoJson():
    tabla1, tabla2 = creandotablas()
    datos = {
                               'data': [list(tabla1[1]), list(tabla1[2]),list(tabla1[3])],
                               'family': 'T12345',
                               'header': list(tabla1[0])
                }, {
                               'data': [list(tabla2[1]), list(tabla2[2]),list(tabla2[3])],
                               'family': 'T45687',
                               'header': list(tabla2[0])
            }
    formatojson = json.dumps(datos)
    print('Datos en formato JSON:', formatojson)
    with open('xml.json', 'w') as file:
        json.dump(datos, file)

    messagebox.showinfo("Fin del Programa", "Hemos parseado el archivo XML.xml. Hemos "+
        "insertado los datos en la BBDD, y finalmente hemos creado un archivo.json, "+
        "visible en la carpeta y tambien imprimida en consola. "+ "Esperamos que todo "+
        "Haya sido de su agrado. "+ " Atentamente, Fernando Lopez.")


TABLA12345, tabla45687 = creandotablas()
insertardatos(TABLA12345, tabla45687)
creandoJson()

