from flask_testing import TestCase
from app import app, db
from app.models.monsters import Monsters

class MonstersModelTests(TestCase):
    def create_app(self):
        app.config.from_object('config.ConfigTest')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.drop_all()
        db.session.commit()

class TestMonsterModel(MonstersModelTests):
    def test_model_should_map_the_properties_correctly(self):
        monster = Monsters( name='test1', speed=100, attack=100, defense=100, hp=100, imageUrl='')
        db.session.add(monster)
        db.session.commit()
        
        assert monster.name == 'test1'
        assert monster.speed == 100
        assert monster.attack == 100
        assert monster.defense == 100
        assert monster.hp == 100
        assert monster.imageUrl == ''

        return

    def test_monster_model_should_have_relationship_with_battle_model(self):
        relationships = Monsters.__mapper__.relationships
        assert len(relationships) == 1
        return
