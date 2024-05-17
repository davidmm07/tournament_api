from app import ma, db
from app.models.battles import Battles

class BattleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Battles
        load_instance = True
        sqla_session = db.session
