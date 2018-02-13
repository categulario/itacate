Itacate
=======

.. image:: https://travis-ci.org/categulario/itacate.svg?branch=master
    :target: https://travis-ci.org/categulario/itacate

*Itacatl: Provisión de comida que se lleva para un viaje o un paseo, o que ha sobrado de una fiesta y se da a algunos invitados.*

El módulo de configuración de flask para el resto del mundo, por que me gusta cómo funciona. Escribe tus configuraciones en archivos python e impórtalas según el entorno, sobreescribiéndolas en cascada.

The `config` module from `flask` for the rest of the world, just because I like how it works. Write your config files in normal python files and import them depending on environment variables. Overwrite them in cascade.

Cómo usar / Usage
-----------------

.. code-block:: python

   # settings.py
   DEBUG = False
   BE_MAGIC = True
   SECREY_KEY = ''
   FIZ_BOZ = 15
   STORAGE_DIR = 'media'
   DB_NAME = 'mysql'

.. code-block:: python

   # settings_develop.py
   DEBUG = True

.. code-block:: json

   # settings.json
   {
      "FIZ_BOZ": 10
   }

.. code-block:: python

   # module.py
   from itacate import Config
   import os

   class MyObject:
      STORAGE_DIR = '/var/www/media'

   DB_NAME = 'postgres'

   config = Config(os.path.dirname(os.path.realpath(__file__)))
   config.from_pyfile('settings.py')
   config.from_envvar('MY_APP_SETTINGS', silent=False) # export MY_APP_SETTINGS=/path/to/settings_develop.py
   config.from_mapping({
      'SECREY_KEY': 'lalala',
   })
   config.from_json('settings.json')
   config.from_object(MyObject)
   config.from_object(__name__) # from this same module!

   assert config.BE_MAGIC == True
   assert config.DEBUG == True
   assert config.FIZ_BOZ == 10
   assert config.SECREY_KEY == 'lalala'
   assert config.STORAGE_DIR == '/var/www/media'
   assert config.DB_NAME == 'postgres'
