## ME.LI Challenge

API Rest para validación de mutantes (?)

# Información general
Desarrollado en Python bajo el framework Flask.

Posee 2 servicios rest hosteados en HEROKU **https://warm-river-14812.herokuapp.com/**
Integrado con base de datos MongoDB hosteada en <https://cloud.mongodb.com>

# Levantar el ambiente de desarrollo
Se utilizó un entorno virtual para instalar las dependencias necesarias, venv que viene incluido con python
Para instalarlo, dentro de la carpeta del proyecto, ejecutar:
``` python -m  venv venv ```

Una vez instalado para la activación del ambiente, ejecutar:
``` venv\Scripts\activate ```

Una vez activado el entorno virtual, seguir los siguientes pasos:

1. Instalar las dependencias del archivo requirements.txt ``` pip install -r requirements.txt ```
2. Indicar el main de la aplicación ``` $env:FLASK_APP = "app.py" ```
3. Levantar la aplicación desde el entorno virtual: ``` python -m flask run ```
4. Para la construcción e instalación del paquete: ``` pip install wheel ```
5. Construir el proyecto ejecutando ``` python setup.py bdist_wheel ```
6. Tomar el archivo de extensión whl generado en la carpeta /dist y ejecutando ````pip install nombreArchivo.whl``` esta listo para ejecutar.

# Instalación instancia propia MongoDB
1. Descargar la versión correspondiente para el SO que se utilice. http://www.mongodb.org/downloads
2. Una vez instalado mongoDB se debe levantar una instancia con el comando ``` mongod ```
3. En la aplicación se utiliza el puerto defautl que provee la conexion de la db. Port: 27017.  
    a. Se utiliza un repository de nombre "MutantAPI"
    b. Se crea una collection hummansRepository donde se guarda la información de los DNAs

# Otras herramientas utilizadas
1. Postman para pruebas de servicos rest. https://www.postman.com/
2. Sonarlint para análisis de codigo. https://www.sonarlint.org/

# Pruebas
A traves de la libreria unittest se configuraron las siguientes pruebas:
- humano_no_mutante: Validación de dna con resutaldo False.
- humano_mutante: Validación de dna con resultado True
- humano_invalido: Validacion de dna con datos incorrectos.
- humano_mutante_horizontal: Diferentes casos de resutados positivos.
- humano_mutante_vertical: Diferentes casos de resutados positivos.
- humano_mutante_diagonal: Diferentes casos de resutados positivos.
- obtener_estadisticas: Obtener estadisticas de la base de datos.
- method_invalid: Ejecución servicio /mutant con method invalido.
- method_ok_no_json: Ejecución servicio /mutant sin request body.
- stats_ok: Prueba servicio rest /stats
Para ejecutar estas pruebas unitarias se debe ejecutar el sigueinte comando:
``` python -m unittest  ```

Se generó una rutina de python <ejecuta_servicios.py> para probar el servicio de forma autonoma y con posibilidad de realizar carga:
Acciones de la prueba:
1. Genera automaticamente los json de forma aleatoria.
2. Ejecuta el servicio /mutant/ con el json generado.
3. Guarda la respuesta en un archivo prueba.txt con el siguiente formato    
    YYYY/MM/D HH:mm:SS - Servicio: http://127.0.0.1:5000/mutant/ - Estado: code_result_http
4. Ejecuta el servicio /stats 
5. Guarda la respuesta en el archivo prueba.txt con el siguiente formato
    YYYY/MM/D HH:mm:SS - Servicio: http://127.0.0.1:5000/stats - Estado: body_response

Estos pasos descriptos estan conifigurados en un loop inicial de 10 ejecuciones, se puede modificar a la cantidad que se crea conveniente:
<Linea 8: for i in range(10):>


## Diagrama de Secuencia

![Secuencia](/doc/secuencia.png)


# ToDo / Mejoras a evaluar
 - Pensando en la carga de usuarios que se podria dar se debe considerar la implementación de cache para que las validaciones no se realicen con la db.
    FlaskCache sería una buena opcion, posee los siguientes tipos de cache:
        - SimpleCache
        - MemcachedCache (se requiere pylibmc o memcache)
        - GAEMemcachedCache 
        - RedisCache (se requiere Werkzeug 0.7)
        - FileSystemCache
        - SASLMemcachedCache (se requiere pylibmc)
    URL: https://pythonhosted.org/Flask-Cache/ 

- Se podría utilizar FastAPI para generar la documetación de las API en el caso de que se quieran generar mas servicios y la libreria tiene integrado el uso de async and await para ejecutar los servicios de forma asincrona. 
    URL: https://fastapi.tiangolo.com/

