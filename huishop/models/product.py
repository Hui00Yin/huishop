import datetime as dt
from huishop.extensions import db
from huishop.database import (
    Column,
    Model,
    ReferenceCol,
    relationship,
    SurrogatePK,
)

class Product( SurrogatePK, Model):

    __tablename__ = 'product'
    category_id= ReferenceCol('category', nullable=True)
    category = relationship('Category', backref='product')

    name = Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)

    def __init__(self, name, description, **kwargs):
        db.Model.__init__(self, name=name, description=description, **kwargs)

    def __repr__(self):
        return '<name {}, description {}, category {}>'.format(self.name, self.description, self.category.name)
