from io import BytesIO
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import pyperclip
import os
import openai
import base64
import time
from PIL import Image, ImageTk
#import googletrans
from dotenv import load_dotenv
from easygoogletranslate import EasyGoogleTranslate

class App:
    def __init__(self, master):
        self.master = master
        self.seleccion = tk.StringVar()
        master.title("Dall-E Image Generator")

        self.option1 = tk.Radiobutton(master, text="Opción 1", variable=self.seleccion, value="1")
        self.option1.grid(row=10, column=0, sticky="s", rowspan=2)
        self.option2 = tk.Radiobutton(master, text="Opción 2", variable=self.seleccion, value="2")
        self.option1.grid(row=11, column=0, sticky="s", rowspan=2)

        self.label = tk.Label(master, text="Prompt (Español):", anchor="w")
        self.label.grid(row=1, column=0, sticky="w", rowspan=2)
        
        self.prompt_es = tk.Text(master, height=3, width=40)
        self.prompt_es.grid(row=1, column=1, rowspan=2)
        self.prompt_es.bind("<KeyRelease>", self.translate_on_the_fly)

        self.label_en = tk.Label(master, text="Prompt (Inglés):", anchor="w")
        self.label_en.grid(row=4, column=0, sticky="w", rowspan=2)

        self.prompt_en = tk.Text(master, height=3, width=40)
        self.prompt_en.grid(row=4, column=1, rowspan=2)

        self.label_cant = tk.Label(master, text="Cantidad (1-2):", anchor="w")
        self.label_cant.grid(row=7, column=0, sticky="w", rowspan=3)

        self.cantidad = tk.Entry(master)
        self.cantidad.insert(0,"1")
        self.cantidad.grid(row=7, column=1, rowspan=2)

        self.label_size = tk.Label(master, text="Tamaño (256, 512, 1024):", anchor="w")
        self.label_size.grid(row=9, column=0, sticky="w", rowspan=2)

        self.create_button = tk.Button(master, text="  Crear  ", command=self.create)
        self.create_button.grid(row=11, column=2, pady=10, padx=10, sticky="e")

        self.clear_button = tk.Button(master, text="Limpiar", command=self.clear)
        self.clear_button.grid(row=11, column=0, pady=10, padx=10, sticky="w")

        self.copiar_button = tk.Button(master, text="Copiar", command=self.copiar)
        self.copiar_button.grid(row=11, column=1, pady=10, padx=10, sticky="s")

        self.size = tk.Entry(master)
        self.size.insert(0,"256")
        self.size.grid(row=9, column=1, rowspan=2)
        

    def translate_on_the_fly(self, event):

        text_to_translate = event.widget.get("1.0", "end")
        translator = EasyGoogleTranslate()
        translation = translator.translate(text_to_translate, "en")
        self.prompt_en.delete("1.0", tk.END)
        self.prompt_en.insert("end", translation)

    def clear(self):
        self.prompt_es.delete("1.0", tk.END)
        self.prompt_en.delete("1.0", tk.END)

     

    def copiar(self) :   
        text_a_copiar = self.prompt_en.get("1.0", tk.END)
        pyperclip.copy(text_a_copiar)         

    def create(self):
        #cantidad = self.cantidad.get()
        valid_sizes = [256, 512, 1024]
        value = self.size.get()
        if int(value) not in valid_sizes:
            messagebox.showerror("Error", "Solo valores: 256, 512, 1024")
            self.size.delete(0, "end")
            self.size.insert(0, "256")
            return
        if len(self.prompt_es.get("1.0", tk.END).strip()) == 0:
            messagebox.showerror("Error", "Ingrese un prompt en español")
            return
        if len(self.prompt_en.get("1.0", tk.END).strip()) == 0:
            messagebox.showerror("Error", "No hay traducción")
            return    
        if self.cantidad.get() != '1' and self.cantidad.get() != '2':
            messagebox.showerror("Error", "La cantidad solo puede ser 1 o 2.")
            return
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        translacion = self.prompt_en.get("1.0", tk.END).strip()
        cantidad = self.cantidad.get()
        miSize = self.size.get()

        res = openai.Image.create(
            prompt=translacion,
            n=int(cantidad),
            size=f'{miSize}x{miSize}',
            response_format="b64_json"
        )

        try:
            for i in range(0, len(res['data'])):
                b64 = res['data'][i]['b64_json']
                fecha_actual = time.strftime("%Y-%m-%d")
                imagenName = fecha_actual + f"-{translacion[:8]}" + ".png"
                filename = 'imagenes\\' + imagenName
                print('Saving file ' + filename)
                with open(filename, 'wb') as f:
                    f.write(base64.urlsafe_b64decode(b64))
                filename = 'G:/Mi unidad/Dall-e/' + imagenName
                with open(filename, 'wb') as f:
                    f.write(base64.urlsafe_b64decode(b64)) 
                img = Image.open(BytesIO(base64.urlsafe_b64decode(b64)))  
                photo = ImageTk.PhotoImage(img)
                self.image_label = tk.Label(self.master, image=photo)
                self.image_label.image = photo
                self.image_label.grid(row=12, column=1, rowspan=3)
        except Exception as e:
            messagebox.showerror("Error", f'Error: {e}')
            print(f'Error: {e}')

root = tk.Tk()
app = App(master=root)
root.mainloop()