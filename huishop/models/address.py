from huishop.extensions import db
from huishop.database import (
    Column,
    db,
    Model,
    ReferenceCol,
    relationship,
    SurrogatePK,
)

class Addresses( SurrogatePK, Model):
    __tablename__ = 'addresses'
    user_id= ReferenceCol('users', nullable=True)
    user = relationship('User', backref='addresses') 
    rcv_name = Column(db.String(80), nullable=False)
    rcv_phone = Column(db.String(20), nullable=False)
    province = Column(db.String(20), nullable=False)
    city = Column(db.String(20), nullable=False)
    district = Column(db.String(20), nullable=False)
    rcv_address = Column(db.String(200), nullable=False) 
    zip = Column(db.String(6), nullable=False)

    def __init__(self, name, phone, province, city, district, rcv_address, **kwargs):
        db.Model.__init__(self, name=name, phone=phone, province=province,city=city, district=district, rcv_address=rcv_address, **kwargs)

    def __repr__(self):
        return '<name {}>'.format(self.name)
