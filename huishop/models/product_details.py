import datetime as dt
from huishop.extensions import db
from huishop.database import (
    Column,
    db,
    Model,
    ReferenceCol,
    relationship,
    SurrogatePK,
)

class Details( SurrogatePK, Model):
    __tablename__ = 'product_details'
    product_id= ReferenceCol('product', nullable=True)
    product = relationship('Product', backref='details')
    sku = Column(db.String(255),nullable=True)
    price = Column(db.Numeric(precision=12, scale=2, asdecimal=False, decimal_return_scale=None))
    weight = Column(db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None))

    longth = Column(db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None))
    width = Column(db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None))
    height = Column(db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None))

    main_image = Column(db.String(500))
    sub_images = Column(db.Text())

    stock = Column(db.Integer, nullable=True)
    status = Column(db.Integer, nullable=True)

    def __init__(self, sku, price, stock, status, **kwargs):
        db.Model.__init__(self, sku=sku, stock=stock, status=status, **kwargs)

    def __repr__(self):
        return '<sku {}>'.format(self.sku)
