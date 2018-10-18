# -*- coding: utf-8 -*-

"""
 (c) 2016 - Copyright Red Hat Inc

 Authors:
   Pierre-Yves Chibon <pingou@pingoured.fr>

"""
from __future__ import unicode_literals, print_function

__version__ = '1.0'

import logging

import flask

# Create the application.
APP = flask.Flask(__name__)


@APP.route('/')
@APP.route('/<path:path>')
def main_get(path=None):  # pragma: no cover
    """ Main endpoint receiving the GET requests. """
    output = {
        'method': 'GET',
        'args': flask.request.args,
        'values': flask.request.values,
        'form': flask.request.form,
        'path': path,
    }
    jsonout = flask.jsonify(output)
    #print(flask.request.headers)
    print(jsonout.get_data(as_text=True))
    return jsonout


@APP.route('/', methods=['POST'])
@APP.route('/<path:path>', methods=['POST'])
def main_post(path=None):  # pragma: no cover
    """ Main endpoint receiving the POST requests. """
    output = {
        'method': 'POST',
        'args': flask.request.args,
        'values': flask.request.values,
        'form': flask.request.form,
        'json': flask.request.json,
        'path': path,
    }
    jsonout = flask.jsonify(output)
    print(flask.request.headers)
    print(jsonout.get_data(as_text=True))
    return jsonout


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(
        description='Run the web app')
    parser.add_argument(
        '--debug', dest='debug', action='store_true',
        default=False,
        help='Expand the level of data returned.')
    parser.add_argument(
        '--port', '-p', default=5000,
        help='Port for the Pagure to run on.')
    parser.add_argument(
        '--host', default="127.0.0.1",
        help='Hostname to listen on. '
        'When set to 0.0.0.0 the server is available externally. '
        'Defaults to 127.0.0.1 making the it only visable on localhost')

    args = parser.parse_args()

    APP.debug = True
    APP.run(host=args.host, port=int(args.port))
