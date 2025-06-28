from ..extensions import db
from ..models import ImageModel, LocationModel

class ImagesManager:
    def select_all_images(self):
        return db.session.execute(db.select(ImageModel)).scalars().all()

    def filter_by_date(self, start_date, end_date):
        if start_date is None and end_date is None:
            return db.session.execute(db.select(ImageModel)).scalars().all()
        # All dates given
        elif start_date is not None and end_date is not None:
            return db.session.execute(db.select(ImageModel).where(ImageModel.date.between(start_date, end_date))).scalars().all()
        # Start date given only
        elif start_date is not None:
            return db.session.execute(db.select(ImageModel).where(ImageModel.date > start_date)).scalars().all()
        # End date given only
        else:
            return db.session.execute(db.select(ImageModel).where(ImageModel.date < end_date)).scalars().all()

    def filter_by_location(self, location):
        if location is not None:
            return db.session.execute(db.select(ImageModel).join(LocationModel).where(LocationModel.location == location)).scalars().all()
        else:
            return db.session.execute(db.select(ImageModel)).scalars().all()