from app import ma, db
from app.models.monsters import Monsters

class MonsterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Monsters
        load_instance = True
        sqla_session = db.session
