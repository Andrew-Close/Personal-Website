from ..extensions import db
from ..models import LocationModel

class LocationsManager:
    def select_all_locations(self):
        return db.session.execute(db.select(LocationModel)).scalars().all()