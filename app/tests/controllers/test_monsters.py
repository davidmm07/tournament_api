import json
import io
from flask_testing import TestCase
from app import app, db
from app.models.monsters import Monsters
from http import HTTPStatus


class MonstersControllerTests(TestCase):
    def create_app(self):
        app.config.from_object('config.ConfigTest')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.drop_all()
        db.session.commit()


class TestListApi(MonstersControllerTests):
    def test_get_monster_list_with_success(self):
        monster1 = Monsters(name='test1', speed=100,
                            attack=100, defense=100, hp=100, imageUrl='')
        monster2 = Monsters(name='test2', speed=100,
                            attack=100, defense=100, hp=100, imageUrl='')
        db.session.add_all([monster1, monster2])
        db.session.commit()

        with app.test_client() as c:
            monsters_list = c.get('/monsters/')
            assert monsters_list.status_code == HTTPStatus.OK
            assert len(monsters_list.json) > 0
        return


class TestGetApi(MonstersControllerTests):
    def test_get_by_id_with_success(self):
        monster = Monsters(name='test1', speed=100, attack=100,
                           defense=100, hp=100, imageUrl='')
        db.session.add(monster)
        db.session.commit()

        with app.test_client() as c:
            monsters = c.get('/monsters/1')
            assert monsters.json['name'] == 'test1'
            assert monsters.status_code == HTTPStatus.OK
        return

    def test_get_by_id_return_404_if_monster_do_not_exists(self):
        with app.test_client() as c:
            monsters = c.get('/monsters/9999')
            assert monsters.status_code == HTTPStatus.NOT_FOUND
        return


class TestCreateApi(MonstersControllerTests):
    def test_create_with_success(self):
        monster = {'name': 'test1', 'speed': 100, 'attack': 100,
                   'defense': 100, 'hp': 100, 'imageUrl': ''}

        with app.test_client() as c:
            monsters = c.post(
                '/monsters/', data=json.dumps(monster), content_type='application/json')
            assert monsters.json['name'] == 'test1'
            assert monsters.status_code == HTTPStatus.OK
        return


class TestUpdateApi(MonstersControllerTests):
    def test_update_with_success(self):
        monster = Monsters(name='test1', speed=100, attack=100,
                           defense=100, hp=100, imageUrl='')
        db.session.add(monster)
        db.session.commit()
        update_params = {'name': 'test2'}

        with app.test_client() as c:
            monsters = c.put(
                '/monsters/1', data=json.dumps(update_params), content_type='application/json')
            assert monsters.json['name'] == 'test2'
            assert monsters.status_code == HTTPStatus.OK
        return

    def test_update_return_404_if_monster_do_not_exists(self):
        update_params = {'name': 'test2'}

        with app.test_client() as c:
            monsters = c.put(
                '/monsters/9999', data=json.dumps(update_params), content_type='application/json')
            assert monsters.status_code == HTTPStatus.NOT_FOUND
        return


class TestDeleteApi(MonstersControllerTests):
    def test_delete_with_success(self):
        monster = Monsters(name='test1', speed=100, attack=100,
                           defense=100, hp=100, imageUrl='')
        db.session.add(monster)
        db.session.commit()

        with app.test_client() as c:
            monsters = c.delete('/monsters/1')
            assert monsters.status_code == HTTPStatus.OK
        return

    def test_delete_return_404_if_monster_do_not_exists(self):
        with app.test_client() as c:
            monsters = c.delete('/monsters/9999')
            assert monsters.status_code == HTTPStatus.NOT_FOUND
        return


class TestImportCsvApi(MonstersControllerTests):
    def test_import_should_fail_when_importing_csv_with_an_empty_monster(self):

        path_file = 'data/monsters-empty-monster.csv'
        with open(path_file, 'r') as file:
            csv_data = file.read()
        data = {'monsters': (io.BytesIO(csv_data.encode()), path_file)}
        with app.test_client() as c:
            response = c.post('/monsters/import', data=data)
            assert len(response.json['error']) > 0
            assert response.status_code == HTTPStatus.BAD_REQUEST
        return

    def test_import_should_fail_when_importing_csv_with_a_missing_column(self):

        path_file = 'data/monsters-wrong-column.csv'
        with open(path_file, 'r') as file:
            csv_data = file.read()
        data = {'monsters': (io.BytesIO(csv_data.encode()), path_file)}
        with app.test_client() as c:
            response = c.post('/monsters/import', data=data)
            assert len(response.json['error']) > 0
            assert response.status_code == HTTPStatus.BAD_REQUEST
        return

    def test_import_should_insert_all_the_csv_lines_into_the_database_successfully(self):

        path_file = 'data/monsters-correct.csv'
        with open(path_file, 'r') as file:
            csv_data = file.read()
        data = {'monsters': (io.BytesIO(csv_data.encode()), path_file)}
        with app.test_client() as c:
            response = c.post('/monsters/import', data=data)
            assert response.status_code == HTTPStatus.OK
        return
