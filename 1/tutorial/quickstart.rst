Быстрый старт
===========


Минимальное приложение
----------------------

.. code-block:: python

  from flask import Flask
  app = Flask(__name__)


  @app.route("/")
  @app.route("/home")
  def home():
      return "<h1>Home Page</h1>"


  @app.route("/about")
  def about():
      return "<h1>About Page</h1>"


  if __name__ == '__main__':
      app.run(debug=True)

Роутинг
--------

Для задания путей, которые обрабатывается сайтом используется декоратор

.. code-block:: python

  @app.route("/")

  В кавычках указывается путь.
