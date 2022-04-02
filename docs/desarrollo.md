# Depdencias de desarrollo para la versión 0.1.0

* [Python versión ^3.10](https://www.python.org/downloads/)
* Poetry (ver instrucciones de instalación más abajo)
* [Docker](https://www.docker.com/products/docker-desktop/)
* [Docker Compose](https://docs.docker.com/compose/install/) (Incluído en Docker-Desktop)

# Detalles de instalación de entorno de desarrollo
* Instalar Python 3.10, cualquier versión sobre 3.10 sirve. No debería dar mayores problemas independiente de tu sistema operativo.
* Instalar poetry usando el comando ``pip install poetry``. Si tienes más de una versión de python instalada, asegúrate de que
se haya instalado con la versión 3.10.
* Configurar poetry para crear el entorno de trabajo en la carpeta de proyecto con el comando ``poetry config virtualenvs.in-project true``.
* Clonar repositorio de github y navegar a la carpeta del proyecto.
* Instalar las dependencias del proyecto con ``poetry install``.
* Copia el archivo ``ejemplo.env`` y renombralo a ``.env``, llena los datos según corresponda (Lo único que deberías cambiar sería ``DB_HOST`` a ``localhost`` si estás corriendo el proyecto desde tu IDE).
* Instalar Docker. En el caso de Windows y Mac puedes usar Docker Desktop, que tiene interfaz gráfica e incluye Docker Compose. 
Linux tendrá que seguir las instrucciones de instalación de [aquí](https://docs.docker.com/engine/install/ubuntu/) y [aquí](https://docs.docker.com/compose/install/).
* Correr el proyecto en modo desarrollo usando el comando ``docker-compose -f dev-compose.yml up``. Instalará la base de datos y el entorno
aislado de docker la primera vez, por lo que puede tomar un tiempo.
* Si quieres correr el proyecto desde tu IDE para probar cambios o hacer debug, puedes comentar en ``dev-compose.yml`` la sección del servicio ``web``
y sólo levantará la base de datos.
