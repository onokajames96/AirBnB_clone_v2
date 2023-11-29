#!/usr/bin/python3


import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Amenity": Amenity, "City": City,
            "Place": Place, "Review": Review, "State": State, "User": User}

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        db_Dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            for i in self.__session.query(cls):
                key = f'{type(i).__name__}.{i.id}'
                db_Dict[key] = i
            else:
                allClasses = [Amenity, City, Place, Review, State, User]
                for eachCls in allClasses:
                    for ii in self.__session.query(eachCls):
                        key = f'{type(ii).__name__}.(ii.id}'
                        db_Dict[key] = ii
           return db_Dict

    def new(self, obj):
        """Adding instance to database"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reloads from database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session



