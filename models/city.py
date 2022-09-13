#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'))
    name = Column(String(128), primary_key=True)

    def __init__(self, *args, **kwargs):
        """City class init
        """
        super().__init__(*args, **kwargs)
