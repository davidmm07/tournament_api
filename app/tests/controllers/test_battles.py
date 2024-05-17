from flask_testing import TestCase
from app import app, db
from app.models.battles import Battles
from http import HTTPStatus
import json

from app.models.monsters import Monsters


class BattlesControllerTests(TestCase):
    def create_app(self):
        app.config.from_object('config.ConfigTest')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.drop_all()
        db.session.commit()


class TestListApi(BattlesControllerTests):
    def test_get_monster_list_with_success(self):
        battle1 = Battles(monster_a=1, monster_b=2, winner=1)
        battle2 = Battles(monster_a=1, monster_b=2, winner=2)
        db.session.add_all([battle1, battle2])
        db.session.commit()

        with app.test_client() as c:
            monsters_list = c.get('/battles/')
            assert monsters_list.status_code == HTTPStatus.OK
            assert len(monsters_list.json) > 0
        return


class TestCreateApi(BattlesControllerTests):
    def test_create_should_fail_when_trying_a_battle_of_monsters_with_an_undefined_monster(self):  # noqa: E501
        # TODO
        battle = {"monsterA": None, "monsterB": 2}

        with app.test_client() as c:
            response = c.post('/battles/', data=json.dumps(battle),
                              content_type='application/json')
            assert response.status_code == HTTPStatus.BAD_REQUEST
        return

    def test_create_should_fail_when_trying_a_battle_of_monsters_with_an_inexistent_monster(self):  # noqa: E501
        # TODO
        battle = {"monsterA": 1, "monsterB": 40}
        with app.test_client() as c:
            response = c.post('/battles/', data=json.dumps(battle),
                              content_type='application/json')
            assert response.status_code == HTTPStatus.NOT_FOUND
        return

    def test_create_should_insert_a_battle_of_monsters_successfully_with_monster_1_winning(self):  # noqa: E501
        # TODO
        monsterA = Monsters(name='testA', speed=200,
                            attack=200, defense=100, hp=100, imageUrl='')
        monsterB = Monsters(name='testB', speed=100,
                            attack=100, defense=100, hp=100, imageUrl='')
        db.session.add_all([monsterA, monsterB])
        db.session.commit()
        battle = {"monsterA": monsterA.id, "monsterB": monsterA.id}
        with app.test_client() as c:
            response = c.post('/battles/', data=json.dumps(battle),
                              content_type='application/json')
            assert response.status_code == HTTPStatus.OK
            assert response.json['winner'] == battle['monsterA']
        return

    def test_create_should_insert_a_battle_of_monsters_successfully_with_monster_2_winning(self):  # noqa: E501
        # TODO
        monsterA = Monsters(name='testA', speed=200,
                            attack=300, defense=100, hp=200, imageUrl='')
        monsterB = Monsters(name='testB', speed=400,
                            attack=200, defense=100, hp=200, imageUrl='')
        db.session.add_all([monsterA, monsterB])
        db.session.commit()
        battle = {"monsterA": monsterA.id, "monsterB": monsterA.id}
        with app.test_client() as c:
            response = c.post('/battles/', data=json.dumps(battle),
                              content_type='application/json')
            assert response.status_code == HTTPStatus.OK
            assert response.json['winner'] == battle['monsterB']
        return


class TestDeleteApi(BattlesControllerTests):
    def test_delete_should_delete_a_battle_successfully(self):
        # TODO
        battle = Battles(monster_a=3, monster_b=4, winner=3)
        db.session.add(battle)
        db.session.commit()

        with app.test_client() as c:
            monsters = c.delete(f'/battles/{battle.id}')
            assert monsters.status_code == HTTPStatus.OK
        return

    def test_delete_should_return_404_if_the_battle_does_not_exists(self):
        # TODO
        NOT_EXISTS_ID = 76
        with app.test_client() as c:
            monsters = c.delete(f'/battles/{NOT_EXISTS_ID}')
            assert monsters.status_code == HTTPStatus.NOT_FOUND
        return
