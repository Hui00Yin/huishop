# -*- coding: utf-8 -*-
import datetime as dt

from huishop.extensions import db
from huishop.database import (
    Column,
    Model,
    ReferenceCol,
    relationship,
    SurrogatePK,
)

class Category(SurrogatePK, Model):
    __tablename__ = 'category'
    parent_id = db.Column(db.Integer)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)
    create_time = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    update_time = db.Column(db.DateTime)

    def __init__(self, name,description, **kwargs):
        db.Model.__init__(self, name=name,description=description, **kwargs)

    def __repr__(self):
        return '<Category({name})>'.format(name=self.name)
