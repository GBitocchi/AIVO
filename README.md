# challenge-aivo
Proyecto que cumple los requerimientos especificados en el challenge de Aivo

## Ejecución del proyecto

  * Pullear el repositorio en la carpeta que se desee.
  * Ingresar a la terminal y ubicarse en la carpeta del repositorio donde fue pulleado el proyecto.
  * Ejecutar el siguiente comando: env\Scripts\activate.bat para ingresar al entorno virtual.
  * Una vez ingresado al mismo, ingresar el comando flask run para ejecutar el proyecto.

## Uso de la aplicación

Ahora que se esta ejecutando el proyecto en localhost:5000, podremos realizar una peticion GET para obtener los paises que cumplen con la condición de un indice determinado que sea mayor a un valor ingresado. Un ejemplo del mismo seria la siguiente URL:

localhost:5000/api/v1.0/countries/Labour market insecurity/12.3

Que nos devolvera un resultado json de los paises que cumplen la condición de que posean un indice de "Labour market insecurity" mayor a 12.3
