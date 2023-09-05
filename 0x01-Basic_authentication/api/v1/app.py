#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from api.v1.auth.auth import Auth


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
auth = getenv("AUTH_TYPE")


if auth == "auth":
    auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """
    Error handler for unauthorized personnel
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """
    Error handler for authorized but wants to access
    forbidden resources
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def check_auth() -> str:
    """
    Checks the path for authentication before_request
    """
    auth_header = auth.authorization_header(request)
    auth_user = auth.current_user(request)

    if auth is None:
        pass
    no_auth_list = [
            '/api/v1/status/',
            '/api/v1/unauthorized/',
            '/api/v1/forbidden/'
            ]
    authenticated = auth.require_auth(request.path, no_auth_list)

    if not authenticated:
        pass
    else:
        if not auth_header:
            abort(401)
        if not auth_user:
            abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
