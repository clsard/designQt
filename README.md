# pruebasQt
## Sobre la consola
### La mejor opción es la consola de GIT que se encuentra en:
### "C:\Program Files\Git\bin\bash.exe"
## Crear entornos virtuales Python: 
*https://www.youtube.com/watch?v=2kLYOzNb3uU*

>En la consola:

Debemos de instalar virtualenv en el entorno global

 **$ pip install virtualenv**

 >A continuación creamos la carpeta raiz del entorno, en este caso *(env)*

**$ virtualenv env**

>Hemos creado una carpeta llamada *(env)* donde se ha guardado todo lo necesario
para que sea un entorno virtual

    Nota: Es conveniente utilizar este nombre o .env por normalización y ponerselo más facil a por ejemplo a GitHub

>Para **activar** el entorno utilizaremos el comando ***(source)***

**$ source env/Scripts/activate**

Si queremos ***desactivar*** el entorno:

**$ source env/Scripts/deactivate**

    ***OJO*** el path indicado depende de donde estemos en ese momento

>*En el caso de las dos instrucciones anteriores estariamos, por ejemplo en:* ***"c:\github\"** o bien en **"c:\proyectos\python\"***
*con lo cual la ruta completa sería con este segundo ejemplo **"C:\proyectos\python\env\"***

## Actualizar pip
>cmd (windows)

>para activar entorno virtual: *env/Scripts/activate.bat*

>Cambiará el prompt:

***(env) Q:\github\env\\***

>Siguiente instruccion actualizará pip

***python -m pip install -U pip***

>URL de mucho interes sobre QT

https://doc.qt.io/qtforpython/gettingstarted/windows.html#creating-a-virtual-environment

>otra URL fundamental para QT

https://www.qt.io/product/features?hsLang=en






