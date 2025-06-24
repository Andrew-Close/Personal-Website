from ..extensions import db
from ..models import ImageModel

class ImagesManager():
    def select_all_images(self):
        return db.session.execute(db.select(ImageModel)).scalars().all()