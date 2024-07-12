Установка
==================

Python Version
---------------



Необходимые компоненты
----------------------
Следующие пакеты будут установлены при уставке Flask.


*  `Werkzeug` -реализация WSGI, стандартный интерфейс Python между приложением и серверов.
*  `Jinja` язык шаблонов, который визуализирует страницы которые отдает ваше приложение.
*  `MarkupSafe` пришел с  Jinja. Он защищает(изолирует) неразрешенный ввод при визуализации шаблонов недопуская атаки типа injection.
*  `ItsDangerous` безопансно подписывает данные гарантируя их целостность. Он используется для защиты cookie сессии.
*  `Click` фреймворк который обеспечивает интерфейс командной строки. Разрешает команду flask и добавляет настраивать командную строку.
*  `Blinker` обепечивает поддержку  Signals.

Опциональные зависимости
~~~~~~~~~~~~~~~~~~~~~~~~
Эти пакеты не ставятся автоматически. Но Flask определит и использует если вы их установите.


* `python-dotenv` включит запуски команды  ``flask``
  commands.
* `Watchdog` обеспечивает более эффективную перезагрузку сервера разработки.


greenlet
~~~~~~~~

Вы можете выбрат использовать `gevent` или `eventlet` в вашем приложении.
В таком случае greenlet>=1.0 . Когда исполье PyPy, PyPy>=7.3.7 нужен.

Это не минимально поддерживаемые версии, они только показывают первые в которых
есть поддержка этих возможностей. Вы должны использовать максимально последнюю версию
обоих компонентов.

Виртуальное окружение
---------------------

Use a virtual environment to manage the dependencies for your project, both in
development and in production.

What problem does a virtual environment solve? The more Python projects you
have, the more likely it is that you need to work with different versions of
Python libraries, or even Python itself. Newer versions of libraries for one
project can break compatibility in another project.

Virtual environments are independent groups of Python libraries, one for each
project. Packages installed for one project will not affect other projects or
the operating system's packages.

Python comes bundled with the :mod:`venv` module to create virtual
environments.


Создание виртуального окружения
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. group-tab:: macOS/Linux

      .. code-block:: text

         $ mkdir myproject
         $ cd myproject
         $ python3 -m venv .venv

   .. group-tab:: Windows

      .. code-block:: text

         > mkdir myproject
         > cd myproject
         > py -3 -m venv .venv

Активация виртуального окружения
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before you work on your project, activate the corresponding environment:

.. tabs::

  .. group-tab:: macOS/Linux

     .. code-block:: text

        $ . .venv/bin/activate

  .. group-tab:: Windows

     .. code-block:: text

        > .venv\Scripts\activate

Your shell prompt will change to show the name of the activated
environment.


Install Flask
--------------
Within the activated environment, use the following command to install
Flask:

.. code-block:: sh

    $ pip install Flask

Flask is now installed. Check out the :doc:`/quickstart` or go to the
:doc:`Documentation Overview </index>`.
