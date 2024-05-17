from http import HTTPStatus
from marshmallow import ValidationError
from app.models.battles import Battles
from app.models.monsters import Monsters
from app.schemas.battles import BattleSchema
from app import db
from flask import jsonify


def get_list() -> dict:
    battle = Battles.query.all()
    battle_schema = BattleSchema(many=True)
    response = battle_schema.jsonify(battle)
    return response


def start(data):
    monster_a_id = data.get('monsterA')
    monster_b_id = data.get('monsterB')
    if not monster_a_id or not monster_b_id:
        return jsonify({'message': 'Monster undefined!'}), HTTPStatus.BAD_REQUEST
    monster_a: Monsters = Monsters.query.get(monster_a_id)
    monster_b: Monsters = Monsters.query.get(monster_b_id)

    if not monster_a or not monster_b:
        return jsonify({'message': 'Both Monster should exist!'}), HTTPStatus.NOT_FOUND

    while monster_a.hp > 0 and monster_b.hp > 0:
        if monster_a.speed > monster_b.speed:
            attack_monster = monster_a
            defense_monster = monster_b
        elif monster_a.speed < monster_b.speed:
            attack_monster = monster_b
            defense_monster = monster_a
        else:
            if monster_a.attack > monster_b.attack:
                attack_monster = monster_a
                defense_monster = monster_b
            else:
                attack_monster = monster_b
                defense_monster = monster_a
        damage = attack_monster.attack - defense_monster.defense
        if damage <= 0:  # attack is equal to or lower than defense
            damage = 1

        defense_monster.hp -= damage

    winner: Monsters = monster_a if monster_a.hp > 0 else monster_b
    battle = Battles(monster_a=monster_a_id,
                     monster_b=monster_b_id, winner=winner.id)
    db.session.add(battle)
    db.session.commit()
    return jsonify({'winner': winner.id}), HTTPStatus.OK


def remove(battle_id: int):
    battle = Battles.query.get(battle_id)
    if not battle:
        return jsonify({'message': 'Battle not found'}), HTTPStatus.NOT_FOUND
    db.session.delete(battle)
    db.session.commit()
    return "Deleted", HTTPStatus.OK
