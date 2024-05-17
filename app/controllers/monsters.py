import io
from flask.json import jsonify
from marshmallow import ValidationError
from werkzeug.datastructures import FileStorage
from app.models.monsters import Monsters
import csv
from http import HTTPStatus
from app import db
from app.schemas.monsters import MonsterSchema


def create(data: dict) -> dict:
    monster_schema = MonsterSchema()
    try:
        monster_model = monster_schema.load(data, session=db.session)
        db.session.add(monster_model)
        db.session.commit()
    except ValidationError:
        return {"errors": "The monster schema is invalid."}, HTTPStatus.BAD_REQUEST  # noqa: E501
    return monster_schema.jsonify(monster_model)


def get(monster_id: int) -> dict:
    monster = Monsters.query.get(monster_id)
    if not monster:
        return jsonify({"message": "monster not found"}), HTTPStatus.NOT_FOUND
    monster_schema = MonsterSchema()
    response = monster_schema.jsonify(monster)
    return response


def get_list() -> dict:
    monster = Monsters.query.all()
    monster_schema = MonsterSchema(many=True)
    response = monster_schema.jsonify(monster)
    return response


def update(monster_id: int, data: dict) -> dict:
    monster = Monsters.query.get(monster_id)
    if not monster:
        return jsonify({"message": "monster not found"}), HTTPStatus.NOT_FOUND
    monster_schema = MonsterSchema()
    try:
        monster_model = monster_schema.load(
            data, session=db.session, instance=monster, partial=True)
    except ValidationError as err:
        return {"errors": err.messages}, HTTPStatus.BAD_REQUEST
    db.session.commit()
    return monster_schema.jsonify(monster_model)


def remove(monster_id: int):
    monster = Monsters.query.get(monster_id)
    if not monster:
        return jsonify({"message": "monster not found"}), HTTPStatus.NOT_FOUND
    db.session.delete(monster)
    db.session.commit()
    return "Deleted", HTTPStatus.OK


def import_csv(file: FileStorage):
    stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
    file_dict = csv.DictReader(stream)
    monster_schema = MonsterSchema(many=True)
    monster_model = monster_schema.load(file_dict, session=db.session)
    db.session.bulk_save_objects(monster_model)
    db.session.commit()
    return "ok"
