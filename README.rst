dump_server
===========

:Author:  Pierre-Yves Chibon <pingou@pingoured.fr>

This is a simple flask-based web application returning the information sent.
It can be used to debug web-hooks for example.

Just run the server and send any GET or POST request to it and it will return
you a JSON object with all the information it could gather about your request as
well as printing this JSON object in the logs of the server.


Get it running
==============

* Retrieve the sources::

    git clone https://pagure.io/pingou/dump_server
    cd dump_server

* Install dependencies

  * create the virtualenv::

      virtualenv sd_env
      source ./sd_env/bin/activate

  * Install the rest of the dependencies::

      pip install flask

* Run the application::

    python dump_server.py


This will launch the application at http://127.0.0.1:5000

To change the host, port or see more options check the help with::

    python dump_server.py --help
