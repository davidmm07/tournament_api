#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from app import db

class Battles(db.Model):
    __tablename__ = 'battles'

    id = db.Column(db.Integer, primary_key=True)
    monsterA = db.Column(db.Integer, db.ForeignKey(
        'monsters.id'), nullable=False)
    monsterB = db.Column(db.Integer, db.ForeignKey(
        'monsters.id'), nullable=False)
    winner = db.Column(db.Integer, db.ForeignKey(
        'monsters.id'), nullable=False)
    # This last line allows you to access all Battle objects associated with a monster

    def __init__(self, monster_a, monster_b, winner):
        self.monsterA = monster_a
        self.monsterB = monster_b
        self.winner = winner
