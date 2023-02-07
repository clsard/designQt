import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect (
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.db_cursor = self.connection.cursor()
        
    def add_record(self, table, fecha_bd, hora_bd, prompt_es, prompt_en, cantidad, size_solicitado, imagen_name ,carpeta_xml):
        query = f"INSERT INTO {table} (fecha, hora, prompt_es, prompt_en, cantidad, size, archivo, carpeta)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (fecha_bd, hora_bd, prompt_es, prompt_en, cantidad, size_solicitado, imagen_name, carpeta_xml)
        try:
            self.db_cursor.execute(query, valores)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            print("Error al agregar registro:", e)
        
    def close(self):
        self.db_cursor.close()
        self.connection.close()