# Este programa solicita por consola un prompt, cantidad y tamaño para solicitar a `Dall-E` imágenes
# programado por C. L. Sard - ene 2023
import os
import openai
import base64
import time
import argparse
from dotenv import load_dotenv
load_dotenv()

# Initiate the parser
# parser = argparse.ArgumentParser()
# parser.add_argument("-p", "--prompt", help="Text to image prompt:", default='score surrounded by musical notes in soft tones and flat colors in the Kandinsky style, abstract painting, oil painting, high definition')
# parser.add_argument("-n", "--number", help="Number of images generated", default=2)
# parser.add_argument("-s", "--size", help="Image size: 256, 512 or 1024", default=1024)

# Read arguments from the command line
# args = parser.parse_args()
#print("Prompt: ", end="")
prompt=input("prompt: ")
porDefecto = 1
miSize = 512
cantidad = int(input(f"cantidad: (por defecto {porDefecto})") or porDefecto)
miSize = int(input(f"Tamaño: (por defecto {miSize})") or miSize)
if miSize != 512 and miSize != 1024 and miSize != 256:
  print(f"El tamaño debe de ser: 256, 512 ó 1024 usted introdujo {miSize}")
  raise SystemExit
  
if cantidad < 1 or cantidad > 2:
  print(f"la cantidad tiene que ser 1 ó 2 usted introdujo {cantidad} ")
  raise SystemExit
else:   
  print(f"Prompt: {prompt}")
print(f"Cantidad: {cantidad}")
print(f"Tamaño: {miSize}")

user_input = input('¿Estas seguro con estos datos? (si/no): ')

if user_input.lower() == 'si':
    print('Has dicho si. Procesando petición...')
elif user_input.lower() == 'no':
    print('Has dicho no')
    raise SystemExit
else:
    print('Escriba si o no')
#raise SystemExit


openai.api_key = os.getenv("OPENAI_API_KEY")
#openai.api_key = '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'

# res = openai.Image.create(
#   prompt=args.prompt,
#   n=int(args.number),
#   size=f'{args.size}x{args.size}',  
#   response_format="b64_json"
# )
res = openai.Image.create(
  prompt=prompt,
  n=int(cantidad),
  size=f'{miSize}x{miSize}',  
  response_format="b64_json"
)

#900333555 opcion 3 baja inmediata
for i in range(0, len(res['data'])):
    b64 = res['data'][i]['b64_json']
    filename =  f'image_{int(time.time())}_{i}.png'
    filename = 'imagenes\\' + filename
    print('Saving file ' + filename)
    with open(filename, 'wb') as f:
        f.write(base64.urlsafe_b64decode(b64))