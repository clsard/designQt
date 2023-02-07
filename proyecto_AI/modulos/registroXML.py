import xml.etree.ElementTree as ET
from xml.dom import minidom
import sys
import os
import mysql.connector

print ("todo bien")
mydb = mysql.connector.connect (
    host = "localhost",
    user = "clsard",
    password = "*2013Cct&Clsm1205#"
)
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
sys.exit()


# def prettify(elem):
#     """Return a pretty-printed XML string for the Element.
#     """
#     rough_string = ET.tostring(elem, 'utf-8')
#     reparsed = minidom.parseString(rough_string)
#     return reparsed.toprettyxml(indent="    ")
class Registro:
    def __init__(self, fecha_hora, prompt_es, prompt_en, cantidad, size, carpeta, archivo):
        self.fecha_hora = fecha_hora
        self.prompt_es = prompt_es
        self.prompt_en = prompt_en
        self.cantidad = cantidad
        self.size = size
        self.carpeta = carpeta
        self.archivo = archivo

class GuardarXML:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.registros = []
        # Verificar si el archivo XML existe
        try:
            tree = ET.parse(self.nombre_archivo)
            root = tree.getroot()

            # Leer los registros existentes en el archivo XML
            for reg in root.findall("registro"):
                fecha_hora = reg.find("fecha").text
                prompt_es = reg.find("prompt_es").text
                prompt_en = reg.find("prompt_en").text
                cantidad = int(reg.find("cantidad").text)
                size = int(reg.find("size").text)
                carpeta = reg.find("carpeta").text
                archivo = reg.find("archivo").text

                registro = Registro(fecha_hora, prompt_es, prompt_en, cantidad, size, carpeta, archivo)
                self.registros.append(registro)
        except FileNotFoundError:
            # Si el archivo XML no existe, crear una estructura de datos vacía
            root = ET.Element("registros")
    def agregar_registro(self, registro):
        self.registros.append(registro)

    def guardar(self):
        #root = ET.Element("registros")
        if not os.path.exists(self.nombre_archivo):
            root = ET.Element("registros")
            tree = ET.ElementTree(root)
            tree.write(self.nombre_archivo, encoding='unicode', xml_declaration=True)
        tree = ET.parse(self.nombre_archivo)
        root = tree.getroot()

        for registro in self.registros:
            reg = ET.SubElement(root, "registro")
            ET.SubElement(reg, "fecha").text = registro.fecha_hora
            ET.SubElement(reg, "prompt_es").text = registro.prompt_es
            ET.SubElement(reg, "prompt_en").text = registro.prompt_en
            ET.SubElement(reg, "cantidad").text = str(registro.cantidad)
            ET.SubElement(reg, "size").text = str(registro.size)
            ET.SubElement(reg, "carpeta").text = registro.carpeta
            ET.SubElement(reg, "archivo").text = registro.archivo
        tree.write(self.nombre_archivo, encoding='unicode', xml_declaration=True)
        # rough_string = ET.tostring(root, 'utf-8')
        # reparsed = minidom.parseString(rough_string)
        # with open(self.nombre_archivo, "w") as f:
        #     f.write(reparsed.toprettyxml(indent="    "))


        # for registro in self.registros:
        #     reg = ET.SubElement(root, "registro")
        #     ET.SubElement(reg, "fecha").text = registro.fecha_hora
        #     ET.SubElement(reg, "prompt_es").text = registro.prompt_es
        #     ET.SubElement(reg, "prompt_en").text = registro.prompt_en
        #     ET.SubElement(reg, "cantidad").text = str(registro.cantidad)
        #     ET.SubElement(reg, "size").text = str(registro.size)
        #     ET.SubElement(reg, "carpeta").text = registro.carpeta

        # xml_str = prettify(root)
        # tree = ET.ElementTree(root)
        # tree.write(self.nombre_archivo, encoding='unicode', xml_declaration=True)
        # # with open(self.nombre_archivo, "wb") as f:
        # #     f.write(xml_str.encode('utf-8'))


