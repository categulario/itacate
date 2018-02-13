Itacate
=======

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

.. code-block:: python

   # settings_develop.py
   DEBUG = True
   SECREY_KEY = 'lalala'

.. code-block:: python

   # module.py
   from itacate import Config
   import os

   config = Config(os.path.dirname(os.path.realpath(__file__)))
   config.from_pyfile('settings.py')
   config.from_envvar('MY_APP_SETTINGS', silent=False) # export MY_APP_SETTINGS=/path/to/settings_develop.py

   assert config.DEBUG == True
   assert config.BE_MAGIC == True
   assert config.SECREY_KEY == 'lalala'
