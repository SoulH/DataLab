Este proyecto es un pequeño ejemplo de una api escrita en flask, de acuerdo al postulado de la actividad 2 únicamente tiene un endpoint 
no obstante esta estructurado de tal forma que pueda crecer de una manera organizada con controladores separados e incluso versionado
usando para gestion de datos la implementación del patron repositorio (adaptado) sobre sqlalchemy

Uso

* crear y activar un virtualenv
* instalar los paquetes listados en requirements.txt en el virtualenv
* generar y editar con la data correspondiente un archivo .env segun ejemplo
* ejecutar en una terminal desde la raíz del proyecto el comando flask run

Endpoints

[GET] /proyectos/<id_proyecto>

        returns:
        {
            "proyectos": [...],
            "usuarios": [...]
        }
