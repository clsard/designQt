# Este programa solicita por consola un prompt, cantidad y tamaño para solicitar a `Dall-E` imágenes
# programado por C. L. Sard - ene 2023
import os
import openai
import base64
import time
import argparse
#cargamos libreria del GUI Tkinter
#import tkinter
# from tkinter import *
# from tkinter import messagebox
from dotenv import load_dotenv
from easygoogletranslate import EasyGoogleTranslate
translator= EasyGoogleTranslate(
  source_language = 'es',
  target_language = 'en',
  timeout = 10
)
load_dotenv()
# tkinter._test()
# buble para solicitar prompt en español y traducir a inglés
# y aceptar con input
todoOk = False
while not todoOk:
  os.system('clear')
  hecho = False
  while not hecho:
    promptEs=input("Prompt (español): ")
    translacion = translator.translate(promptEs)
    print(f"Traducción: {translacion}")
    user_input = input('¿Estas satisfecho con esta traducción? (si/no): ')
    if user_input.lower() == 'si':
      hecho = True
      print('Has dicho si. Seguimos...')
    else:
      break
    porDefecto = 1
    miSize = 512
    cantidad = int(input(f"cantidad: (por defecto {porDefecto})") or porDefecto)
    miSize = int(input(f"Tamaño: (por defecto {miSize})") or miSize)
    if miSize != 512 and miSize != 1024 and miSize != 256:
      print(f"El tamaño debe de ser: 256, 512 ó 1024 usted introdujo {miSize}")
      print("Ha solicitado un tamaño erroneo, entiendo que no quiere continuar")
      raise SystemExit
      
    if cantidad < 1 or cantidad > 2:
      print(f"la cantidad tiene que ser 1 ó 2 usted introdujo {cantidad} ")
      print("Entiendo que no quiere continuar")
      raise SystemExit
    os.system('clear')
    print(f"Prompt (Español): {promptEs}")
    print(f"Prompt (Inglés)  : {translacion}")  
    print(f"Cantidad: {cantidad}")
    print(f"Tamaño: {miSize}")
    print()
    user_input = input('¿Estas seguro con estos datos? (si/no): ')
    if user_input.lower() == 'si':
        print('Has dicho si. Procesando petición...')
        todoOk = True
    # No hace falta lo siguiente pero lo dejo
    # para recordar la instrucción "elif" (como ELSE IF)
    # elif user_input.lower() == 'no':
    #     print('Has dicho no')
    #     raise SystemExit
    else:
        print('No se realizará su petición: Cancelado por usuario')
        print('En dos segundos comenzaremos de nuevo')
        time.sleep(3)
        todoOk = False
#os.system('clear')    
openai.api_key = os.getenv("OPENAI_API_KEY")
res = openai.Image.create(
  prompt=translacion,
  n=int(cantidad),
  size=f'{miSize}x{miSize}',  
  response_format="b64_json"
)
for i in range(0, len(res['data'])):
    b64 = res['data'][i]['b64_json']
    imagenName =  f'image_{int(time.time())}_{i}.png'
    filename = 'imagenes\\' + imagenName
    print('Saving file ' + filename)
    with open(filename, 'wb') as f:
        f.write(base64.urlsafe_b64decode(b64))
    filename = 'G:/Mi unidad/Dall-e/' + imagenName
    with open(filename, 'wb') as f:
        f.write(base64.urlsafe_b64decode(b64))    
        