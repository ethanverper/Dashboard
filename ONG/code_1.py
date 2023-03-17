import sqlite3
import pandas as pd

def create_database():
    conn = sqlite3.connect('dbs.db') 
    c = conn.cursor()

    return conn, c

def create_tables(conn, c):
    
    c.execute('''
              CREATE TABLE IF NOT EXISTS Clases
              (id INTEGER PRIMARY KEY, 
               departamento TEXT, 
               nombre TEXT,
               fecha_inicio DATE, 
               fecha_fin DATE, 
               tema TEXT);
              ''')

    c.execute('''
              CREATE TABLE IF NOT EXISTS Alumnos
              (
               id INTEGER PRIMARY KEY, 
               nombre TEXT,
               apellido_paterno TEXT, 
               apellido_materno TEXT, 
               genero TEXT,
               grupo TEXT,
               clases_id integer,
               tasa_asistencia FLOAT,
               foreign key (clases_id) REFERENCES Clases (id));
              ''')

    c.execute('''

              CREATE TABLE IF NOT EXISTS Familia
              (id INTEGER PRIMARY KEY, 
               apellido TEXT,
               nivel TEXT, 
               tasa_asistencia FLOAT,
               alumno_id integer,
               clases_id integer,
               foreign key (alumno_id) REFERENCES Alumnos (id),
               foreign key (clases_id) REFERENCES Clases (id));

              ''')

    c.execute('''

              CREATE TABLE IF NOT EXISTS Profesor
              (
               id INTEGER PRIMARY KEY, 
               nombre TEXT,
               apellido TEXT,
               clases_id integer,
               foreign key (clases_id) REFERENCES Clases (id));

              ''')

    conn.commit()

def insert_data(conn, c):
    print('Inserting data')
    Alumnos = pd.read_csv('Base de Datos Dummie - Alumnos (1).csv')
    Clases = pd.read_csv('Base de Datos Dummie - Clases.csv')
    Familia = pd.read_csv('Base de Datos Dummie - Familia.csv')
    Profesor = pd.read_csv('Base de Datos Dummie - Profesores.csv')

    lista_tablas = [Clases, Alumnos, Familia, Profesor]

    for tabla in range(len(lista_tablas)):
        inserts = [tuple(x) for x in lista_tablas[tabla].values]
        for i in range(len(inserts)):
            if tabla == 0:
                insert_query = """INSERT OR REPLACE INTO Clases(id, nombre, departamento, fecha_inicio, fecha_fin, tema) VALUES(?,?,?,?,?,?)""" 
                c.execute(insert_query, inserts[i])
                conn.commit()
            elif tabla == 1:
                insert_query = """INSERT OR REPLACE INTO Alumnos(id, nombre, apellido_paterno, apellido_materno, genero, grupo, clases_id, tasa_asistencia) VALUES(?,?,?,?,?,?,?,?)""" 
                c.execute(insert_query, inserts[i])
                conn.commit()
            elif tabla == 2:
                insert_query = """INSERT OR REPLACE INTO Familia(id, apellido, nivel, tasa_asistencia, alumno_id, clases_id) VALUES(?,?,?,?,?,?)""" 
                c.execute(insert_query, inserts[i])
                conn.commit()
            elif tabla == 3:
                insert_query = """INSERT OR REPLACE INTO Profesor(id, clases_id, nombre, apellido) VALUES(?,?,?,?)""" 
                c.execute(insert_query, inserts[i])
                conn.commit()

if __name__ == '__main__':
    conn, c = create_database()
    create_tables(conn, c)
    insert_data(conn, c)
    

