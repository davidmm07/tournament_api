#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from http import HTTPStatus
from flask import Blueprint, request, make_response
from flask.json import jsonify
from marshmallow import ValidationError
import app.controllers.monsters as monsters_controller

monsters_bp = Blueprint('monsters', __name__)

@monsters_bp.route('/', methods=['POST'])
def create():
    params = request.json
    if not params:
        return "json parameter is required", HTTPStatus.BAD_REQUEST

    return monsters_controller.create(params)
@monsters_bp.route('/', methods=['GET'])
def get_list():
    return monsters_controller.get_list()
@monsters_bp.route('/<int:monster_id>', methods=['GET'])
def get(monster_id: int):
    return monsters_controller.get(monster_id)

@monsters_bp.route('/<int:monster_id>', methods=['PUT'])
def update(monster_id: int):
    params = request.json
    if not params:
        return "json parameter is required", HTTPStatus.BAD_REQUEST

    return monsters_controller.update(monster_id, params)

@monsters_bp.route('/<int:monster_id>', methods=['DELETE'])
def remove(monster_id: int):
    return monsters_controller.remove(monster_id)

@monsters_bp.route('/import', methods=['POST'])
def import_csv():
    try:
        file = request.files['monsters']
        if not file:
            return "a csv file is required", HTTPStatus.BAD_REQUEST
        response = make_response(monsters_controller.import_csv(file))
        response.status_code = HTTPStatus.OK
    except ValidationError as e:
        return jsonify({"error": e.messages}), HTTPStatus.BAD_REQUEST
    return response
