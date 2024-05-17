from flask_testing import TestCase
from app import app, db
from app.models.battles import Battles

class BattleModelTests(TestCase):
    def create_app(self):
        app.config.from_object('config.ConfigTest')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.drop_all()
        db.session.commit()

class TestMonsterModel(BattleModelTests):
    def test_battle_model_should_have_relationships_with_monster_model(self):
        relationships = Battles.__mapper__.relationships
        assert len(relationships) == 1
        return

    def test_battle_model_should_have_foreign_keys_with_monster_model(self):
        columns = Battles.__mapper__.columns
        assert len(columns['monsterA'].foreign_keys) == 1
        assert len(columns['monsterB'].foreign_keys) == 1
        assert len(columns['winner'].foreign_keys) == 1
        return
