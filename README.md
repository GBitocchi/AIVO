# challenge-aivo
Proyecto que cumple los requerimientos especificados en el challenge de Aivo, realizado con Python 3.9

## Ejecución del proyecto en un entorno virtual

  * Pullear el repositorio en la carpeta que se desee
  * Ingresar como administrador a la terminal y ubicarse en la carpeta del repositorio donde fue pulleado el proyecto
  * Verificar tener instalado virtualenv en el sistema. Caso contrario ingresar el comando pip install virtualenv --user
  * Creamos el entorno virtual en la carpeta del proyecto con el comando: python -m virtualenv -p UBICACION_EXE_DE_PYTHON_3_EN_SU_SISTEMA env
  * Modificar el fichero activate.bat que se encuentra en challenge-aivo/env/Scripts/activate.bat y agregar las siguientes variables de entorno al comienzo del mismo:
     * export FLASK_APP="entrypoint:app"
     * export FLASK_ENV="development"
     * export APP_SETTINGS_MODULE="config.default"
  * Ejecutar el siguiente comando: env\Scripts\activate.bat para ingresar al entorno virtual
  * Instalamos las bibliotecas del proyecto con el comando: pip install -r requirements.txt
  * Ahora podremos ejecutar el proyecto con el comando: flask run

## Uso de la aplicación

Ahora que se esta ejecutando el proyecto en localhost:5000, podremos realizar una peticion GET para obtener los paises que cumplen con la condición de un indice determinado que sea mayor a un valor ingresado. Un ejemplo del mismo seria la siguiente URL:

localhost:5000/api/v1.0/countries/Labour market insecurity/12.3

Que nos devolvera un resultado json de los paises que cumplen la condición de que posean un indice de "Labour market insecurity" mayor a 12.3
