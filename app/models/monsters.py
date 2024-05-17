#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from typing import List
from app import db


class Monsters(db.Model):
    __tablename__ = 'monsters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String, nullable=True)

    def __init__(self, name, speed, attack, defense, hp, imageUrl):
        self.name = name
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.imageUrl = imageUrl
