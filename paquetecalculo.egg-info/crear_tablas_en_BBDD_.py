import pymysql
import warnings, pymysql
from tkinter import messagebox
import sys
warnings.filterwarnings('error', category=pymysql.Warning)

def creacionBBDD():

    try:
        db = pymysql.connect(host="localhost",   
                     user="root",        
                     passwd="", 
                     db="wdna_test")

        cursor = db.cursor()
    except:
        messagebox.showinfo("Atencion", "Necesito que cree una base de datos con el nombre 'wdana_test. "+
            "Después vuelve a iniciar este programa.")
        sys.exit()

    try:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS T12345 (
            RNC VARCHAR(50) CHARACTER SET latin1 DEFAULT NULL,
            CELL VARCHAR(50) CHARACTER SET latin1 DEFAULT NULL,
            C67194793 INT(11) DEFAULT NULL,
            C67194794 INT(11) DEFAULT NULL,
            C67194795 INT(11) DEFAULT NULL,
            C67194796 INT(11) DEFAULT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8;''')

    except:
        messagebox.showinfo("Atencion", "Tabla T12345 ya esta creada")
    

    

    
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS T45687 (
                RNC VARCHAR(50) CHARACTER SET latin1 DEFAULT NULL,
                CELL VARCHAR(50) CHARACTER SET latin1 DEFAULT NULL,
                C125458785 INT(11) DEFAULT NULL,
                C125458786 INT(11) DEFAULT NULL,
                C125458787 INT(11) DEFAULT NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8''')

    except:
        messagebox.showinfo("Atencion", "Tabla T45687 ya esta creada")
        sys.exit()
    
    messagebox.showinfo("Atencion", "Tablas creadas correctamente, muchas gracias. Ahora puede"+
        " iniciar el Script del ejercicio.")
    db.commit()

    db.close()

creacionBBDD()

