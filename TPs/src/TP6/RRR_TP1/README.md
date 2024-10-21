Extractor de token para acceso API Servicios Banco XXX (versión 1.0)

Este programa permite extraer la clave de acceso API para utilizar los servicios del 
Banco XXX.

El programa operará como un microservicio invocado mediante:

        {path ejecutable}/getJason.pyc {path archivo JSON}/{nombre archivo JSON}.json
        C:\Users\Nicolás Cardinaux\Desktop\RRR_TP1\getJason.pyc C:\Users\Nicolás Cardinaux\Desktop\RRR_TP1\sitedata.json

ej.
        ./getJason.pyc ./sitedata.json
        python .\getJason-3.6.pyc .\sitedata.json token2

El token podrá recuperarse mediante el standard output de ejecución en el formato

       {1.0}XXXX-XXXX-XXXX-XXXX

Para obtener un mensaje de ayuda detallado ejecutar

       ./getJason.pyc -h

Excepciones

Todas las condiciones de error del programa deben producir un mensaje de error bajo su control antes de
terminar.


