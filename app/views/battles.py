#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import Blueprint, request
import app.controllers.battles as Battles

battles_bp = Blueprint('battles', __name__)

@battles_bp.route('/')
def list_battles():
    return Battles.get_list()

@battles_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    print(data)
    return Battles.start(data)

@battles_bp.route('/<int:battle_id>', methods=['DELETE'])
def remove(battle_id: int):
    return Battles.remove(battle_id)